# 📷 Android Camera Object Detection with YOLOv5

![Android Camera Object Detection](https://example.com/path/to/image.png)

This project aims to provide a solution for object detection in low-light conditions using the Android camera. It utilizes YOLOv5, a state-of-the-art real-time object detection model, to identify objects in the captured images. The project is specifically designed to assist farmers in detecting objects of interest in low-light environments.

## Features

- Capture images from the Android camera using ADB commands
- Apply YOLOv5 for real-time object detection
- Highlight and label detected objects
- Designed for low-light conditions
- Targeted towards farmers and agricultural applications

## Requirements

- Android device with camera
- ADB (Android Debug Bridge) installed on your computer
- YOLOv5 model and weights
- Python environment with the required dependencies

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/sachinlodhi/LL_IntDet.git
   ```

2. Connect your Android device to your computer via USB.

3. Enable USB debugging on your Android device.

4. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Download the YOLOv5 model and weights from the official repository.

6. Copy the YOLOv5 model and weights into the project directory.

7. Run the application:

   ```
   python connector.py
   ```

## Usage

1. Launch the application on your computer.

2. Open a terminal and navigate to the project directory.

3. Connect your Android device to your computer via USB.

4. Ensure that USB debugging is enabled on your Android device.

5. Run the application:

   ```
   python main.py
   ```

6. The application will send ADB commands to the Android device to capture images.

7. YOLOv5 will process the captured images and detect objects.

8. Detected objects will be highlighted and labeled on the images.

9. The results can be accessed and analyzed within the application.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your forked repository.

5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- YOLOv5 - [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- Android Debug Bridge (ADB) - [https://developer.android.com/studio/command-line/adb](https://developer.android.com/studio/command-line/adb)

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact me at [your-email@example.com](mailto:your-email@example.com).

Happy object detecting! 😊🌱📷