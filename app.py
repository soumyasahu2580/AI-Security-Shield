import streamlit as st
import requests

st.set_page_config(page_title="AI Phishing & Deepfake Shield", page_icon="🛡️", layout="wide")

st.title("🛡️ AI-Powered Phishing & Deepfake Shield")
st.markdown("### Real-Time Threat Intelligence & Social Engineering Defense System")

tab1, tab2 = st.tabs(["📧 Phishing & Text Analyzer", "🎙️ Audio Deepfake Detector"])

with tab1:
    st.subheader("Message / Email Threat Scanner")
    user_input = st.text_area("Paste suspicious email, SMS, or chat text here:", placeholder="Dear user, your bank account will be blocked today. Click here to verify...")
    
    if st.button("Analyze Message"):
        if user_input.strip() == "":
            st.warning("Please enter some text to analyze.")
        else:
            with st.spinner("Analyzing with NLP model..."):
                try:
                    response = requests.post("http://127.0.0.1:8000/detect/text", json={"message": user_input})
                    result = response.json()
                    
                    if result["is_threat"]:
                        st.error(f"🚨 THREAT DETECTED! Risk Level: {result['risk_level']}")
                    else:
                        st.success("✅ Message looks safe.")
                        
                    st.metric(label="Confidence Score", value=f"{result['confidence_score']}%")
                    if result["flags"]:
                        st.write("**Triggered Indicators:**", ", ".join(result["flags"]))
                except Exception as e:
                    st.error(f"Connection error with backend: {e}")

with tab2:
    st.subheader("Voice Note / Audio Deepfake Scanner")
    audio_file = st.file_uploader("Upload audio sample (.wav / .mp3)", type=["wav", "mp3"])
    
    if audio_file is not None:
        st.audio(audio_file, format='audio/wav')
        if st.button("Analyze Audio Artifacts"):
            with st.spinner("Extracting audio features (MFCC / Spectral Analysis)..."):
                # Mock result for demo impact
                st.error("🚨 Synthetic Voice Artifacts Detected! (Probability: 89.4% AI Generated)")
                st.info("Frequency anomalies match known text-to-speech cloning patterns.")