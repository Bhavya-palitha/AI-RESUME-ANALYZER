import streamlit as st
import pdfplumber
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("background.png")

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="logo.png",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="stFileUploader"] {
    background: white;
    border-radius: 12px;
    padding: 10px;
}
/* Uploaded file name only */
[data-testid="stFileUploaderFileName"] {
    color: black !important;
    font-weight: 600;
}
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Playfair+Display:wght@600;700&display=swap');
            /* Headings style */
h1, h2, h3 {
    font-family: "Playfair Display", cursive;
    font-weight: 700;
    color: #1a1a1a;
}
            /* Normal text */
p, span, div {
    font-family: "Poppins", sans-serif;
    color: #222222;
    font-weight: 500;
}
            /* Dark green success box */
div[data-testid="stAlert"] {
    background-color: #1B5E20 !important;
    color: white !important;
    border: none !important;
}

/* Make text inside success message white */
div[data-testid="stAlert"] p {
    color: white !important;
    font-weight: 600;
}
h1, h2, h3 {
            color: #2E1F1A !important; }
/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #BFA98A;
}
/* Make all main content text dark */
.stApp {
    color: #2E1F1A;
}

/* Streamlit text elements */
.stMarkdown, .stText, .stMetric {
    color: #2E1F1A !important;
}

/* Subheaders like Skill Analysis */
h1, h2, h3 {
    color: #2E1F1A !important;
}
            /* Resume score number color */
[data-testid="stMetricValue"] {
    color: #000000 !important;
}

/* Resume score label color */
[data-testid="stMetricLabel"] {
    color: #000000 !important;
}
/* Sidebar text style */
[data-testid="stSidebar"] * {
    color: #3E2C23;
   font-family: 'Poppins', sans-serif;
   font-size: 18px;
}
[data-testid="stSidebar"] h1 { font-size: 28px; } 
[data-testid="stSidebar"] h2 { font-size: 24px; } 
[data-testid="stSidebar"] h3 {
    font-size: 22px;
    
}
/* Upload box styling */
[data-testid="stFileUploader"] {
    background-color: #D8CFC4;
    border: 2px dashed #8C7B6B;
    padding: 20px;
    border-radius: 15px;
}
/* Upload box styling */
/* Cute Glass Upload Box */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(10px);
    border: 2px dashed #8C7B6B;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
}
[data-testid="stFileUploader"]:hover {
    box-shadow: 0px 10px 30px rgba(0,0,0,0.25);
    transform: scale(1.02);
}

/* Upload button */
[data-testid="stFileUploader"] button {
    background-color: #8C7B6B;
    color: white;
    border-radius: 10px;
}

/* Drag and drop text */
[data-testid="stFileUploader"] label {
    color: #3E2C23;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)
st.sidebar.image("logo.png", width=700)
st.sidebar.markdown ("""
                     <h1 style="font-size:36px;
                     text-align:center;">
                    ☁️ AI Resume Analyzer
                     </h1>
                     """,
                     unsafe_allow_html=True

)


st.sidebar.markdown("""
✨ **Welcome!**

This AI tool helps you:

✔ Analyze your resume  
✔ Identify missing skills  
✔ Improve job readiness  
✔ Get smart suggestions  

---

💡 **How to use**

1️⃣ Upload your resume (PDF)  
2️⃣ AI scans your skills  
3️⃣ See your resume score  
4️⃣ Improve your profile  

---

🚀 Built for students & job seekers
""")
st.sidebar.markdown("---")

st.sidebar.markdown("### 📊 What this AI checks")

st.sidebar.markdown("""
✔ Skills mentioned in your resume  
✔ Missing industry skills  
✔ Resume completeness  
✔ Overall resume strength  
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🎯 Tips for a strong resume")

st.sidebar.markdown("""
• Keep your resume **1–2 pages**  
• Use **clear headings**  
• Highlight **technical skills**  
• Add **projects & achievements**  
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🛠 Technologies used")

st.sidebar.markdown("""
🤖 Python  
📄 PDFPlumber  
🎨 Streamlit  
⚡ AI Skill Analysis  
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🌟 Why use this tool?")

st.sidebar.markdown("""
This AI analyzer helps students and job seekers  
quickly improve their resumes and understand  
what skills they should add to stand out.
""")
st.sidebar.markdown("---")

st.sidebar.markdown(
"""
<p style="text-align:center; font-size:22px;">
 Built by <br>
<b>Palitha Bhavya</b>
</p>
""",
unsafe_allow_html=True
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">

<h1 style='text-align: center; 
font-family: "Dancing Script", cursive; 
color: #000000;
font-size: 55px;'>
🤖 AI Resume Analyzer
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center;
font-family: "Dancing Script", cursive;
font-size: 26px;
color:#3E2C23;'>
☁️ Upload your resume and let the AI explore your strengths ✨
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Upload file
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text from resume
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content

    # Show resume text
    st.subheader("Resume Content")
    st.subheader("📄 Resume Content")

    st.markdown(
    f"""
    <div style="
    background-color: rgba(255,255,255,0.8);
    padding:20px;
    border-radius:15px;
    color:#2E1F1A;
    font-size:16px;
    line-height:1.6;
    ">
    {text}
    </div>
    """,
    unsafe_allow_html=True
    )

    # Skills to check
    skills = [
        "python",
        "java",
        "machine learning",
        "data analysis",
        "sql",
        "communication",
        "teamwork"
    ]

    st.subheader("Skill Analysis")

    score = 0
    detected_skills = []
    missing_skills = []

    for skill in skills:
        if skill in text.lower():
            st.write(f"✅ {skill} detected")
            score += 100 / len(skills)
            detected_skills.append(skill)
        else:
            st.write(f"❌ {skill} missing")
            missing_skills.append(skill)

    # Resume score
    st.subheader("Resume Score")

    st.progress(int(score) / 100)

    st.metric(label="Resume Score", value=f"{int(score)}/100")

    if score >= 80:
            st.success("Excellent resume!")
    elif score >= 50:
            st.warning("Good resume but can be improved.")
    else:
            st.error("Your resume needs improvement.")

    # Suggest skills
    st.subheader("Suggested Skills to Add")

    if missing_skills:
                for skill in missing_skills:
                    st.write(f"🔹 {skill}")
    else:
                st.write("Your resume already includes all key skills!")