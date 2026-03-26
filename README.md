# 👟 Shoe Detection Dataset (acv-assignment-4): Group 2

## Overview

- **Format:** COCO JSON (original) / CSV (flattened)
    
- **Classes:** `Shoes` (ID: 0), `shoe` (ID: 1) in json (multiple rows in csv)
    
- **Source:** Roboflow Export
    

---

## Key Technical Considerations

### 1. The EXIF Orientation Issue

A common hurdle with this dataset involves images captured on mobile devices. Standard image loading libraries (like `PIL` or `OpenCV`) often ignore the **EXIF Orientation metadata** by default.

- **The Problem:** Many smartphone cameras capture images in a physical landscape orientation but add a "tag" telling the viewer to rotate it 90 degrees for portrait view.

- **The Result:** If you load the image without checking this tag, the image will appear "sideways," but the bounding box coordinates (which assume the upright view) will be completely misaligned.

- **The Fix:** Always apply `ImageOps.exif_transpose(img)` immediately after opening a file. This physically re-orients the pixel grid to match the annotation coordinate system.


### 2. Resolution & Coordinate Scaling

The dataset contains images of various sizes. To standardize the input to $512 \times 512$:

- **Resizing:** Use a linear resize.
    
- **Box Scaling:** You must calculate scale factors for width ($scale\_x$) and height ($scale\_y$).
    
- **Formula:**
    
    $$x_{new} = x_{old} \times (512 / width_{original})$$
    
    $$y_{new} = y_{old} \times (512 / height_{original})$$
    

### 3. Coordinate Format

The original COCO JSON stores boxes as `[xmin, ymin, width, height]`. The provided conversion scripts maintain this format in the CSV for consistency with common detection frameworks.

---

## 📂 Repository Structure

- `data/raw/`: Contains the source image files (`.jpg`, `.jpeg`).
    
- `_annotations.coco.json`: The original ground-truth file.
    
- `shoe_annotations.csv`: A flattened version of the annotations containing filenames, dimensions, and boxes.
    
- `visualize_dataset.ipynb`: An example notebook demonstrating the full pipeline: conversion, EXIF fixing, resizing, and visualization.