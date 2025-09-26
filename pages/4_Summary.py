import streamlit as st

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
# Page Content
# ----------------------------
st.markdown('<h1 class="animated-title"> Summary of Project</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.3rem;" class="fade-in">"Insights from all dashboards in one place."</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Dashboard 1 ---
st.markdown(
    '<div class="card fade-in">'
    '<h3>🌎 Holiday Informaiton Dashboard</h3>'
    '<ul>'
    
    '<li>The dataset contains <b>44,380 holidays</b> recorded across <b>232 countries</b> covering a timeframe from <b>2010 to 2019</b> (10 years).</li>'
    
    '<li>The <b>United States recorded the highest number of holidays with 1,079</b>, followed by India (614), Spain (587), Canada (576), Malaysia (527), '
    'Germany (521), China (512), Israel (471), Taiwan (450), and Nepal (403).</li>'
    
    '<li><b>Christmas Day</b>, occurring <b>1,853 times</b>, is the most widely celebrated holiday. Other frequent global holidays include Good Friday, '
    'Easter Monday, Independence Day, New Year’s Day, New Year’s Eve, Easter Sunday, Boxing Day, Christmas Eve, and Labor Day/May Day.</li>'
    
    '<li>The majority of the holidays are <b>public holidays</b> totaling 30,663 (≈70%). There are 10,490 observances, 2,301 local holidays, and fewer than 1,000 combined special, replacement, or half-day holidays.</li>'
    
    '<li>Holidays <b>peak in December</b> (Christmas & New Year), <b>April</b> (Easter), and <b>May</b> (Labor Day), while February and September have the fewest recorded holidays globally.</li>'
    
    '<li>Some countries have a wide variety of unique holiday names while others mainly repeat global holidays. '
    'Countries that focus on observances differ from those emphasizing public holidays, showing cultural variations in recognition. '
    'Additionally, multi-day holiday streaks often occur during major religious or national festivals.</li>'
    
    '</ul>'
    '</div>',
    unsafe_allow_html=True
)


# --- Dashboard 2 ---
st.markdown(
    '<div class="card fade-in">'
    '<h3>✈️ Travelling Information Dashboard </h3>'
    '<ul>'
    
    # ✈️ Travel Activity
    '<li>The global travel industry recorded <b>409.15 million total passengers</b> between 2010 and 2019, '
    'covering <b>90 countries</b> with monthly-level data. Each record includes total, domestic, and international passengers.</li>'
    
    '<li>The <b>average daily cost of travel is 144.70 USD</b>, making trips moderately expensive yet manageable for tourists.</li>'
    
    '<li>The <b>average destination rating is 4.47/5</b>, which reflects very strong traveler satisfaction across the globe.</li>'
    
    # 🏆 Top Destinations
    '<li><b>Top types of destinations by annual visitors:</b>'
    '<ul>'
    '<li>Religious destinations → 305M annual visitors</li>'
    '<li>Historical destinations → 303M annual visitors</li>'
    '<li>Beaches → 302M annual visitors</li>'
    '<li>Nature → 287M annual visitors</li>'
    '<li>Adventure → 262M annual visitors</li>'
    '<li>Cities → 257M annual visitors</li>'
    '</ul>'
    '👉 This shows tourism is <b>diverse</b>, with travelers equally attracted to culture, history, relaxation, and recreation.</li>'
    
    # 🌐 Domestic vs International
    '<li><b>Domestic vs International Travel (2010–2020):</b> Passenger numbers grew steadily to around <b>5 billion annually</b> by 2015–2018. '
    'Domestic passengers form the backbone of traffic, while international travel also contributes strongly. '
    'In 2020, numbers dropped sharply to near zero due to global travel restrictions and pandemic impacts.</li>'
    
    # 📅 Seasonality
    '<li><b>Monthly passenger seasonality:</b>'
    '<ul>'
    '<li>2.4B – 3.4B passengers per month globally</li>'
    '<li>Peak travel: <b>May–July</b> with over 3.4B passengers</li>'
    '<li>Slow period: Late autumn & winter (~2.5B passengers)</li>'
    '</ul>'
    '👉 Summer is the <b>busiest travel season</b>, while winter records fewer trips.</li>'
    
    # 🏛️ UNESCO
    '<li><b>UNESCO vs Non-UNESCO Destinations:</b> '
    '31% (3.22K) of destinations are <b>UNESCO World Heritage Sites</b>, while 69% (7.15K) are non-UNESCO. '
    'Tourists enjoy both iconic landmarks and modern attractions like cities, beaches, and entertainment hubs.</li>'
    
    # 📊 Key dataset details
    '<li><b>Dataset 1 (Monthly Passengers):</b> 7,242 records across 90 countries, 2010–2019. '
    'Covers total, domestic, and international passenger volumes. Useful for analyzing air travel trends, seasonality, and global growth patterns.</li>'
    
    '<li><b>Dataset 2 (Tourist Destinations):</b> 2,000 destinations across 22 countries and 6 continents. '
    'Includes type of destination, cost per day, best season, tourist ratings, annual visitors, and UNESCO status. '
    'The <b>average daily cost is 148 USD</b>, with annual visitors ranging from 0.5M to 10M (avg ~5.2M).</li>'
    
    '<li><b>Annual Visitors Globally:</b> Over <b>10.37 billion recorded visitors</b> across destinations, '
    'highlighting the scale of international and domestic tourism worldwide.</li>'
    
    # 🔗 Relationship
    '<li><b>Relationship Between Both Datasets:</b> Both share the column <b>Country_code</b>, making them linkable. '
    'This allows analysis of how passenger traffic influences tourism demand. '
    'For example, countries with high international passenger volumes often also have many tourist attractions with large visitor numbers. '
    'Seasonality in passenger data can also be compared with the <b>best visiting seasons</b> of destinations.</li>'
    
    '</ul>'
    '</div>',
    unsafe_allow_html=True
)



# --- Dashboard 3 ---

st.markdown(
    '<div class="card fade-in">'
    '<h3>💹 Economic Impact Dashboard </h3>'
    '<ul>'
    
    # 📊 Dataset Overview
    '<li>The dataset spans a <b>ten–year period from 2010 to 2019</b> and contains '
    '<b>2,660 records across 266 countries and regions</b>, including both individual nations and aggregates like the World, OECD, and European Union.</li>'
    
    '<li>It tracks <b>11 key indicators</b> such as tourism receipts, arrivals, exports, departures, expenditures, GDP, inflation, and unemployment.</li>'
    
    '<li>The dataset is <b>completely clean</b> with no missing values, making it highly reliable for analysis.</li>'
    
    # 💰 Tourism Economy
    '<li>Between 2010 and 2019, the global tourism economy generated a total of <b>83 trillion USD</b> in receipts, proving the massive scale of the travel industry.</li>'
    
    '<li>In 2019, the top contributors were dominated by high–income economies and regional aggregates: '
    '<ul>'
    '<li>World → 15 trillion USD</li>'
    '<li>High–income countries → 10 trillion USD</li>'
    '<li>Post–demographic dividend nations → 9 trillion USD</li>'
    '<li>OECD members → 8 trillion USD</li>'
    '<li>Europe & Central Asia → 5 trillion USD</li>'
    '<li>European Union → 4 trillion USD</li>'
    '<li>Euro area → 3 trillion USD</li>'
    '<li>North America → 3 trillion USD</li>'
    '</ul>'
    '- Among individual nations, the <b>United States led with nearly 2 trillion USD</b> in receipts.</li>'
    
    '<li>This shows that while the <b>United States</b> is the single largest country for tourism earnings, <b>Europe dominates regionally</b>.</li>'
    
    # ✈️ Travel & Arrivals
    '<li>Global air passenger numbers reached <b>35 billion</b> between 2010 and 2019, reflecting continuous growth in international mobility.</li>'
    
    '<li>Tourism arrivals rose steadily from <b>20 billion in 2010</b> to a cumulative <b>83 billion in 2019</b>.</li>'
    
    '<li>Tourism receipts grew in parallel with arrivals, proving that <b>more travelers consistently drive higher earnings</b>.</li>'
    
    # 📈 Correlations
    '<li>Statistical analysis shows strong connections between tourism and the economy: '
    '<ul>'
    '<li>Receipts ↔ Arrivals → 0.87 correlation</li>'
    '<li>Arrivals ↔ GDP → 0.96 correlation</li>'
    '<li>Receipts ↔ GDP → 0.86 correlation</li>'
    '<li>Tourism exports ↔ GDP → -0.17 (negative correlation)</li>'
    '</ul>'
    '- This indicates that richer nations depend proportionally less on tourism, while developing economies rely more heavily on it.</li>'
    
    # 👷 Tourism & Jobs
    '<li>The <b>average unemployment rate</b> across countries is <b>5.75%</b>, while unemployment adjusted by inflation averages <b>5.68%</b>.</li>'
    
    '<li>Countries with stronger tourism receipts often report <b>lower unemployment levels</b>, showing how tourism supports <b>job creation and economic stability</b>.</li>'
    
    # 🌐 Key Insights
    '<li>Overall, the data reveals clear insights: '
    '<ul>'
    '<li>Tourism receipts and arrivals grew steadily before the pandemic.</li>'
    '<li>High–income and European countries dominate absolute earnings.</li>'
    '<li>Small islands and developing economies remain heavily dependent on tourism as a share of GDP.</li>'
    '<li>Tourism growth helps stabilize unemployment and drives job creation.</li>'
    '<li>The sector is sensitive to global shocks, such as COVID–19, which is not included in this dataset but had major impacts after 2020.</li>'
    '</ul></li>'
    
    '</ul>'
    '</div>',
    unsafe_allow_html=True
)

