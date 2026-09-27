import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Security Analytics Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Custom Styling for Professional Look
st.markdown("""
    <style>
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0px;
        }
        .sub-header {
            font-size: 1rem;
            color: #94a3b8;
            margin-bottom: 30px;
        }
        .metric-card {
            background-color: #1e293b;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #334155;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Dashboard Header
st.markdown('<p class="main-header">🛡️ AI Security Shield - Threat Intelligence</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Real-time enterprise threat monitoring, phishing detection logs, and deepfake analysis telemetry.</p>', unsafe_allow_html=True)

st.divider()

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Scans Today", value="1,428", delta="+12%")
with col2:
    st.metric(label="Phishing Links Blocked", value="342", delta="-4%")
with col3:
    st.metric(label="Deepfake Media Flagged", value="89", delta="+8%")
with col4:
    st.metric(label="System Security Score", value="98.4%", delta="+0.5%")

st.divider()

# Charts Section
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📈 Threat Detection Volume (Last 7 Days)")
    chart_data = pd.DataFrame(
        np.random.randn(7, 2) * 10 + 50,
        columns=['Phishing Attempts', 'Deepfake Videos']
    )
    st.line_chart(chart_data)

with col_right:
    st.subheader("📊 System Resource Utilization")
    resource_data = pd.DataFrame(
        {
            'CPU Usage (%)': [45, 55, 40, 65, 50, 60, 48],
            'RAM Usage (%)': [70, 72, 68, 75, 71, 74, 69]
        }
    )
    st.area_chart(resource_data)

st.divider()

# Recent Activity Log Table
st.subheader("📋 Recent Security Events")
event_data = pd.DataFrame({
    "Timestamp": ["2026-09-28 02:40", "2026-09-28 02:35", "2026-09-28 02:20", "2026-09-28 01:55"],
    "Module": ["Phishing Detector", "Deepfake Analyzer", "Phishing Detector", "Deepfake Analyzer"],
    "Target / File": ["suspicious-login-verify.com", "sample_video_clip.mp4", "secure-bank-update.net", "audio_voice_clone.wav"],
    "Threat Level": ["High (Malicious)", "Critical (Fake)", "Medium (Suspicious)", "Low (Safe)"],
    "Status": ["Blocked", "Quarantined", "Blocked", "Passed"]
})

st.dataframe(event_data, use_container_width=True)