import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="AI Security Shield - Enterprise Workspace",
    page_icon="🛡️",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
        .login-container {
            max-width: 450px;
            margin: auto;
            padding-top: 5rem;
        }
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0px;
        }
        .sub-header {
            font-size: 1rem;
            color: #94a3b8;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "users_db" not in st.session_state:
    st.session_state["users_db"] = {"admin": "security123"}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["current_user"] = ""

# Authentication Gateway
if not st.session_state["authenticated"]:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])
    
    with col2:
        st.markdown("## 🛡️ AI Security Shield")
        st.markdown("<p style='color: #94a3b8; font-size: 0.9rem;'>Enterprise Threat Intelligence Gateway</p>", unsafe_allow_html=True)
        
        tab_login, tab_register = st.tabs(["🔑 Login", "📝 Register"])
        
        with tab_login:
            with st.form("login_form"):
                username = st.text_input("Username", placeholder="Enter username")
                password = st.text_input("Password", type="password", placeholder="Enter password")
                submit_login = st.form_submit_button("Sign In", use_container_width=True)
                
                if submit_login:
                    if username in st.session_state["users_db"] and st.session_state["users_db"][username] == password:
                        st.session_state["authenticated"] = True
                        st.session_state["current_user"] = username
                        st.rerun()
                    else:
                        st.error("Invalid username or password.")
                        
        with tab_register:
            with st.form("register_form"):
                new_user = st.text_input("Choose Username", placeholder="New username")
                new_pass = st.text_input("Choose Password", type="password", placeholder="Secure password")
                confirm_pass = st.text_input("Confirm Password", type="password", placeholder="Confirm password")
                submit_register = st.form_submit_button("Register Account", use_container_width=True)
                
                if submit_register:
                    if not new_user or not new_pass:
                        st.error("Fields cannot be empty.")
                    elif new_user in st.session_state["users_db"]:
                        st.error("Username already exists.")
                    elif new_pass != confirm_pass:
                        st.error("Passwords do not match.")
                    else:
                        st.session_state["users_db"][new_user] = new_pass
                        st.success("Account created successfully! Please switch to Login tab.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Professional Post-Login Enterprise Dashboard View inside app.py
    top_col1, top_col2 = st.columns([6, 1])
    with top_col1:
        st.markdown(f'<p class="main-header">🛡️ Welcome, {st.session_state["current_user"].capitalize()}</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Enterprise Security Operations Center & Threat Intelligence Hub</p>', unsafe_allow_html=True)
    with top_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Log Out", type="secondary", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["current_user"] = ""
            st.rerun()

    st.divider()

    # Quick Metrics Overview
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Active Threats Monitored", value="1,428", delta="+12%")
    with m2:
        st.metric(label="Phishing URLs Blocked", value="342", delta="-4%")
    with m3:
        st.metric(label="Deepfake Files Flagged", value="89", delta="+8%")
    with m4:
        st.metric(label="System Security Health", value="98.4%", delta="+0.5%")

    st.divider()

    # Section with quick navigation / modules summary
    st.subheader("🚀 Quick Module Access & Telemetry")
    col_a, col_b = st.columns(2)

    with col_a:
        st.info("### 🎣 Phishing & URL Detector\nAnalyze suspicious domains, evaluate SSL certificates, and check blacklists in real-time using our advanced classification engine.")
        
    with col_b:
        st.success("### 🤖 Deepfake Media Analyzer\nInspect video and audio files for generative facial anomalies, frequency artifacts, and voice-cloning signatures.")

    st.divider()

    # Recent Threat Feed Table
    st.subheader("📋 Global Enterprise Security Feed")
    feed_df = pd.DataFrame({
        "Timestamp": ["2026-09-28 02:55", "2026-09-28 02:40", "2026-09-28 02:15", "2026-09-28 01:50"],
        "Vector": ["Phishing URL", "Deepfake Video", "Phishing Domain", "Voice Cloning"],
        "Source / Target": ["secure-login-verify-bank.com", "ceo_statement_fake.mp4", "update-apple-id.net", "audio_sample_09.wav"],
        "Risk Severity": ["Critical", "High", "Critical", "Medium"],
        "Status": ["Mitigated", "Quarantined", "Blocked", "Flagged"]
    })
    st.dataframe(feed_df, use_container_width=True)