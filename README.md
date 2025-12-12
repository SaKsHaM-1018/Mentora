================================================================================
MENTORA: AI-POWERED CAREER GUIDANCE SYSTEM
================================================================================

Mentora is an industry-grade career intelligence platform engineered to bridge 
the gap between academic preparation and professional employment. Leveraging 
advanced psychometric profiling algorithms, real-time market analytics, and 
AI-driven coaching, Mentora empowers students to make data-driven career 
decisions.

================================================================================
KEY FEATURES
================================================================================

1. PROFESSIONAL PERSONALITY ASSESSMENT
   - What it does: A comprehensive psychometric test based on the RIASEC model 
     (Realistic, Investigative, Artistic, Social, Enterprising, Conventional).
   - How it works: Users rate their agreement with professional statements on a 
     5-point scale.
   - Outcome: Generates a dominant personality profile and maps it to specific, 
     high-fit career roles.

2. INTELLIGENT JOB DATABASE
   - Function: A searchable, filterable database of high-growth roles 
     (e.g., Data Scientist, UX Designer).
   - Details: Provides "Deep Dive" cards that reveal critical skills, required 
     educational qualifications, and role descriptions.

3. INDIAN MARKET ANALYTICS (2024 EDITION)
   - Context: Specifically tailored to the Indian Job Market.
   - Sector Growth: Visualizes the dominance of IT/Services vs. emerging sectors 
     like Pharma and Startups.
   - Salary Trends: Tracks Average Fresher Packages (LPA) over the last 5 years.
   - Work Modes: Analyzes the shift between Remote, Hybrid, and WFO models.

4. AI INTERVIEW COACH
   - The Engine: A simulated AI logic engine that provides instant feedback 
     without needing external API keys.
   - Keyword Detection: Checks for "red flag" words (e.g., negative self-talk) 
     and "power words" (e.g., collaboration, growth).
   - Confidence Scoring: Analyzes answer length and structure.
   - Actionable Feedback: Delivers a numerical rating (1-10) and specific 
     "Pro Tips" to improve delivery.

================================================================================
TECH STACK
================================================================================

- Language: Python 3.10+
- Web Framework: Streamlit (for rapid, responsive UI)
- Data Processing: Pandas
- Visualization: Matplotlib
- Deployment Ready: Compatible with Streamlit Cloud

================================================================================
PROJECT STRUCTURE
================================================================================

Mentora_Web/
  |-- Home.py                   # Main Application Entry Point (Index Page)
  |-- requirements.txt          # List of dependencies
  |-- pages/                    # Multi-Page Modules
      |-- 1_Career_Quiz.py
      |-- 2_Job_Search.py
      |-- 3_Analytics.py
      |-- 4_AI_Coach.py
      |-- 5_About.py

================================================================================
INSTALLATION & SETUP
================================================================================

Follow these steps to run Mentora locally on your machine:

1. CLONE THE REPOSITORY
   Open your terminal and run:
   git clone https://github.com/your-username/mentora.git
   cd mentora

2. INSTALL DEPENDENCIES
   Make sure you have Python installed, then run:
   pip install -r requirements.txt

3. RUN THE APPLICATION
   Launch the app using the Streamlit CLI:
   streamlit run Home.py

4. ACCESS THE APP
   The application will automatically open in your default web browser at:
   http://localhost:8501

================================================================================
THE TEAM
================================================================================

Mentora was conceptualized and built by:

- Ramitha (Project Lead)
- Haarika (Developer)
- Saksham (Analyst)

================================================================================
LICENSE
================================================================================

This project is open-source and available for educational purposes.

(c) 2025 Mentora Systems. All Rights Reserved.
