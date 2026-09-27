import streamlit as st
st.title("🎥 Deepfake Media Analyzer")
uploaded_file = st.file_uploader("Upload image or video for detection", type=["jpg", "png", "mp4"])
if uploaded_file is not None:
    st.success("File uploaded successfully. Processing analysis...")