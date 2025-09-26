import streamlit as st
import re
import json
from streamlit_lottie import st_lottie
from db import get_connection  

# --- Access control ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You must log in first.")
    st.switch_page("1_Welcome.py")

# ----------------------------
# CSS Styling (copied from your perfect code)
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
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Page Title + Animation
# ----------------------------
st.markdown('<h1 class="animated-title">Feedback</h1>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Load Lottie Animation ---
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_animation = load_lottiefile(
    "D:/ITM/Data_Analysis/infosys springboard Project/website/my_portfolio/assets/Rating Character Animation.json"
)
st_lottie(lottie_animation, speed=1, loop=True, quality="high", height=300, key="ratingAnim")

st.markdown('<h4 style="text-align:center;">We value your feedback!</h4>', unsafe_allow_html=True)

# ----------------------------
# Feedback Form Inputs
# ----------------------------
name = st.text_input("Your Name")
email_id = st.text_input("Your Email ID")
feedback = st.text_area("Your Feedback")
rating = st.number_input("Rating (out of 5)", min_value=0.0, max_value=5.0, step=0.5, format="%.1f")

# --- Validation ---
def validate_inputs():
    if len(name.strip()) < 2:
        st.error("❌ Name must have at least 2 characters.")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_id):
        st.error("❌ Please enter a valid email address.")
        return False
    if len(feedback.strip()) < 5:
        st.error("❌ Feedback must have at least 5 characters.")
        return False
    if rating < 0 or rating > 5:
        st.error("❌ Rating must be between 0 and 5.")
        return False
    return True

# --- Save to PostgreSQL ---
if st.button("Submit"):
    if validate_inputs():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO feedbacks (name, email_id, feedback, rating)
                VALUES (%s, %s, %s, %s)
            """, (name, email_id, feedback, rating))
            conn.commit()
            cur.close()
            conn.close()
            st.success(f"✅ Thank you! Your feedback has been saved successfully with a {rating}-star rating.")
        except Exception as e:
            st.error(f"⚠️ Error saving to database: {e}")
