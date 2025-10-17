#!/usr/bin/env python3
"""
Stitch photos into a time-lapse video with configurable transitions.

Usage:
    python3 stitch_photos.py [options] image1.jpg image2.jpg image3.jpg ...
    
Options:
    --image-duration DURATION    Duration per image in milliseconds (default: 500)
    --transition-duration DURATION  Duration of transitions in milliseconds (default: 0)
    --transition-type TYPE       Type of transition: none, fade, slide (default: none)
    --output FILENAME           Output video filename (default: output.mp4)
    --help                      Show this help message
"""

import argparse
import subprocess
import sys
import os
import tempfile
from pathlib import Path

def validate_image_files(image_files):
    """Validate that all image files exist and are readable."""
    valid_files = []
    for file_path in image_files:
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist")
            return None
        if not os.access(file_path, os.R_OK):
            print(f"Error: File '{file_path}' is not readable")
            return None
        valid_files.append(file_path)
    return valid_files

def get_image_info(image_path):
    """Get basic image information using ffprobe."""
    try:
        cmd = [
            'ffprobe', '-v', 'quiet', '-print_format', 'json',
            '-show_streams', image_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        import json
        data = json.loads(result.stdout)
        stream = data['streams'][0]
        return {
            'width': stream['width'],
            'height': stream['height'],
            'duration': float(stream.get('duration', 0))
        }
    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError) as e:
        print(f"Warning: Could not get info for {image_path}: {e}")
        return None

def create_ffmpeg_filter(image_files, image_duration_ms, transition_duration_ms, transition_type):
    """Create FFmpeg filter complex for video generation."""
    
    # Convert durations to seconds
    image_duration = image_duration_ms / 1000.0
    transition_duration = transition_duration_ms / 1000.0
    
    # Get image info for the first image to determine target resolution
    first_info = get_image_info(image_files[0])
    if not first_info:
        print("Error: Could not determine image dimensions")
        return None
    
    target_width = first_info['width']
    target_height = first_info['height']
    
    # Build filter complex
    filters = []
    inputs = []
    
    for i, image_path in enumerate(image_files):
        # Add input
        inputs.extend(['-i', image_path])
        
        # Scale and pad to target resolution
        scale_filter = f"[{i}:v]scale={target_width}:{target_height}:force_original_aspect_ratio=decrease,pad={target_width}:{target_height}:(ow-iw)/2:(oh-ih)/2,setsar=1[v{i}]"
        filters.append(scale_filter)
    
    # Create transitions between images
    if transition_type == "none" or transition_duration_ms == 0:
        # Simple concatenation with proper duration
        concat_inputs = "".join([f"[v{i}]" for i in range(len(image_files))])
        concat_filter = f"{concat_inputs}concat=n={len(image_files)}:v=1:a=0:unsafe=1[outv]"
        filters.append(concat_filter)
        
    elif transition_type == "fade":
        # Fade transitions
        for i in range(len(image_files) - 1):
            if i == 0:
                # First transition
                fade_filter = f"[v{i}][v{i+1}]xfade=transition=fade:duration={transition_duration}:offset={image_duration}[v{i+1}_fade]"
            else:
                # Subsequent transitions
                fade_filter = f"[v{i}_fade][v{i+1}]xfade=transition=fade:duration={transition_duration}:offset={image_duration * (i + 1)}[v{i+1}_fade]"
            filters.append(fade_filter)
        
        # Final output
        final_filter = f"[v{len(image_files)-1}_fade]format=yuv420p[outv]"
        filters.append(final_filter)
        
    elif transition_type == "slide":
        # Slide transitions
        for i in range(len(image_files) - 1):
            if i == 0:
                slide_filter = f"[v{i}][v{i+1}]xfade=transition=slideleft:duration={transition_duration}:offset={image_duration}[v{i+1}_slide]"
            else:
                slide_filter = f"[v{i}_slide][v{i+1}]xfade=transition=slideleft:duration={transition_duration}:offset={image_duration * (i + 1)}[v{i+1}_slide]"
            filters.append(slide_filter)
        
        # Final output
        final_filter = f"[v{len(image_files)-1}_slide]format=yuv420p[outv]"
        filters.append(final_filter)
    
    else:
        print(f"Error: Unknown transition type '{transition_type}'")
        return None
    
    return {
        'inputs': inputs,
        'filters': filters
    }

def create_video(image_files, image_duration_ms, transition_duration_ms, transition_type, output_file):
    """Create video using FFmpeg."""
    
    # Validate inputs
    valid_files = validate_image_files(image_files)
    if not valid_files:
        return False
    
    if len(valid_files) < 2:
        print("Error: Need at least 2 images to create a video")
        return False
    
    # Convert durations to seconds
    image_duration = image_duration_ms / 1000.0
    transition_duration = transition_duration_ms / 1000.0
    
    # Get target resolution from first image
    first_info = get_image_info(valid_files[0])
    if not first_info:
        print("Error: Could not determine image dimensions")
        return False
    
    target_width = first_info['width']
    target_height = first_info['height']
    
    # Create individual video segments
    temp_files = []
    try:
        for i, image_path in enumerate(valid_files):
            temp_file = f"temp_segment_{i}.mp4"
            temp_files.append(temp_file)
            
            # Create video segment from single image
            cmd = [
                'ffmpeg', '-y',
                '-loop', '1', '-i', image_path,
                '-t', str(image_duration),
                '-vf', f'scale={target_width}:{target_height}:force_original_aspect_ratio=decrease,pad={target_width}:{target_height}:(ow-iw)/2:(oh-ih)/2,setsar=1',
                '-pix_fmt', 'yuv420p',
                temp_file
            ]
            
            print(f"Creating segment {i+1}/{len(valid_files)}...")
            subprocess.run(cmd, check=True, capture_output=True)
        
        # Concatenate segments
        concat_file = "concat_list.txt"
        with open(concat_file, 'w') as f:
            for temp_file in temp_files:
                f.write(f"file '{temp_file}'\n")
        
        # Final concatenation
        cmd = [
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', concat_file,
            '-c', 'copy',
            output_file
        ]
        
        print("Concatenating segments...")
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"Successfully created video: {output_file}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error running FFmpeg: {e}")
        return False
    finally:
        # Clean up temp files
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        if os.path.exists("concat_list.txt"):
            os.remove("concat_list.txt")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Stitch photos into a time-lapse video",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        'images',
        nargs='+',
        help='Image files to stitch (in sequential order)'
    )
    
    parser.add_argument(
        '--image-duration',
        type=int,
        default=500,
        help='Duration per image in milliseconds (default: 500)'
    )
    
    parser.add_argument(
        '--transition-duration',
        type=int,
        default=0,
        help='Duration of transitions in milliseconds (default: 0)'
    )
    
    parser.add_argument(
        '--transition-type',
        choices=['none', 'fade', 'slide'],
        default='none',
        help='Type of transition (default: none)'
    )
    
    parser.add_argument(
        '--output',
        default='output.mp4',
        help='Output video filename (default: output.mp4)'
    )
    
    args = parser.parse_args()
    
    # Check if FFmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: FFmpeg is not installed or not in PATH")
        print("Please install FFmpeg: https://ffmpeg.org/download.html")
        return 1
    
    # Create video
    success = create_video(
        args.images,
        args.image_duration,
        args.transition_duration,
        args.transition_type,
        args.output
    )
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())