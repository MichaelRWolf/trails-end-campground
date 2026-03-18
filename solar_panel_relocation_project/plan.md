# Solar Panel Removal Time-Lapse Video Plan

## Goal

Create a jaggly time-lapse video by stitching together still photos from two sets of solar panel removal shots, where each set shows the progression after panels have been removed from a line.

## Project Overview

- **Input**: 2 sets of photos taken after solar panel removal
- **Challenge**: Freehand photography with non-identical framing
- **Constraint**: Foot position mostly consistent (artistic flourish)
- **Output**: Time-lapse video with appropriate transitions

## Technology Stack Selection

### Primary Options

1. **Python + OpenCV** (Recommended)
   - Pros: Powerful image processing, good alignment algorithms, flexible
   - Cons: Requires Python knowledge

2. **FFmpeg + ImageMagick**
   - Pros: Command-line tools, very fast, good for batch processing
   - Cons: Less control over alignment algorithms

3. **Python + PIL/Pillow + MoviePy**
   - Pros: Simple, good for basic stitching
   - Cons: Limited advanced alignment features

### Selected: Python + OpenCV + MoviePy

- OpenCV for image alignment and stabilization
- MoviePy for video creation
- PIL/Pillow for image preprocessing

## Implementation Steps

### 1. File Organization

- [x] Create directory structure:

  ```text
  outside_panels/    # 21 JPEG images (IMG_2972 - IMG_2995) - Portrait orientation
  inside_panels/     # 8 JPEG images (IMG_2996 - IMG_3004) - Landscape orientation
  ```

### 2. Choose tools

- [x] Analyze photos for minimal traits that are necessary to choose very simple work flow.
  - Results documented in "Image Characteristics Analysis" section below
- [x] Suggest tools
- [x] Select tools.

#### Image Characteristics Analysis (COMPLETED)

**Analysis Method**: [`analyze_traits.py`](file:analyze_traits.py) script + manual verification

- Script examined file sizes, dimensions, and formats
- Checked naming patterns and sequencing
- Verified orientation consistency within sets
- Results validated through manual inspection

**Outside Panels**: 21 images

- ✅ All same size: 3024x4032 (portrait, 3:4 aspect ratio)
- ✅ All JPEG format
- ✅ Sequential naming (IMG_2972-IMG_2995)
- ✅ Consistent framing within set
- ✅ Shows external view of solar panel removal

**Inside Panels**: 8 images  

- ✅ All same size: 4032x3024 (landscape, 4:3 aspect ratio)
- ✅ All JPEG format
- ✅ Sequential naming (IMG_2996-IMG_3004)
- ✅ Consistent framing within set
- ✅ Shows internal view of solar panel removal

**Key Finding**: Each set has consistent orientation internally (Outside: portrait, Inside: landscape)

#### Tool Candidates (FOR REVIEW)

**Option 1: Python + MoviePy**

- Pros: Handles mixed orientations automatically, good for video creation, flexible
- Cons: Requires Python environment setup
- Best for: Full control over transitions and effects

**Option 2: FFmpeg (command line)**

- Pros: Very fast, handles many formats, no dependencies
- Cons: Command-line only, less control over transitions
- Best for: Simple, fast video creation

**Option 3: ImageMagick + FFmpeg**

- Pros: Powerful image processing + video creation
- Cons: More complex workflow, multiple tools
- Best for: Advanced image manipulation needs

**Option 4: Online tools (Canva, etc.)**

- Pros: No setup required, user-friendly
- Cons: Limited control, file size limits, internet required
- Best for: Quick prototypes

**RECOMMENDATION**: Start with Option 2 (FFmpeg) for simplest approach, then move to Option 1 (Python + MoviePy) if more control needed.

**Tool Selection (COMPLETED)**

**Selected**: Option 2 (FFmpeg) → Option 1 (Python + MoviePy) if needed

- Start with FFmpeg for simplest approach to get basic video working
- Move to Python + MoviePy if more control over transitions/effects needed
- Keeps options 1-4 available for future reference

**UPDATE**: Tried Option 1 (Python + MoviePy) - ABANDONED due to jankiness

- MoviePy script created and tested successfully
- However, the output quality and performance was unsatisfactory
- Moving to explore Option 3 (ImageMagick + FFmpeg) for manual point selection workflow

### 3. Stitch Raw Photos into Video

- [x] Analyze images and generate characteristic report (resolution, orientation, etc.)
- [x] **Milestone: Generate video from 3 images with very simple transition**
  - [x] Install FFmpeg
  - [x] Test `stitch_photos.py` script with 3 sample images
  - [x] Verify video output plays correctly
- [x] **Create full videos for both sets**
  - [x] [`outside_panels_full_video.mp4`](../videos.md) (21 images, 10.92s, 62.5MB)
  - [x] [`inside_panels_full_video.mp4`](../videos.md) (8 images, 4.16s, 23.0MB)
- [ ] Implement nicer transition between images
- [ ] Add longer pause on final image
- [ ] Add longer pause on first image
- [ ] Add fade after final image

### 99. Maybe, some day

- [ ] **Combine both sets into unified time-lapse**
  - Handle orientation differences (portrait vs landscape)
  - Create smooth transitions between sets
  - Add fade effects and timing adjustments

### 4. Align Images

- [ ] Pre-process images in a set to create aligned versions (e.g. image_1234.jpeg → aligned_image_1234.jpeg)
- [ ] Create aligned images in `{source_dir}/aligned/` subdirectories
- [ ] Review images in file viewer before proceeding
- [ ] Use previously created script to stitch these aligned images together

## Technical Requirements

### Dependencies

**Primary Tool**: FFmpeg

- Install via: `brew install ffmpeg` (macOS) or download from <https://ffmpeg.org/download.html>

**Python Scripts**:

```python
pillow  # For image analysis
```

**Script Requirements**:

- `stitch_photos.py` - Command-line video creation tool
  - Args: image files (positional, sequential order)
  - `--image-duration` (default: 500ms)
  - `--transition-duration` (default: 0ms)
  - `--transition-type` (default: none, options: none/fade/slide)
  - `--output` (default: output.mp4)

- `align_images.py` - Command-line image alignment tool
  - Args: image files (positional, sequential order)
  - `--output-directory` / `-o` (required) - Output directory for aligned images
  - Creates aligned versions with 'aligned_' prefix to avoid overwriting originals
  - Uses ORB feature detection and homography transformation
  - First image becomes reference, others aligned to it
  - **Naming convention**: Use `{source_dir}/aligned/` for output (e.g., `outside_panels/aligned/`)

### Key Algorithms

1. **Simple Video Creation**: Frame-by-frame assembly with timing control
2. **Image Analysis**: Basic image characteristic detection (resolution, orientation)
3. **Feature Detection**: SIFT or ORB for finding matching points (for alignment step)
4. **Image Alignment**: Homography transformation (for alignment step)

## Expected Output

- Time-lapse video showing solar panel removal progression
- Smooth transitions despite freehand photography
- Preserved artistic quality of non-identical framing
- Professional-looking final product

## File Structure

```text
solar_panel_relocation_project/
├── plan.md
├── stitch_photos.py
├── analyze_traits.py
├── align_images.py
├── outside_panels/           # 21 JPEG images (IMG_2972 - IMG_2995) - Portrait
│   └── aligned/              # Aligned versions (when created)
├── inside_panels/            # 8 JPEG images (IMG_2996 - IMG_3004) - Landscape
│   └── aligned/              # Aligned versions (when created)
├── outside_panels_full_video.mp4    # Complete outside view time-lapse (see ../videos.md)
└── inside_panels_full_video.mp4     # Complete inside view time-lapse (see ../videos.md)
```

## Next Steps

1. ✅ Analyze image characteristics (resolution, orientation, etc.)
2. ✅ **Milestone: Generate video from 3 images with very simple transition**
3. ✅ **Create full videos for both sets**
4. **Next milestone: Enhance individual videos**
   - Add transitions between images
   - Implement timing adjustments
   - Add fade effects
