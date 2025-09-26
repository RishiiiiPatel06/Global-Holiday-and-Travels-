import streamlit as st
import json
import os
from streamlit_lottie import st_lottie

# ----------------------------
# --- Access control ---
# ----------------------------
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You must log in first.")
    st.switch_page("1_Welcome.py")

# ----------------------------
# --- Helper function to load Lottie animations ---
# ----------------------------

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Use relative path (works both locally & on Streamlit Cloud)
lottie_world = load_lottiefile("assets/world Tour.json")

# ----------------------------
# CSS Styling for Theme + Animations + Advanced Features
# ----------------------------
st.markdown("""
<style>
body { background-color: #1E1E1E; color: #E0E0E0; }
h1, h2, h3, h4, h5, h6 { color: #00B8A9; }
p { color: #E0E0E0; }
.stButton>button {
    background-color: #00B8A9; color: #E0E0E0;
    border-radius: 8px; height: 2.5rem; width: 100%;
    font-size: 1rem; transition: background 0.3s ease, transform 0.2s ease;
}
.stButton>button:hover { background-color: #009688; transform: translateY(-3px); }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.fade-in { animation: fadeInUp 1.2s ease-in-out; }
.animated-title {
  font-size: 3rem; text-align: center;
  background: linear-gradient(90deg, #00B8A9, #2575fc, #6a11cb);
  background-size: 200% auto; color: #fff;
  background-clip: text; -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientMove 4s linear infinite;
}
@keyframes gradientMove { to { background-position: 200% center; } }
.card {
  background: #2B2B2B; padding: 1.2rem; margin: 1rem 0;
  border-radius: 12px; box-shadow: 0 6px 15px rgba(0,0,0,0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover { transform: translateY(-8px) scale(1.02); box-shadow: 0 12px 25px rgba(0, 184, 169, 0.6); }
.divider {
  height: 3px; width: 80%; margin: 20px auto;
  background: linear-gradient(90deg, #6a11cb, #2575fc, #00B8A9);
  border-radius: 2px; animation: slide 3s infinite alternate;
}
@keyframes slide { from { width: 40%; } to { width: 80%; } }
html { scroll-behavior: smooth; }
.navbar {
  position: fixed; top: 8px; left: 50%; transform: translateX(-50%);
  background: rgba(32,32,32,0.7); backdrop-filter: blur(10px);
  border-radius: 25px; padding: 0.4rem 1.5rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.4); z-index: 999;
}
.navbar a {
  color: #00B8A9; margin: 0 12px; font-weight: 600; font-size: 0.95rem;
  text-decoration: none; transition: color 0.3s ease;
}
.navbar a:hover { color: #ffffff; }
.footer { margin-top: 3rem; text-align: center; padding: 1.5rem; font-size: 0.9rem; color: #aaa; }
.footer a { margin: 0 10px; color: #00B8A9; text-decoration: none; }
.footer a:hover { color: white; }
</style>
<div class="navbar">
  <a href="#overview">Overview</a>
  <a href="#collection">Collection</a>
  <a href="#cleaning">Cleaning</a>
  <a href="#dashboard">Dashboard</a>
  <a href="#tech">Tech</a>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Page Content with Animation
# ----------------------------
st.markdown('<h1 class="animated-title">  Project :-  Global Holiday & Travel</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.3rem;" class="fade-in">"A Power BI dashboard analyzing global tourism & holidays data."</p>', unsafe_allow_html=True)

# Show only World Tour animation (centered)
st_lottie(lottie_world, key="world", height=400, speed=1, loop=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# --- Project Overview ---
st.markdown('<div id="overview" class="card fade-in"><h3>📋 Project Overview</h3><p>We developed a <b>Global Holiday & Travel Dashboard</b> to analyze worldwide tourism data.<br>This project integrates data collection, cleaning, modeling, and visualization into one powerful dashboard.</p></div>', unsafe_allow_html=True)

# --- Data Collection ---
st.markdown('<div id="collection" class="card fade-in"><h3>📂 Data Collection</h3><ul><li>Collected datasets from multiple sources such as <b>Kaggle</b> and open data portals.</li><li>Combined diverse tourism-related datasets to build a complete data model.</li></ul></div>', unsafe_allow_html=True)

# --- Data Cleaning ---
st.markdown('<div id="cleaning" class="card fade-in"><h3>🧹 Data Cleaning</h3><ul><li>Used Python libraries like <b>Pandas</b>, <b>NumPy</b>, and <b>Scikit-Learn</b> to clean and preprocess data.</li><li>Handled a large amount of <b>missing values</b> using <b>KNN Imputer</b> for accurate predictions.</li></ul></div>', unsafe_allow_html=True)

# --- Data Integration ---
st.markdown('<div class="card fade-in"><h3>🔗 Data Integration</h3><ul><li>Merged datasets using <b>Country Code, Year, Month, Date, and Country Name</b> as keys.</li><li>Created relationships in Power BI to ensure proper linking between datasets.</li></ul></div>', unsafe_allow_html=True)

# --- Dashboard Creation ---
st.markdown('<div id="dashboard" class="card fade-in"><h3>📊 Dashboard Creation</h3><ul><li>Built an <b>interactive Power BI dashboard</b> with country-wise and time-based filters.</li><li>Visualized tourism trends, patterns, and KPIs.</li></ul></div>', unsafe_allow_html=True)

# --- Website Integration ---
st.markdown('<div class="card fade-in"><h3>🌐 Website Integration</h3><ul><li>Integrated the dashboard into a <b>Streamlit website</b> for online access.</li><li>Added <b>Login & Signup authentication</b> for secure access.</li></ul></div>', unsafe_allow_html=True)

# --- Technologies Used ---
st.markdown('<div id="tech" class="card fade-in"><h3>🛠 Technologies Used</h3><ul><li>Power BI (Creating Dashboards for data analysis and visualization)</li><li>Python (for data cleaning)</li><li>PostgreSQL (Storing user information - login, contact, feedback)</li><li>Streamlit (for portfolio integration)</li><li>Lottie Animations ( Interactive UI )</li></ul></div>', unsafe_allow_html=True)



# --- Footer ---
st.markdown("""
<div class="footer">
  © 2025 Global Travel Project | Built with ❤️ using Streamlit  
  <br>
  <a href="https://github.com/RishiiiiPatel06" target="_blank">GitHub</a> |
  <a href="https://www.linkedin.com/in/rishipatel01/" target="_blank">LinkedIn</a> 
</div>
""", unsafe_allow_html=True)

