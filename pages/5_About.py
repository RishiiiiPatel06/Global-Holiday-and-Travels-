import streamlit as st
import time
import json
from streamlit_lottie import st_lottie

# --- Access control ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You must log in first.")
    st.switch_page("1_Welcome.py")

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

/* --- Typing Subtitle --- */
.typewriter {
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #00B8A9;
    animation: typing 3s steps(30, end) infinite alternate, blink 0.75s step-end infinite;
    font-size: 1.2rem;
    color: #E0E0E0;
    text-align: center;
    margin-bottom: 1.5rem;
}
@keyframes typing { from { width: 0 } to { width: 100% } }
@keyframes blink { 50% { border-color: transparent } }

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

/* --- Smooth Scroll --- */
html { scroll-behavior: smooth; }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Lottie Animation
# ----------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_talking = load_lottiefile("assets/Talking_Character.json")

# ----------------------------
# Page Title + Divider + Animation
# ----------------------------
st.markdown('<h1 class="animated-title">About Me</h1>', unsafe_allow_html=True)

# Divider line below title
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Show animation just below divider
st_lottie(lottie_talking, height=250, key="talkingAnim")

# --- Animated Typing Intro ---
def animated_write(text, delay=0.03):
    container = st.empty()
    output = ""
    for char in text:
        output += char
        container.markdown(f"<p style='font-size:18px; color:#E0E0E0;'>{output}</p>", unsafe_allow_html=True)
        time.sleep(delay)

animated_write("Hii, I’m Rishi Patel from Gujarat, India — passionate about Data Analytics & Business Intelligence.")

# ----------------------------
# Page Content in Cards
# ----------------------------
st.markdown('<div class="card fade-in"><h3>🚀 Professional Snapshot</h3><ul><li>🎓 Final-year <b>B.Tech student in AI & Data Science</b> with a focus on Data Analytics.</li><li>🛠️ Skilled in <b>Python, SQL, Power BI, and Excel</b> for data cleaning, visualization, and reporting.</li><li>📊 Experienced in <b>KPI dashboards, ETL pipelines, and statistical analysis.</b></li><li>🔍 Passionate about <b>turning raw data into insights</b> that guide decision-making.</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="card fade-in"><h3>🧑‍💻 Technical Skills</h3><ul><li><b>Programming & Tools</b>: Python ( Pandas, NumPy, Matplotlib, Seaborn, etc.), SQL ( Joins, Aggregation & Grouping, Subqueries & CTEs, Window Functions, Date & Time Analysis, etc.), Git & Github.</li><li><b>Business Intelligence</b>: Power BI (DAX, dashboards, visualization)</li><li><b>Data Handling</b>: ETL, data cleaning, modeling, transformation.</li><li><b>Excel</b>: Pivot Tables, VLOOKUP, advanced charting</li></ul></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="card fade-in">'
    '<h3>🌟 Beyond Work</h3>'
    '<ul>'
    '<li>🏀 A <b>3-time district basketball champion</b> — twice at <b>U14</b> level and once at <b>U17</b>, also a <b>national-level player</b>.</li>'
    '<li>📈 A curious learner who enjoys solving <b>real-world business problems</b> through <b>data storytelling</b>.</li>'
    '<li>🚀 Known for strong <b>teamwork, discipline, and leadership</b> — qualities built both on the court and in professional projects.</li>'
    '</ul>'
    '</div>',
    unsafe_allow_html=True
)


st.markdown('<div class="card fade-in" style="text-align:center; color:#00B8A9;">✅ Always open to opportunities in <b>Data Analytics & Business Intelligence</b></div>', unsafe_allow_html=True)
