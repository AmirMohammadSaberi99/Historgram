# histogram_equalization.py

"""
Apply global histogram equalization to a grayscale image using OpenCV.
"""

import cv2
import numpy as np
import argparse

def main(input_path: str, output_path: str = None):
    # 1) Load the image in grayscale
    img_gray = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img_gray is None:
        raise FileNotFoundError(f"Cannot load image: {input_path}")

    # 2) Apply global histogram equalization
    equalized = cv2.equalizeHist(img_gray)

    # 3) Stack original and equalized for comparison
    combined = np.hstack([
        cv2.cvtColor(img_gray,  cv2.COLOR_GRAY2BGR),
        cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
    ])

    # 4) Display result
    cv2.imshow('Original (L) vs. Equalized (R)', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 5) Save if requested
    if output_path:
        cv2.imwrite(output_path, equalized)
        print(f"Equalized image saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Global histogram equalization with cv2.equalizeHist()"
    )
    parser.add_argument(
        "input_image",
        help="Path to input grayscale image (e.g. photo.jpg)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Optional path to save the equalized image"
    )
    args = parser.parse_args()

    main(args.input_image, args.output)
