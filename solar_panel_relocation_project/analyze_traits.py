#!/usr/bin/env python3
"""
Analyze minimum traits needed to choose tools for video creation.
"""

import os
from PIL import Image
import glob

def analyze_traits():
    """Analyze minimum image traits for tool selection."""
    
    print("=== MINIMUM TRAIT ANALYSIS ===")
    
    # Check both sets
    for set_name in ['set_1', 'set_2']:
        print(f"\n--- {set_name.upper()} ---")
        
        # Get all JPEG files
        jpeg_files = glob.glob(f"{set_name}/*.jpeg")
        jpg_files = glob.glob(f"{set_name}/*.jpg")
        all_files = sorted(jpeg_files + jpg_files)
        
        print(f"File count: {len(all_files)}")
        
        if not all_files:
            print("No image files found!")
            continue
            
        # Check first few images for traits
        resolutions = set()
        orientations = set()
        formats = set()
        
        for i, filepath in enumerate(all_files[:5]):  # Check first 5 images
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    resolutions.add((width, height))
                    orientations.add("landscape" if width > height else "portrait")
                    formats.add(img.format)
                    print(f"  {os.path.basename(filepath)}: {width}x{height} {img.format}")
            except Exception as e:
                print(f"  {os.path.basename(filepath)}: ERROR - {e}")
        
        # Summary for this set
        print(f"  Unique resolutions: {len(resolutions)}")
        print(f"  Unique orientations: {len(orientations)}")
        print(f"  Unique formats: {len(formats)}")
        
        if len(resolutions) == 1:
            print(f"  ✓ All images same size: {list(resolutions)[0]}")
        else:
            print(f"  ⚠ Mixed sizes: {resolutions}")
            
        if len(orientations) == 1:
            print(f"  ✓ All images same orientation: {list(orientations)[0]}")
        else:
            print(f"  ⚠ Mixed orientations: {orientations}")

if __name__ == "__main__":
    analyze_traits()