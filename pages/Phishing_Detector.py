import streamlit as st
st.title("🎣 Phishing Link & Email Detector")
url_input = st.text_input("Enter URL or text to scan:")
if st.button("Scan Threat"):
    st.info("Scanning for malicious patterns...")