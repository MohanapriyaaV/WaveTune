import streamlit as st
import cv2
import tempfile
import os
import numpy as np
from PIL import Image
from hand_utils import detect_hands_in_image, detect_hands_in_video

# Streamlit page configuration
st.set_page_config(page_title="Gesture Control Media Player", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .main {background-color: #fafafa;}
        h1, h2, h3 {color: #303030;}
        .stButton>button {
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
            padding: 0.5em 1em;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("🖐️ Gesture Control Media Player")
st.markdown("Use your hands to control media using image, video, or webcam input. Built with MediaPipe + Streamlit.")

# Sidebar options
option = st.sidebar.radio(
    "Choose Input Type",
    ["📷 Image", "📁 Folder of Images", "🎥 Video", "🎦 Webcam"],
)
st.sidebar.markdown("Made with ❤️ by Your Name")

# ========== 📷 IMAGE UPLOAD ==========
if option == "📷 Image":
    uploaded_img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_img is not None:
        file_bytes = uploaded_img.read()
        np_img = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
        result_img, landmarks = detect_hands_in_image(np_img)
        st.image(result_img, channels="BGR", caption="Detected Hand Landmarks")
        if landmarks:
            st.success("Hand landmarks detected!")
        else:
            st.warning("No hands detected.")

# ========== 📁 FOLDER OF IMAGES ==========
elif option == "📁 Folder of Images":
    uploaded_files = st.file_uploader("Upload multiple images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            st.markdown(f"**{file.name}**")
            file_bytes = file.read()
            np_img = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
            result_img, landmarks = detect_hands_in_image(np_img)
            st.image(result_img, channels="BGR", caption="Detected Hand Landmarks")

# ========== 🎥 VIDEO UPLOAD ==========
elif option == "🎥 Video":
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
    if video_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())
        tfile.close()
        stframe = st.empty()
        st.info("Processing video... please wait")
        for frame in detect_hands_in_video(tfile.name):
            stframe.image(frame, channels="BGR")

# ========== 🎦 WEBCAM ==========
elif option == "🎦 Webcam":
    st.warning("Click below to start webcam detection. (Only works if Streamlit runs locally)")
    if st.button("Start Webcam"):
        stframe = st.empty()
        for frame in detect_hands_in_video(None, is_webcam=True):
            stframe.image(frame, channels="BGR")
