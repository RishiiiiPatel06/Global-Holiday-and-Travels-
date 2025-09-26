import streamlit as st
import hashlib
import json
from streamlit_lottie import st_lottie
from db import get_connection  

# ----------------------------
# Animation Loader
# ----------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Paths
LOGIN_PATH = r"D:\ITM\Data_Analysis\infosys springboard Project\website\my_portfolio\assets\Login.json"
WELCOME_PATH = r"D:\ITM\Data_Analysis\infosys springboard Project\website\my_portfolio\assets\Welcome.json"
ACCOUNT_CREATED_PATH = r"D:\ITM\Data_Analysis\infosys springboard Project\website\my_portfolio\assets\Account Created.json"

# Load Animations
lottie_login = load_lottiefile(LOGIN_PATH)
lottie_welcome = load_lottiefile(WELCOME_PATH)
lottie_account_created = load_lottiefile(ACCOUNT_CREATED_PATH)

# ----------------------------
# Helpers
# ----------------------------
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

def get_user(email):
    """Fetch user by email"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT email, password_hash FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user  # (email, password_hash) or None

def add_user(email, password_hash):
    """Insert new user"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, password_hash) VALUES (%s, %s)", (email, password_hash))
    conn.commit()
    cur.close()
    conn.close()

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Login & Signup", page_icon="🔒", layout="centered")

# ----------------------------
# Global Styling
# ----------------------------
st.markdown("""
<style>
body {
    background-color: #1E1E1E;
    color: #E0E0E0;
    font-family: 'Arial', sans-serif;
}
h2 {
    text-align: center;
    color: #00B8A9;
}
label, .stTextInput>div>div>input, .stPassword>div>div>input {
    color: #E0E0E0 !important;
}
.stButton>button {
    width: 100%;
    border-radius: 8px;
    height: 2.8rem;
    color: white;
    font-size: 1rem;
    margin-top: 0.5rem;
}
.login-btn>button {
    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
}
.signup-btn>button {
    background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
}
.gray-btn>button {
    background: gray;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Session State
# ----------------------------
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if "message" not in st.session_state:
    st.session_state["message"] = ""

# ----------------------------
# Welcome Animation
# ----------------------------
def show_welcome_anim():
    st_lottie(lottie_welcome, height=200, key="welcome_anim")

# ----------------------------
# LOGIN PAGE
# ----------------------------
def login_page():
    show_welcome_anim()
    st.markdown("<h2>🔒 Secure Login</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st_lottie(lottie_login, height=300, key="login_anim")

    with col2:
        email = st.text_input("Email", placeholder="Enter your email", key='login_email')
        password = st.text_input("Password", type="password", placeholder="Enter your password", key='login_pass')
        if st.button("Login", key='login_button', use_container_width=True):
            user = get_user(email)
            if user and check_hashes(password, user[1]):  # user[1] = password_hash
                st.session_state['authenticated'] = True
                st.session_state['page'] = 'dashboard'
                st.rerun()
            else:
                st.warning("⚠️ No account found. Please sign up first.")

        col_a, col_b = st.columns(2, gap="medium")
        with col_a:
            if st.button("Forgot Password?", key='forgot', use_container_width=True):
                st.info("Password reset link will be sent to your email.")
        with col_b:
            if st.button("Go to Sign Up", key='goto_signup', use_container_width=True):
                st.session_state['page'] = 'signup'
                st.rerun()

# ----------------------------
# SIGNUP PAGE
# ----------------------------
def signup_page():
    show_welcome_anim()
    st.markdown("<h2>📝 Create Account</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st_lottie(lottie_login, height=300, key="signup_anim")

    with col2:
        new_email = st.text_input("Email", placeholder="Enter your email", key='signup_email')
        new_password = st.text_input("Password", type="password", placeholder="Enter your password", key='signup_pass')
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password", key='signup_confirm')

        if st.button("Sign Up", key='signup_button', use_container_width=True):
            if new_password != confirm_password:
                st.warning("⚠️ Passwords do not match.")
            elif len(new_password) < 6:
                st.warning("⚠️ Password should be at least 6 characters.")
            elif get_user(new_email):  # check if exists in DB
                st.warning("⚠️ User already exists.")
            else:
                hashed = make_hashes(new_password)
                add_user(new_email, hashed)
                st.success("✅ Account created successfully! Please log in.")
                st.session_state['page'] = 'login'
                st.rerun()

        col_a, col_b = st.columns(2, gap="medium")
        with col_a:
            if st.button("Back to Login", key='back_to_login', use_container_width=True):
                st.session_state['page'] = 'login'
                st.rerun()

# ----------------------------
# DASHBOARD PAGE
# ----------------------------
def dashboard_page():
    show_welcome_anim()
    st_lottie(lottie_account_created, height=300, key="account_created_anim")
    
    # Button to go to project.py
    if st.button("🚀 Go to Project Page", key="go_project", use_container_width=True):
        st.switch_page("pages/2_Project.py")

# ----------------------------
# LOGOUT PAGE
# ----------------------------
def logout_page():
    show_welcome_anim()
    if st.button("Logout", key='logout_button', use_container_width=True):
        st.session_state['authenticated'] = False
        st.session_state['page'] = 'login'
        st.session_state["message"] = ""
        st.rerun()

# ----------------------------
# PAGE ROUTER
# ----------------------------
if st.session_state['authenticated']:
    if st.session_state['page'] == 'dashboard':
        dashboard_page()
    elif st.session_state['page'] == 'logout':
        logout_page()
else:
    if st.session_state['page'] == 'login':
        login_page()
    elif st.session_state['page'] == 'signup':
        signup_page()
