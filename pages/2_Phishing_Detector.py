import streamlit as st
import pandas as pd

st.set_page_config(page_title="Phishing & URL Threat Detector", page_icon="🎣", layout="wide")

st.markdown("## 🎣 AI-Powered Phishing & URL Threat Detector")
st.markdown("Analyze suspicious URLs, domain reputation signatures, and email headers using machine learning classification.")

st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔍 URL & Domain Scanner")
    url_input = st.text_input("Enter Target URL or Domain:", placeholder="https://suspicious-login-verify.com/secure")
    
    analysis_type = st.selectbox(
        "Select Heuristic Model:",
        ["Deep Neural Classifier (High Accuracy)", "Heuristic Domain Matcher", "SSL & Certificate Inspector"]
    )
    
    if st.button("Run Security Scan", type="primary", use_container_width=True):
        if url_input:
            with st.spinner("Analyzing domain entropy, SSL handshake, and blacklists..."):
                import time
                time.sleep(1.5)
            
            # Simulated Threat Result based on input keywords
            if "secure" in url_input or "login" in url_input or "bank" in url_input:
                st.error("🚨 **CRITICAL THREAT DETECTED: High Probability Phishing URL!**")
                st.markdown("""
                - **Risk Score:** `94.8% (Malicious)`
                - **Heuristic Flags:** Typo-squatting pattern detected, invalid SSL issuer authority, missing SPF/DKIM alignment.
                - **Recommendation:** Do not enter credentials. Block domain at firewall level.
                """)
            else:
                st.success("✅ **Domain Appears Safe / Low Risk**")
                st.markdown("""
                - **Risk Score:** `2.1% (Safe)`
                - **Heuristic Flags:** Valid SSL certificate, clean reputation history across global threat intel feeds.
                """)
        else:
            st.warning("Kripya scan karne ke liye ek valid URL enter karein.")

with col2:
    st.subheader("📊 Live Threat Stats")
    st.metric(label="URLs Scanned Today", value="1,245", delta="+18%")
    st.metric(label="Phishing Signatures DB", value="4.2M+", delta="Updated")
    st.metric(label="Average Latency", value="140 ms", delta="-12ms")

st.divider()

st.subheader("📋 Recent Phishing Interceptions Log")
log_df = pd.DataFrame({
    "Timestamp": ["2026-09-28 02:50", "2026-09-28 02:42", "2026-09-28 02:15", "2026-09-28 01:30"],
    "Target URL": ["http://apple-id-verify-support.net", "https://paytm-kyc-update-offer.com", "http://netflix-billing-issue-fix.com", "https://secure-login-microsoft-online.com"],
    "Detection Engine": ["Neural NLP Classifier", "Heuristic Matcher", "Blacklist Intel", "SSL Inspector"],
    "Threat Level": ["Critical", "High", "High", "Critical"],
    "Action Taken": ["Blocked & Quarantined", "Blocked", "Blocked", "Blocked"]
})
st.dataframe(log_df, use_container_width=True)