import streamlit as st
import json

# --- Access control ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You must log in first.")
    st.switch_page("1_Welcome.py")

# --- CSS Styling for Animated Gradient Title + Full-width iframe ---
st.markdown("""
<style>
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100%;
}
iframe {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
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
    margin-bottom: 1rem;
}
@keyframes gradientMove {
    to { background-position: 200% center; }
}
a.powerbi-link {
    display: block;
    text-align: center;
    color: #00B8A9;
    font-weight: bold;
    margin-bottom: 1rem;
    text-decoration: underline;
}
a.powerbi-link:hover {
    color: #2575fc;
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
</style>
""", unsafe_allow_html=True)

# --- Animated Gradient Title ---
st.markdown('<h1 class="animated-title"> Global Holiday & Travel Dashboard</h1>', unsafe_allow_html=True)

# --- Divider Line ---
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Embed URL Input ---
powerbi_url = st.text_input(
    "Enter your Power BI Embed URL:",
    "https://app.powerbi.com/view?r=eyJrIjoiYmUxMDIzMTYtYTYzMC00MTk2LWE3MzUtM2MxYTEzZTZlMGU0IiwidCI6ImRlMjg5MTJiLTMyYTgtNGU5MS1hZTdjLWI4YWIxYmIzOTRkMiJ9",
    label_visibility="collapsed"
)

# --- Clickable Link ---
if powerbi_url:
    st.markdown(f'<a class="powerbi-link" href="{powerbi_url}" target="_blank">Open Dashboard in New Tab</a>', unsafe_allow_html=True)

# --- Dashboard Frame ---
st.components.v1.iframe(powerbi_url, width=1800, height=470, scrolling=False)
