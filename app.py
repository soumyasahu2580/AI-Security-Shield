import streamlit as st

st.set_page_config(page_title="AI Security Shield", page_icon="🛡️", layout="wide")

# Session state initialize karein login status ke liye
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🛡️ AI Security Shield - Login")
    st.markdown("Please enter your credentials to access the secure dashboard.")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Yahan aap apna simple hardcoded check ya backend verification rakh sakti hain
        if username == "admin" and password == "security123":
            st.session_state.logged_in = True
            st.success("Login Successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid Username or Password")

def main_app():
    st.title("Welcome to AI Security Shield Dashboard 🚀")
    st.write("Aapka secure workspace successfully load ho chuka hai. Left sidebar se alag-alag pages access karein.")
    
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

# Check agar user logged in hai ya nahi
if not st.session_state.logged_in:
    login()
else:
    main_app()