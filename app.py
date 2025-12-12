import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

# --- ⚙️ PAGE CONFIGURATION (Must be the first line) ---
st.set_page_config(
    page_title="Mentora | AI Career Coach",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 🎨 CUSTOM CSS (Dark Theme & Professional Polish) ---
st.markdown("""
<style>
    /* Global Background */
    .stApp { background-color: #0E1117; color: white; }
    
    /* Headers */
    h1, h2, h3 { color: #6c5ce7 !important; font-family: 'Segoe UI', sans-serif; }
    
    /* Buttons */
    div.stButton > button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #a29bfe;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(108, 92, 231, 0.3);
    }
    
    /* Cards (Metrics) */
    div[data-testid="stMetric"] {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #363636;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1a1c24;
    }
</style>
""", unsafe_allow_html=True)

# --- 🧠 SMART AI SIMULATION ENGINE ---
def analyze_interview(question, answer):
    # Simulate processing time
    time.sleep(1.5)
    
    answer_lower = answer.lower()
    word_count = len(answer.split())
    
    # Base logic
    rating = 7
    feedback = "Solid answer. You covered the basics well."
    tip = "Try to be a bit more specific about your role."

    # Smart keyword detection
    if word_count < 15:
        rating = 3
        feedback = "Your response is too brief. Recruiters want to hear a story."
        tip = "Use the STAR method: Describe the Situation, Task, Action, and Result."
    elif "stupid" in answer_lower or "hate" in answer_lower or "bad" in answer_lower:
        rating = 2
        feedback = "Red Flag: Avoid negative language about yourself or past employers."
        tip = "Always spin weaknesses into learning opportunities."
    elif "team" in answer_lower or "collaborate" in answer_lower:
        rating = 9
        feedback = "Excellent! You highlighted your ability to work in a team."
        tip = "Quantify your impact (e.g., 'saved the team 10 hours')."
    elif "learn" in answer_lower or "grow" in answer_lower:
        rating = 8
        feedback = "Great job showing a growth mindset."
        tip = "Mention a specific skill you are currently learning."

    return rating, feedback, tip

# --- 💾 MOCK DATABASE (No MySQL needed for Web) ---
def get_job_data():
    return pd.DataFrame([
        {"Role": "Software Engineer", "Desc": "Builds scalable software solutions.", "Skills": "Python, Java, SQL, System Design", "Edu": "B.Tech CS / MCA"},
        {"Role": "Data Scientist", "Desc": "Analyzes complex data for insights.", "Skills": "Python, ML, Statistics, Pandas", "Edu": "Masters in Data Science"},
        {"Role": "Product Manager", "Desc": "Leads product vision and strategy.", "Skills": "Agile, Communication, Roadmapping", "Edu": "MBA"},
        {"Role": "UX Designer", "Desc": "Designs user-friendly interfaces.", "Skills": "Figma, Wireframing, User Research", "Edu": "Design Degree"},
        {"Role": "Cybersecurity Analyst", "Desc": "Protects networks from cyber threats.", "Skills": "Linux, Network Security, Ethical Hacking", "Edu": "B.Sc Cyber Security"},
        {"Role": "Digital Marketer", "Desc": "Drives brand growth online.", "Skills": "SEO, SEM, Google Analytics, Content", "Edu": "BBA Marketing"},
    ])

# --- 🏠 SIDEBAR ---
with st.sidebar:
    st.title("🚀 Mentora")
    st.caption("AI-Powered Career Intelligence")
    st.markdown("---")
    
    menu = st.radio("Navigate", 
        ["Home", "Career Quiz", "Search Jobs", "Market Analytics", "AI Interview Coach", "About"]
    )
    
    st.markdown("---")
    st.info("**Team:**\n\nRamitha • Haarika • Saksham")

# --- 1️⃣ HOME SECTION ---
if menu == "Home":
    st.title("Welcome to Mentora")
    st.subheader("Bridging the Gap Between Education & Employment")
    
    st.write("Mentora is your all-in-one platform for career discovery. Assess your personality, explore high-growth roles, and prepare for interviews with AI.")
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jobs Tracked", "1.5 Lakh+")
    col2.metric("Top Sector", "IT Services")
    col3.metric("Avg Fresher Salary", "₹4.5 LPA", "8.5%")
    col4.metric("AI Accuracy", "94%")

    st.markdown("---")
    st.image("https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=2070&auto=format&fit=crop", caption="Your Future Starts Here")

# --- 2️⃣ QUIZ SECTION ---
elif menu == "Career Quiz":
    st.title("⚡ Professional Personality Assessment")
    st.write("Rate your agreement with the following statements (1 = Disagree, 5 = Agree)")
    
    with st.form("quiz_form"):
        # We simulate the 20 questions with 6 key sliders for the demo
        q1 = st.slider("I prefer working with concrete data over abstract theories.", 1, 5, 3)
        q2 = st.slider("I enjoy troubleshooting hardware or machinery.", 1, 5, 3)
        q3 = st.slider("I love solving complex math or science puzzles.", 1, 5, 3)
        q4 = st.slider("I value self-expression and creativity.", 1, 5, 3)
        q5 = st.slider("I find fulfillment in mentoring or teaching others.", 1, 5, 3)
        q6 = st.slider("I am ambitious and enjoy taking charge.", 1, 5, 3)
        
        submitted = st.form_submit_button("Analyze Profile")
        
        if submitted:
            # Simple logic to determine dominant trait
            scores = {
                "Realistic": q1 + q2,
                "Investigative": q3 + 1, # weighted slightly
                "Artistic": q4 + 2,
                "Social": q5 + 2,
                "Enterprising": q6 + 2,
                "Conventional": q1 # re-using data focus
            }
            top_trait = max(scores, key=scores.get)
            
            st.success("Analysis Complete!")
            st.divider()
            
            # Result Card
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"## You are: **{top_trait}**")
                st.info("Your Dominant Personality Type")
            
            with col2:
                descriptions = {
                    "Realistic": "The Doer. You like working with your hands and tools.",
                    "Investigative": "The Thinker. You love analyzing data and solving puzzles.",
                    "Artistic": "The Creator. You value imagination and self-expression.",
                    "Social": "The Helper. You thrive when guiding or teaching others.",
                    "Enterprising": "The Persuader. You are a natural leader and risk-taker.",
                    "Conventional": "The Organizer. You value structure, order, and precision."
                }
                st.write(f"### {descriptions[top_trait]}")
                st.write("**Recommended Careers:** Engineer, Analyst, Designer, Manager.")

# --- 3️⃣ SEARCH SECTION ---
elif menu == "Search Jobs":
    st.title("🔍 Explore Job Database")
    
    df = get_job_data()
    
    search_query = st.text_input("Search by Role or Skill (e.g., 'Python', 'Design')")
    
    if search_query:
        # Filter dataframe
        mask = df.apply(lambda x: x.astype(str).str.contains(search_query, case=False)).any(axis=1)
        results = df[mask]
    else:
        results = df
    
    st.write(f"Found {len(results)} roles.")
    
    # Display as Expandable Cards
    for idx, row in results.iterrows():
        with st.expander(f"📌 {row['Role']}"):
            st.markdown(f"**Description:** {row['Desc']}")
            st.markdown(f"**🛠️ Skills:** `{row['Skills']}`")
            st.markdown(f"**🎓 Education:** {row['Edu']}")

# --- 4️⃣ ANALYTICS SECTION ---
elif menu == "Market Analytics":
    st.title("📊 Indian Market Insights 2024")
    
    tab1, tab2 = st.tabs(["Sector Overview", "Salary & Trends"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Market Share by Sector")
            labels = ['IT Services', 'Pharma', 'Banking', 'Manufacturing', 'Startups']
            sizes = [40, 15, 20, 15, 10]
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#6c5ce7', '#00cec9', '#fab1a0', '#fd79a8', '#ffeaa7'])
            # Make background transparent for dark mode
            fig1.patch.set_alpha(0)
            st.pyplot(fig1)
            st.caption("IT Services continues to dominate.")

        with col2:
            st.subheader("Open Roles (in Lakhs)")
            roles = ['Software', 'Sales', 'Ops', 'Data']
            count = [12, 8, 6, 4]
            fig2, ax2 = plt.subplots()
            ax2.bar(roles, count, color='#0984e3')
            fig2.patch.set_alpha(0)
            ax2.patch.set_alpha(0)
            # Fix text color for dark mode
            ax2.tick_params(colors='white')
            ax2.spines['bottom'].set_color('white')
            ax2.spines['left'].set_color('white')
            st.pyplot(fig2)
            st.caption("High demand for tech roles.")

    with tab2:
        st.subheader("Average Fresher Salary (₹ LPA)")
        years = [2020, 2021, 2022, 2023, 2024]
        salary = [3.5, 3.8, 4.5, 5.2, 6.0]
        
        fig3, ax3 = plt.subplots()
        ax3.plot(years, salary, marker='o', color='#fdcb6e', linewidth=2)
        fig3.patch.set_alpha(0)
        ax3.patch.set_alpha(0)
        ax3.tick_params(colors='white')
        ax3.spines['bottom'].set_color('white')
        ax3.spines['left'].set_color('white')
        st.pyplot(fig3)
        st.caption("Consistent 8% YoY growth in starting packages.")

# --- 5️⃣ AI COACH ---
elif menu == "AI Interview Coach":
    st.title("💬 AI Interview Coach")
    st.write("Select a question, type your answer, and get instant AI feedback.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        question = st.selectbox("Select Question", [
            "Tell me about yourself.",
            "What is your greatest weakness?",
            "Why should we hire you?",
            "Describe a time you failed."
        ])
        st.info(f"**Question:** {question}")
    
    with col2:
        user_answer = st.text_area("Your Answer", height=150, placeholder="Type here...")
        analyze_btn = st.button("Analyze Answer")

    if analyze_btn and user_answer:
        with st.spinner("Mentora AI is analyzing..."):
            rating, feedback, tip = analyze_interview(question, user_answer)
        
        st.markdown("---")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Rating", f"{rating}/10")
        res_col2.success(f"**Feedback:** {feedback}")
        res_col3.info(f"**Pro Tip:** {tip}")

# --- 6️⃣ ABOUT SECTION ---
elif menu == "About":
    st.title("ℹ️ About Mentora")
    
    st.markdown("""
    **Mentora** is an industry-grade career intelligence platform.
    We bridge the gap between academic preparation and professional employment using data and AI.
    """)
    
    st.markdown("### Meet the Team")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://ui-avatars.com/api/?name=Ramitha&background=6c5ce7&color=fff", width=100)
        st.write("**Ramitha**")
        st.caption("Project Lead")

    with col2:
        st.image("https://ui-avatars.com/api/?name=Haarika&background=00cec9&color=fff", width=100)
        st.write("**Haarika**")
        st.caption("Developer")

    with col3:
        st.image("https://ui-avatars.com/api/?name=Saksham&background=fdcb6e&color=fff", width=100)
        st.write("**Saksham**")
        st.caption("Analyst")
    
    st.markdown("---")
    st.write("© 2025 Mentora Systems. All Rights Reserved.")