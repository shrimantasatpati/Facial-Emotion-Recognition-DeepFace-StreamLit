# Facial-Emotion-Recognition-DeepFace-StreamLit
- This project implements real-time facial emotion detection using the `deepface` library and OpenCV.
- It captures video from the webcam, detects faces, and predicts the emotions associated with each face. The emotion labels are displayed on the frames in real-time.
- to implement realtime emotion monitoring.
- Give this repository a ⭐ if you liked it, since it took me time to understand and implement this
- Made with ❤️ by [Shrimanta Satpati](https://github.com/shrimantasatpati)

## Dependencies
- [deepface](https://github.com/serengil/deepface): A deep learning facial analysis library that provides pre-trained models for facial emotion detection. It relies on TensorFlow for the underlying deep learning operations.
- [OpenCV](https://opencv.org/): An open-source computer vision library used for image and video processing.

## Usage
### Initial steps:
- Git clone this repository Run: `git clone https://github.com/shrimantasatpati/Facial-Emotion-Recognition-DeepFace-StreamLit.git`
- Run: `Facial-Emotion-Recognition-DeepFace-StreamLit`
1. Install the required dependencies:
   - You can use `pip install -r requirements.txt`
   - Or you can install dependencies individually:
      - `pip install deepface`
      - `pip install opencv-python`
3. Run the code:
   - Execute the Python script.
   - The webcam will open, and real-time facial emotion detection will start.
   - Emotion labels will be displayed on the frames around detected faces. (Using the DeepFace extended models to predict age, emotions, gender and racial identity of the persons.)

## Approach

- Import the necessary libraries: `cv2` for video capture and image processing, and `deepface` for the emotion detection model.
- Start capturing video from the default webcam using `cv2.VideoCapture()`.
- Enter a continuous loop to process each frame of the captured video.
- Convert each frame to grayscale using `cv2.cvtColor()`.
- For each detected face, extract the face ROI (Region of Interest).
- Preprocess the face image for emotion detection using the `deepface` library's built-in preprocessing function.
- Make predictions for the emotions using the pre-trained emotion detection model provided by the `deepface` library.
- Retrieve the index of the predicted emotion and map it to the corresponding emotion label.
- Draw a rectangle around the detected face and label it with the predicted emotion using `cv2.rectangle()` and `cv2.putText()`.
- Display the resulting frame with the labeled emotion using `cv2.imshow()`.
- If the 'q' key is pressed, exit the loop.
- Release the video capture and close all windows using `cap.release()` and `cv2.destroyAllWindows()`.

  ## StreamLit
  - Local Deployment on StreamLit framework.
