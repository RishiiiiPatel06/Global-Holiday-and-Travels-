import streamlit as st
import re
import json
from streamlit_lottie import st_lottie
from db import get_connection  # 👈 Import database connection

# --- Access control ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You must log in first.")
    st.switch_page("1_Welcome.py")

# ----------------------------
# Animation Loader
# ----------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

CONTACT_ANIM_PATH = "assets/Contact_Us_Character_Animation.json"
lottie_contact = load_lottiefile(CONTACT_ANIM_PATH)

# ----------------------------
# CSS Styling for Theme + Animations + Cards
# ----------------------------
st.markdown(""" 
<style>
body {
    background-color: #1E1E1E;
    color: #E0E0E0;
}
h1, h2, h3, h4, h5, h6 {
    color: #00B8A9;
}
p, li {
    color: #E0E0E0;
    font-size: 1rem;
    line-height: 1.5;
}
ul {
    padding-left: 1.2rem;
}
/* --- Animated Gradient Title --- */
.animated-title {
    font-size: 3rem;
    text-align: center;
    background: linear-gradient(90deg, #00B8A9, #2575fc, #6a11cb);
    background-size: 200% auto;
    color: #fff;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 4s linear infinite;
    margin-bottom: 0.5rem;
}
@keyframes gradientMove {
    to { background-position: 200% center; }
}
/* --- Card Styling + Glow Hover --- */
.card {
    background: #2B2B2B;
    padding: 1.2rem;
    margin: 1rem 0;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 12px 25px rgba(0, 184, 169, 0.6);
}
/* --- Fade-in Animation --- */
.fade-in {
    animation: fadeInUp 1.2s ease-in-out;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
/* --- Animated Divider --- */
.divider {
    height: 3px;
    width: 80%;
    margin: 20px auto;
    background: linear-gradient(90deg, #6a11cb, #2575fc, #00B8A9);
    border-radius: 2px;
    animation: slide 3s infinite alternate;
}
@keyframes slide {
    from { width: 40%; }
    to { width: 80%; }
}
/* --- Buttons --- */
.stButton>button {
    background-color: #00B8A9;
    color: #E0E0E0;
    border-radius: 8px;
    height: 2.5rem;
    width: 945%;
    font-size: 1rem;
    transition: background 0.3s ease, transform 0.2s ease;
}
.stButton>button:hover {
    background-color: #009688;
    transform: translateY(-3px);
}
/* --- Smooth Scroll --- */
html {
    scroll-behavior: smooth;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Page Title + Animation
# ----------------------------
st.markdown('<h1 class="animated-title">Contact Me</h1>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Animation Display
st_lottie(lottie_contact, height=300, key="contact_anim")

# --- Contact Info Cards ---
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card fade-in"><h4 style="text-align:center;">📧 Email</h4><p style="text-align:center;">codewithrishi01@gmail.com</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card fade-in"><h4 style="text-align:center;">📱 Mobile</h4><p style="text-align:center;">+91-9265997850</p></div>', unsafe_allow_html=True)

# --- Social Connect Card ---
st.markdown("""
<div class="card fade-in" style="text-align:center;">
    <h4>🌐 Connect with Me</h4>
    <p>💼 LinkedIn: <a href="https://www.linkedin.com/in/rishipatel01" target="_blank" style="color:#00B8A9;">linkedin.com/in/rishipatel01</a></p>
    <p>🐙 GitHub: <a href="https://github.com/RishiiiiPatel06" target="_blank" style="color:#00B8A9;">github.com/RishiiiiPatel06</a></p>
    <p>📷 Instagram: <a href="https://instagram.com/rishiii_._06" target="_blank" style="color:#00B8A9;">instagram.com/rishiii_._06</a></p>
</div>
""", unsafe_allow_html=True)

# --- Form Title ---
st.markdown('<h4 style="text-align:center;">Share Your Details</h4>', unsafe_allow_html=True)

# --- Form Inputs ---
full_name = st.text_input("Full Name")
contact_number = st.text_input("Contact Number")
email_id = st.text_input("Email ID")
linkedin_account = st.text_input("LinkedIn Profile URL")
github_account = st.text_input("GitHub Profile URL")
message = st.text_area("Your Message")

# --- Validation ---
def validate_inputs():
    if len(full_name.strip()) < 2:
        st.error("❌ Full name must have at least 2 characters.")
        return False
    if not re.fullmatch(r"\d{10}", contact_number):
        st.error("❌ Contact number must be exactly 10 digits.")
        return False
    if not email_id.endswith("@gmail.com"):
        st.error("❌ Email must end with @gmail.com")
        return False
    return True

# --- Save to PostgreSQL ---
if st.button("Submit"):
    if validate_inputs():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO contacts (full_name, contact_number, email, linkedin_account, github_account, message)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (full_name, contact_number, email_id, linkedin_account, github_account, message))

            conn.commit()
            cur.close()
            conn.close()
            st.success("✅ Your details have been saved successfully!")
        except Exception as e:
            st.error(f"❌ Error saving to database: {e}")
