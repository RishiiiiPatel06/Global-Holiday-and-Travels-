import streamlit as st
import json
from streamlit_lottie import st_lottie

# ----------------------------
# Load Lottie Animation
# ----------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

THANKYOU_PATH = r"D:\ITM\Data_Analysis\infosys springboard Project\website\my_portfolio\assets\Thank You.json"
lottie_thankyou = load_lottiefile(THANKYOU_PATH)

# --- Access Control ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("⚠️ You must log in first.")
    st.switch_page("1_Welcome.py")  # redirect back to login page

# ----------------------------
# CSS Styling
# ----------------------------
st.markdown("""
<style>
body {
    background-color: #1E1E1E;
    color: #E0E0E0;
    text-align: center;
}
.center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 40px;
    width: 100%;
}
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 40px;
    width: 100%;
}
.stButton>button {
    background-color: #FF4B4B;
    color: #fff;
    border-radius: 8px;
    height: 3rem;
    width: 700px;   /* <<< Bigger width */
    font-size: 1.3rem;
    font-weight: bold;
    transition: background 0.3s ease, transform 0.2s ease;
}
.stButton>button:hover {
    background-color: #ff1a1a;
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Thank You Animation + Wide Button
# ----------------------------
st.markdown("<div class='center-container'>", unsafe_allow_html=True)

# Show Thank You animation
st_lottie(lottie_thankyou, height=250, key="thankyou_anim")

# Centered wide Logout button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
if st.button("Logout"):
    st.session_state['authenticated'] = False
    st.session_state['page'] = 'login'
    st.session_state["message"] = ""
    st.switch_page("1_Welcome.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
