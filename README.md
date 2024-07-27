# Cattle Counting API

### Overview

The Cattle Counter API is a tool designed to automate the counting of cattle in images using computer vision techniques. Leveraging OpenCV for image processing and masking, this API provides detection and counting of cattle in images. The project is ideal for agricultural technology applications where monitoring livestock numbers is crucial for farm management and analytics.

The Cattle Counter API is currently in development and, at this stage, uses only basic image masking techniques with the OpenCV library for cattle detection and counting. The system is in an early phase, and the techniques employed are limited to color-based segmentation and contour detection.

### Key Features

* Automatic Cattle Detection:

The API utilizes image processing techniques to detect and count cattle in digital images.
Employs color-based segmentation and contour detection to accurately identify and isolate cattle from the background.

* Image Masking:
Uses OpenCV to create masks for different color ranges, such as white, green, and brown, to enhance cattle detection.

### API Endpoints:

* Provides RESTful API endpoints for easy integration into existing systems or web applications.
Supports image upload and processing, returning the count of detected cattle along with the processed image.

### Technical Details

* Image Processing with OpenCV:
Color Conversion: Converts images to HSV (Hue, Saturation, Value) color space for more effective color-based segmentation.
Mask Creation: Applies cv2.inRange() to generate masks for different color ranges. For example, a mask for white color helps in detecting cattle that are primarily white.
Contour Detection: Detects contours in the masks to identify individual cattle. The contours are then used to calculate the number of detected cattle.

### Notice of Limitations

* Accuracy: The counting accuracy may not be sufficient for production environments due to the complexity and variability of cattle images. The current solution may not perform well under all lighting conditions, varying cattle colors, or images with significant overlap.

<img src="https://github.com/user-attachments/assets/db576e4b-53d8-4aa8-85f9-335dd524f2cf" alt="cattle01" width="600"/>

### Architeture

<img src="https://github.com/user-attachments/assets/5aa6b83b-74a4-41aa-9f3e-daceaf33611c" alt="API" width="600"/>

