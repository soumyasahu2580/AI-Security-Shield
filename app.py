import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Security Shield - Access Gateway",
    page_icon="🛡️",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
        .login-title {
            color: #ffffff;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 5px;
            text-align: center;
        }
        .login-subtitle {
            color: #94a3b8;
            font-size: 0.95rem;
            text-align: center;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Users Database & Authentication
if "users_db" not in st.session_state:
    # Default admin user pre-registered
    st.session_state["users_db"] = {"admin": "security123"}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["current_user"] = ""

# Main App Logic
if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<p class="login-title">🛡️ AI Security Shield</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Enterprise Threat Intelligence Gateway</p>', unsafe_allow_html=True)
        
        # Tabs for Login and Register
        tab_login, tab_register = st.tabs(["🔑 Login", "📝 Register"])
        
        with tab_login:
            with st.form("login_form"):
                username = st.text_input("Username", placeholder="Enter username")
                password = st.text_input("Password", type="password", placeholder="Enter password")
                submit_login = st.form_submit_button("Login", use_container_width=True)
                
                if submit_login:
                    if username in st.session_state["users_db"] and st.session_state["users_db"][username] == password:
                        st.session_state["authenticated"] = True
                        st.session_state["current_user"] = username
                        st.success(f"Welcome back, {username}! Loading workspace...")
                        st.rerun()
                    else:
                        st.error("Invalid username or password.")
                        
        with tab_register:
            with st.form("register_form"):
                new_user = st.text_input("Choose Username", placeholder="Enter new username")
                new_pass = st.text_input("Choose Password", type="password", placeholder="Enter secure password")
                confirm_pass = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
                submit_register = st.form_submit_button("Create Account", use_container_width=True)
                
                if submit_register:
                    if not new_user or not new_pass:
                        st.error("Username aur password khali nahi ho sakte.")
                    elif new_user in st.session_state["users_db"]:
                        st.error("Yeh username pehle se exist karta hai. Dusra chunlein.")
                    elif new_pass != confirm_pass:
                        st.error("Passwords match nahi kar rahe hain.")
                    else:
                        st.session_state["users_db"][new_user] = new_pass
                        st.success("Account successfully ban gaya! Ab 'Login' tab par jakar sign in karein.")
else:
    # Logged in view
    st.markdown("---")
    st.markdown(f"## 🚀 Welcome, {st.session_state['current_user']}!")
    st.markdown("Aapka secure workspace successfully load ho chuka hai. Left sidebar se alag-alag modules (Dashboard, Phishing Detector, Deepfake Analyzer) access karein.")
    
    if st.button("Log Out", type="secondary"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = ""
        st.rerun()