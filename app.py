import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Security Shield - Login",
    page_icon="🛡️",
    layout="centered"
)

# Custom Styling for Professional Login Screen
st.markdown("""
    <style>
        .login-container {
            background-color: #1e293b;
            padding: 40px;
            border-radius: 12px;
            border: 1px solid #334155;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .login-title {
            color: #ffffff;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 10px;
            text-align: center;
        }
        .login-subtitle {
            color: #94a3b8;
            font-size: 0.95rem;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Main Logic
if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<p class="login-title">🛡️ AI Security Shield</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Enterprise Threat Intelligence & Access Gateway</p>', unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter admin username")
            password = st.text_input("Password", type="password", placeholder="Enter security password")
            submit_btn = st.form_submit_button("Secure Login", use_container_width=True)
            
            if submit_btn:
                # Default Credentials Check
                if username == "admin" and password == "security123":
                    st.session_state["authenticated"] = True
                    st.success("Authentication successful! Loading workspace...")
                    st.rerun()
                else:
                    st.error("Invalid credentials. Use admin / security123")
else:
    # Once logged in, show the welcome screen with direct links or instructions
    st.markdown("---")
    st.markdown("## 🚀 Welcome to AI Security Shield Workspace")
    st.markdown("Aapka secure workspace successfully load ho chuka hai. Left sidebar se alag-alag modules (Dashboard, Phishing Detector, Deepfake Analyzer) access karein.")
    
    if st.button("Log Out", type="secondary"):
        st.session_state["authenticated"] = False
        st.rerun()