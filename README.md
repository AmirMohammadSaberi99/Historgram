# Image Histogram Utilities

This repository contains two scripts for analyzing and enhancing image contrast using OpenCV:

```
├── histogram_equalization.py   # Global histogram equalization on a grayscale image
└── color_histogram.py          # Per-channel histogram visualization for color images
```

## Requirements

* Python 3.6+
* OpenCV-Python
* Matplotlib (for plotting color histograms)

Install dependencies:

```bash
pip install opencv-python matplotlib
```

---

## 1. Global Histogram Equalization

**Script:** `histogram_equalization.py`

Enhances the contrast of a grayscale image by redistributing its intensity histogram to span the full 0–255 range.

### Usage

```bash
python histogram_equalization.py <input_image> [--output <equalized_image>]
```

* `<input_image>`: Path to a grayscale image (e.g., `photo.jpg`).
* `--output, -o`: (Optional) Path to save the equalized image.

### Example

```bash
python histogram_equalization.py lena_gray.png -o lena_eq.png
```

This will display the original and equalized images side by side and save the equalized result to `lena_eq.png`.

---

## 2. Color Channel Histogram Visualization

**Script:** `color_histogram.py`

Computes and plots histograms for the Blue, Green, and Red channels of a color image using `cv2.calcHist()` and Matplotlib.

### Usage

```bash
python color_histogram.py <input_image>
```

* `<input_image>`: Path to a color image (e.g., `scenery.jpg`).

### Example

```bash
python color_histogram.py landscape.jpg
```

This opens a Matplotlib window showing three overlaid curves (in blue, green, and red) representing the intensity distributions of each channel.

---

## License

MIT License
