import cv2
import streamlit as st
import numpy as np
from deepface import DeepFace

# Function to analyze facial attributes using DeepFace
def analyze_frame(frame):
    result = DeepFace.analyze(img_path=frame, actions=['age', 'gender', 'race', 'emotion'],
                              enforce_detection=False,
                              detector_backend="opencv",
                              align=True,
                              silent=False)
    return result

def overlay_text_on_frame(frame, texts):
    overlay = frame.copy()
    alpha = 0.9  # Adjust the transparency of the overlay
    cv2.rectangle(overlay, (0, 0), (frame.shape[1], 100), (255, 255, 255), -1)  # White rectangle
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    text_position = 15 # Where the first text is put into the overlay
    for text in texts:
        cv2.putText(frame, text, (10, text_position), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        text_position += 20

    return frame

def facesentiment():
    # st.title("Real-Time Facial Analysis with Streamlit")
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)
    stframe = st.image([])  # Placeholder for the webcam feed

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Analyze the frame using DeepFace
        result = analyze_frame(frame)

        # Extract the face coordinates
        face_coordinates = result[0]["region"]
        x, y, w, h = face_coordinates['x'], face_coordinates['y'], face_coordinates['w'], face_coordinates['h']

        # Draw bounding box around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = f"{result[0]['dominant_emotion']}"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

        # Convert the BGR frame to RGB for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Overlay white rectangle with text on the frame
        texts = [
            f"Age: {result[0]['age']}",
            f"Face Confidence: {round(result[0]['face_confidence'],3)}",
            # f"Gender: {result[0]['dominant_gender']} {result[0]['gender'][result[0]['dominant_gender']]}",
            f"Gender: {result[0]['dominant_gender']} {round(result[0]['gender'][result[0]['dominant_gender']], 3)}",
            f"Race: {result[0]['dominant_race']}",
            f"Dominant Emotion: {result[0]['dominant_emotion']} {round(result[0]['emotion'][result[0]['dominant_emotion']], 1)}",
        ]

        frame_with_overlay = overlay_text_on_frame(frame_rgb, texts)

        # Display the frame in Streamlit
        stframe.image(frame_with_overlay, channels="RGB")

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    # Face Analysis Application #
    # st.title("Real Time Face Emotion Detection Application")
    activities = ["Webcam Face Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    st.sidebar.markdown(
        """ Developed by Shrimanta Satpati    
            Email : satpatishrimanta@gmail.com  
        """)
    if choice == "Webcam Face Detection":
        html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Real time face emotion recognition of webcam feed using OpenCV, DeepFace and Streamlit.</h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)
        facesentiment()

    elif choice == "About":
        st.subheader("About this app")

        html_temp4 = """
                                     		<div style="background-color:#98AFC7;padding:10px">
                                     		<h4 style="color:white;text-align:center;">This Application is developed by Shrimanta Satpati. </h4>
                                     		<h4 style="color:white;text-align:center;">Thanks for Visiting</h4>
                                     		</div>
                                     		<br></br>
                                     		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)

    else:
        pass

if __name__ == "__main__":
    main()