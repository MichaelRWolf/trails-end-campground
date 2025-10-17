#!/usr/bin/env python3
"""
Stitch photos into a time-lapse video with configurable transitions using MoviePy.

Usage:
    python3 stitch_photos_moviepy.py [options] image1.jpg image2.jpg image3.jpg ...
    
Options:
    --image-duration DURATION    Duration per image in milliseconds (default: 500)
    --transition-duration DURATION  Duration of transitions in milliseconds (default: 0)
    --transition-type TYPE       Type of transition: none, fade, slide (default: none)
    --output FILENAME           Output video filename (default: output.mp4)
    --help                      Show this help message
"""

import argparse
import sys
import os
from pathlib import Path
from moviepy import ImageSequenceClip, concatenate_videoclips
from PIL import Image

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
    """Get basic image information using PIL."""
    try:
        with Image.open(image_path) as img:
            return {
                'width': img.width,
                'height': img.height,
                'format': img.format
            }
    except Exception as e:
        print(f"Warning: Could not get info for {image_path}: {e}")
        return None

def create_video_clips(image_files, image_duration_ms, transition_duration_ms, transition_type):
    """Create video clips from images."""
    
    # Convert durations to seconds
    image_duration = image_duration_ms / 1000.0
    transition_duration = transition_duration_ms / 1000.0
    
    clips = []
    
    for i, image_path in enumerate(image_files):
        print(f"Processing image {i+1}/{len(image_files)}: {os.path.basename(image_path)}")
        
        # Create clip from image
        clip = ImageSequenceClip([image_path], durations=[image_duration])
        clips.append(clip)
    
    return clips, transition_duration, transition_type

def create_video(image_files, image_duration_ms, transition_duration_ms, transition_type, output_file):
    """Create video using MoviePy."""
    
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
    
    try:
        print("Creating video clips...")
        clips, _, _ = create_video_clips(valid_files, image_duration_ms, transition_duration_ms, transition_type)
        
        print("Concatenating clips...")
        if transition_type == "none" or transition_duration_ms == 0:
            # Simple concatenation
            final_clip = concatenate_videoclips(clips, method="compose")
        elif transition_type == "fade":
            # Fade transitions
            final_clip = concatenate_videoclips(clips, method="compose", transition=transition_duration)
        elif transition_type == "slide":
            # Slide transitions (MoviePy doesn't have built-in slide, so we'll use fade as fallback)
            print("Note: MoviePy doesn't support slide transitions natively, using fade instead")
            final_clip = concatenate_videoclips(clips, method="compose", transition=transition_duration)
        else:
            print(f"Error: Unknown transition type '{transition_type}'")
            return False
        
        print(f"Writing video to {output_file}...")
        final_clip.write_videofile(
            output_file,
            fps=24,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        print(f"Successfully created video: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error creating video: {e}")
        return False

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Stitch photos into a time-lapse video using MoviePy",
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
