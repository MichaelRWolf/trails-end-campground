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
  set_1/             # 22 JPEG images (IMG_2972 - IMG_2995)
  set_2/             # 8 JPEG images (IMG_2996 - IMG_3004)
  ```

### 2. Choose tools

- [ ] Anayze photos for minimal traits that are necessary to choose very simple work flow.
- [ ] Suggest tools
- [ ] Select tools.

### 3. Stitch Raw Photos into Video

- [ ] Analyze images and generate characteristic report (resolution, orientation, etc.)
- [ ] **Milestone: Generate video from 3 images with very simple transition**
- [ ] Implement nicer transition between images
- [ ] Add longer pause on final image
- [ ] Add longer pause on first image
- [ ] Add fade after final image

### 4. Align Images

- [ ] Pre-process images in a set to create aligned versions (e.g. image_1234.jpeg → aligned_image_1234.jpeg)
- [ ] Review images in file viewer before proceeding
- [ ] Use previously created script to stitch these aligned images together

## Technical Requirements

### Dependencies

TBD

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
├── set_1/           # 22 JPEG images (IMG_2972 - IMG_2995)
└── set_2/           # 8 JPEG images (IMG_2996 - IMG_3004)
```

## Next Steps

1. Analyze image characteristics (resolution, orientation, etc.)
2. **Milestone: Generate video from 3 images with very simple transition**
