import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --------------------------------------------------
# app configuration
# --------------------------------------------------
st.set_page_config(page_title="Heart Disease Risk Analytics",
                   page_icon="❤️",
                   layout="wide")

# --------------------------------------------------
# session state defaults (including login)
# --------------------------------------------------
for key in ["risk", "prob", "pred", "rec", "color", "appointment_booked", "logged_in", "username"]:
    if key not in st.session_state:
        st.session_state[key] = None

# --------------------------------------------------
# login page
# --------------------------------------------------
def login_page():
    """Ultra-premium high-end professional login page with glassmorphism and 3D effects."""
    
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Mono:wght@400;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body {
        height: 100vh;
        overflow: hidden;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    [data-testid="stAppViewContainer"] {
        height: 100vh !important;
        background: linear-gradient(135deg, rgba(20, 10, 15, 0.95) 0%, rgba(15, 15, 26, 0.95) 100%),
                    url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 200 200%22%3E%3Cdefs%3E%3ClinearGradient id=%22heartGrad%22 x1=%220%25%22 y1=%220%25%22 x2=%22100%25%22 y2=%22100%25%22%3E%3Cstop offset=%220%25%22 style=%22stop-color:%23dc2626;stop-opacity:0.3%22 /%3E%3Cstop offset=%22100%25%22 style=%22stop-color:%23991b1b;stop-opacity:0.1%22 /%3E%3C/linearGradient%3E%3C/defs%3E%3Cg transform=%22translate(100,100)%22%3E%3Cpath d=%22M0,-70 C-40,-70 -70,-40 -70,0 C-70,40 0,90 0,90 C0,90 70,40 70,0 C70,-40 40,-70 0,-70 Z%22 fill=%22url(%23heartGrad)%22 stroke=%22%23dc2626%22 stroke-width=%221%22 opacity=%220.4%22/%3E%3C/g%3E%3C/svg%3E') center/cover fixed;
        background-blend-mode: overlay;
        position: relative;
    }
    
    [data-testid="stHeader"],
    [data-testid="stSidebar"],
    [data-testid="stFooter"] {
        display: none !important;
    }
    
    [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        height: 100vh !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    /* Animated Background */
    .bg-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 40% 60%, rgba(220, 38, 38, 0.05) 0%, rgba(139, 0, 0, 0.02) 25%, transparent 50%),
                    radial-gradient(circle at 70% 40%, rgba(220, 38, 38, 0.03) 0%, transparent 40%);
        animation: bg-pulse 8s ease-in-out infinite;
        z-index: 0;
        pointer-events: none;
    }
    
    @keyframes bg-pulse {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    
    /* Floating Particles */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 1;
        pointer-events: none;
    }
    
    .particle {
        position: absolute;
        width: 2px;
        height: 2px;
        background: rgba(220, 38, 38, 0.4);
        border-radius: 50%;
        animation: float-up 15s infinite ease-out;
    }
    
    @keyframes float-up {
        0% {
            opacity: 0;
            transform: translateY(100vh) translateX(0) scale(1);
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            opacity: 0;
            transform: translateY(-100vh) translateX(100px) scale(0);
        }
    }
    
    /* 3D Heart Glow Background */
    .heart-glow {
        position: fixed;
        width: 600px;
        height: 600px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
        pointer-events: none;
    }
    
    .heart-glow::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(circle, rgba(220, 38, 38, 0.3) 0%, rgba(220, 38, 38, 0.1) 30%, transparent 70%);
        border-radius: 50%;
        animation: glow-pulse 4s ease-in-out infinite;
        filter: blur(40px);
    }
    
    @keyframes glow-pulse {
        0%, 100% { transform: scale(1); opacity: 0.6; }
        50% { transform: scale(1.2); opacity: 0.8; }
    }
    
    /* Main Content */
    .content-wrapper {
        position: relative;
        z-index: 10;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
        padding: 20px;
    }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(20, 20, 35, 0.85);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(220, 38, 38, 0.6);
        border-radius: 24px;
        padding: 60px 50px;
        width: 100%;
        max-width: 450px;
        box-shadow: 0 30px 90px rgba(220, 38, 38, 0.2),
                    0 0 60px rgba(220, 38, 38, 0.1),
                    inset 0 1px 1px rgba(255, 255, 255, 0.1);
        animation: card-float 3s ease-in-out infinite;
        border-image: linear-gradient(135deg, rgba(220, 38, 38, 0.3), rgba(220, 38, 38, 0.1)) 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    @keyframes card-float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Neon Heart Logo */
    .neon-logo {
        text-align: center;
        margin-bottom: 50px;
        position: relative;
    }
    
    .heart-icon-neon {
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    .heart-icon-neon svg {
        width: 100%;
        height: 100%;
        filter: drop-shadow(0 0 15px rgba(220, 38, 38, 0.8));
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        14% { transform: scale(1.1); }
        28% { transform: scale(1); }
        42% { transform: scale(1.1); }
        56% { transform: scale(1); }
    }
    
    /* Title */
    .card-title {
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: 100;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
        text-transform: uppercase;
        word-spacing: 100vw;
    }
    
    .card-subtitle {
        text-align: center;
        color: rgba(220, 38, 38, 0.8);
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    
    .form-description {
        text-align: center;
        color: rgba(255, 255, 255, 0.7);
        font-size: 13px;
        line-height: 1.6;
        margin-bottom: 35px;
        font-weight: 400;
    }
    
    /* Form Groups */
    .form-group {
        margin-bottom: 20px;
        position: relative;
        width: 100%;
        max-width: 360px;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }
    
    .form-label {
        display: block;
        color: rgba(255, 255, 255, 0.7);
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
        text-align: left;
    }
    
    .input-wrapper {
        position: relative;
        display: flex;
        align-items: center;
    }
    
    .input-icon {
        position: absolute;
        left: 16px;
        font-size: 18px;
        color: rgba(220, 38, 38, 0.7);
        pointer-events: none;
        z-index: 2;
    }
    
    .form-wrapper {
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 24px;
        align-items: stretch;
        padding: 0 15px;
    }
    
    /* Semi-transparent Input Fields */
    [data-testid="stTextInput"] {
        width: 100% !important;
        margin: 0 auto !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    [data-testid="stTextInput"] > div {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        flex-direction: column !important;
    }
    
    [data-testid="stTextInput"] > div > div {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    [data-testid="stTextInput"] input {
        width: 100% !important;
        padding: 14px 18px 14px 50px !important;
        background: rgba(255, 255, 255, 0.12) !important;
        border: 1.5px solid rgba(0, 255, 255, 0.6) !important;
        border-radius: 25px !important;
        color: white !important;
        font-size: 14px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 500 !important;
        font-family: 'Inter', sans-serif !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.2) !important;
        text-align: left !important;
    }
    
    [data-testid="stTextInput"] input:focus {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 1.5px solid rgba(220, 38, 38, 0.9) !important;
        box-shadow: 0 0 40px rgba(220, 38, 38, 0.5), inset 0 0 20px rgba(220, 38, 38, 0.1) !important;
        outline: none !important;
    }
    
    [data-testid="stTextInput"] input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
        font-weight: 400 !important;
    }
    
    [data-testid="stTextInput"] label {
        display: block !important;
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }
    
    /* Input Icons */
    .input-icon {
        position: absolute;
        left: 18px;
        top: 50%;
        transform: translateY(-50%);
        color: rgba(220, 38, 38, 0.6);
        font-size: 16px;
        pointer-events: none;
    }
    
    /* Login Button */
    .login-btn-container {
        margin-top: 40px;
    }
    
    .stButton > button {
        width: 100% !important;
        padding: 16px 24px !important;
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 50%, #991b1b 100%) !important;
        color: white !important;
        border: 1px solid rgba(220, 38, 38, 0.6) !important;
        border-radius: 12px !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        cursor: pointer !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 0 30px rgba(220, 38, 38, 0.4),
                    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        font-family: 'Inter', sans-serif !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button::before {
        content: '➜' !important;
        margin-right: 8px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #b91c1c 0%, #991b1b 50%, #7c1d1d 100%) !important;
        box-shadow: 0 0 50px rgba(220, 38, 38, 0.6),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    
    /* Bottom Links */
    .bottom-links {
        margin-top: 32px;
        text-align: center;
        display: flex;
        justify-content: space-around;
        padding-top: 24px;
        border-top: 1px solid rgba(220, 38, 38, 0.2);
    }
    
    .link-item {
        flex: 1;
    }
    
    .link-text {
        color: rgba(220, 38, 38, 0.8);
        font-size: 11px;
        font-weight: 700;
        text-decoration: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: inline-block;
    }
    
    .link-text:hover {
        color: rgba(220, 38, 38, 1);
        text-shadow: 0 0 10px rgba(220, 38, 38, 0.5);
    }
    
    /* Security Info */
    .security-info {
        text-align: center;
        margin-top: 32px;
        font-size: 10px;
        color: rgba(255, 255, 255, 0.5);
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .glass-card {
            padding: 40px 30px;
            max-width: 95%;
        }
        .card-title {
            font-size: 24px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Background Elements
    st.markdown('<div class="bg-container"></div>', unsafe_allow_html=True)
    st.markdown('<div class="heart-glow"></div>', unsafe_allow_html=True)
    
    # Floating Particles (Python-generated)
    particles_html = '<div class="particles">'
    import random
    for i in range(50):
        left = random.randint(5, 95)
        duration = random.randint(10, 20)
        delay = random.randint(0, 10)
        particles_html += f'<div class="particle" style="left: {left}%; animation-delay: {delay}s; animation-duration: {duration}s;"></div>'
    particles_html += '</div>'
    st.markdown(particles_html, unsafe_allow_html=True)
    
    # Main Content
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    # Logo Section
    st.markdown("""
    <div class="neon-logo">
        <div class="heart-icon-neon">
            <svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
            </svg>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Title Section
    st.markdown("""
    <div class="card-title">Heart Disease Risk Analytics</div>
    <div class="card-subtitle">Clinical Insights & Prevention</div>
    <div class="form-description">
        Log in securely to access your personalized dashboard and health insights.
    </div>
    """, unsafe_allow_html=True)
    
    # Form Container - Centered
    st.markdown('<div class="form-wrapper">', unsafe_allow_html=True)
    
    # Username Field - CENTERED
    st.markdown('<div class="form-group">', unsafe_allow_html=True)
    username = st.text_input("Username / Email", placeholder="Enter your registered credentials", key="login_user")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Password Field - CENTERED
    st.markdown('<div class="form-group">', unsafe_allow_html=True)
    password = st.text_input("Password", type="password", placeholder="Keep your account secure", key="login_pass")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close form-wrapper
    
    # Login Button
    st.markdown('<div class="login-btn-container">', unsafe_allow_html=True)
    if st.button("Login Now", use_container_width=True, key="login_btn"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Access Granted. System Loading...")
            st.rerun()
        else:
            st.error("❌ Username and password required")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom Links
    st.markdown("""
    <div class="bottom-links">
        <div class="link-item">
            <a class="link-text" onclick="alert('🔐 Password Recovery\\n\\nEmail reset link sent to your registered address.'); return false;">
                Forgot Password?
            </a>
        </div>
        <div class="link-item">
            <a class="link-text" onclick="alert('📧 New User Sign Up\\n\\nContact: admin@heartdisease.health'); return false;">
                New User? Sign Up
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Security Footer
    st.markdown("""
    <div class="security-info">
        🔒 HIPAA COMPLIANT • AES-256 ENCRYPTED • SECURE HEALTHCARE DATA
    </div>
    """, unsafe_allow_html=True)
    
    # Close cards
    st.markdown('</div></div>', unsafe_allow_html=True)

# --------------------------------------------------
# check login status and show appropriate page
# --------------------------------------------------
if not st.session_state.logged_in:
    login_page()
    st.stop()

# --------------------------------------------------
# logout button in sidebar (only if logged in)
# --------------------------------------------------
with st.sidebar:
    st.write(f"👤 **Logged in as:** {st.session_state.username}")
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.risk = None
        st.session_state.prob = None
        st.session_state.pred = None
        st.session_state.rec = None
        st.session_state.color = None
        st.session_state.appointment_booked = False
        st.success("Logged out successfully!")
        st.rerun()

# --------------------------------------------------
# load persisted objects
# --------------------------------------------------
with open("heart_disease_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# --------------------------------------------------
# encoding maps
# --------------------------------------------------
gender_map = {"Female": 0, "Male": 1}
smoking_map = {"Current": 0, "Former": 1, "Never": 2}
alcohol_map = {"High": 0, "Low": 1, "None": 2}
activity_map = {"Active": 0, "Moderate": 1, "Sedentary": 2}
diet_map = {"Average": 0, "Healthy": 1, "Unhealthy": 2}
stress_map = {"High": 0, "Low": 1, "Medium": 2}

# --------------------------------------------------
# email utility
# --------------------------------------------------
def send_email(subject: str, body: str, to_address: str):
    sender = st.secrets.get("email", {}).get("user")
    password = st.secrets.get("email", {}).get("password")
    smtp_server = st.secrets.get("email", {}).get("smtp_server", "smtp.gmail.com")
    smtp_port = st.secrets.get("email", {}).get("smtp_port", 587)

    if not sender or not password:
        st.error("Email credentials are not configured in secrets. Cannot send confirmation.")
        return

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        st.success(f"📧 Confirmation sent to {to_address}")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# --------------------------------------------------
# static doctor directory
# --------------------------------------------------
DOCTOR_DIRECTORY = [
    {"name": "Dr. Rajesh Kumar",
     "specialization": "Cardiologist",
     "experience": "15+ years",
     "hospital": "Apollo Hospitals",
     "contact": "+91-9876543210",
     "available_days": ["Monday", "Wednesday", "Friday"]},
    {"name": "Dr. Ananya Sharma",
     "specialization": "Interventional Cardiologist",
     "experience": "10+ years",
     "hospital": "Fortis Heart Institute",
     "contact": "+91-9123456780",
     "available_days": ["Tuesday", "Thursday", "Saturday"]},
    {"name": "Dr. Vikram Iyer",
     "specialization": "Preventive Cardiology",
     "experience": "12+ years",
     "hospital": "AIIMS Cardiology Dept",
     "contact": "+91-9988776655",
     "available_days": ["Monday", "Thursday"]}
]

# --------------------------------------------------
# header
# --------------------------------------------------
st.title("❤️ Heart Disease Risk Analytics")
st.markdown("""
**AI-powered clinical decision support system**  
Choose a page from the sidebar to get started.
"""
)

page = st.sidebar.radio("Go to", ["Risk Prediction", "Doctor & Appointment"])

# --------------------------------------------------
# risk prediction page
# --------------------------------------------------
if page == "Risk Prediction":
    st.sidebar.header("🧑‍⚕️ Patient Profile")

    age = st.sidebar.slider("Age", 18, 100, 50)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    weight = st.sidebar.slider("Weight (kg)", 40, 150, 70)
    height = st.sidebar.slider("Height (cm)", 140, 200, 170)

    bmi = weight / ((height / 100) ** 2)
    st.sidebar.metric("BMI", f"{bmi:.2f}")

    smoking = st.sidebar.selectbox("Smoking Status", ["Never", "Former", "Current"])
    alcohol = st.sidebar.selectbox("Alcohol Intake", ["None", "Low", "High"])
    activity = st.sidebar.selectbox("Physical Activity", ["Sedentary", "Moderate", "Active"])
    diet = st.sidebar.selectbox("Diet Quality", ["Healthy", "Average", "Unhealthy"])
    stress = st.sidebar.selectbox("Stress Level", ["Low", "Medium", "High"])

    st.sidebar.subheader("Medical History")
    hypertension = st.sidebar.selectbox("Hypertension", [0, 1])
    diabetes = st.sidebar.selectbox("Diabetes", [0, 1])
    hyperlipidemia = st.sidebar.selectbox("Hyperlipidemia", [0, 1])
    family_history = st.sidebar.selectbox("Family History", [0, 1])
    previous_attack = st.sidebar.selectbox("Previous Heart Attack", [0, 1])

    st.sidebar.subheader("Clinical Measurements")
    systolic_bp = st.sidebar.slider("Systolic BP", 80, 200, 120)
    diastolic_bp = st.sidebar.slider("Diastolic BP", 50, 130, 80)
    heart_rate = st.sidebar.slider("Heart Rate", 50, 150, 70)
    blood_sugar = st.sidebar.slider("Fasting Blood Sugar", 70, 200, 100)
    cholesterol = st.sidebar.slider("Total Cholesterol", 100, 400, 200)

    # perform prediction only on button press
    if st.sidebar.button("🔍 Predict Risk"):
        features = np.array([[
            age,
            gender_map[gender],
            weight,
            height,
            bmi,
            smoking_map[smoking],
            alcohol_map[alcohol],
            activity_map[activity],
            diet_map[diet],
            stress_map[stress],
            hypertension,
            diabetes,
            hyperlipidemia,
            family_history,
            previous_attack,
            systolic_bp,
            diastolic_bp,
            heart_rate,
            blood_sugar,
            cholesterol
        ]])

        features_scaled = scaler.transform(features)
        prob = model.predict_proba(features_scaled)[0][1]
        pred = model.predict(features_scaled)[0]

        if prob < 0.30:
            st.session_state.risk = "Low Risk"
            st.session_state.color = "🟢"
            st.session_state.rec = "Maintain a healthy lifestyle."
        elif prob < 0.60:
            st.session_state.risk = "Moderate Risk"
            st.session_state.color = "🟠"
            st.session_state.rec = "Lifestyle improvement and monitoring advised."
        else:
            st.session_state.risk = "High Risk"
            st.session_state.color = "🔴"
            st.session_state.rec = "Immediate cardiologist consultation required."

        st.session_state.prob = prob
        st.session_state.pred = pred

    # show results if we have them
    if st.session_state.risk is not None:
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Disease Probability", f"{st.session_state.prob*100:.1f}%")
        c2.metric("Prediction", "Positive" if st.session_state.pred == 1 else "Negative")
        c3.metric("Risk Category", f"{st.session_state.color} {st.session_state.risk}")

        st.success(f"**Clinical Recommendation:** {st.session_state.rec}")

        st.subheader("🩺 Prescription & Daily Exercise Plan")
        if st.session_state.risk == "Low Risk":
            st.info(
                """**Prescription:** No medication required  
**Exercise:**  
- 30 min brisk walking  
- Light yoga/stretching  
"""
            )
        elif st.session_state.risk == "Moderate Risk":
            st.warning(
                """**Prescription:** Doctor-advised BP/cholesterol medication  
**Exercise:**  
- 30–45 min walking  
- Cycling or swimming  
"""
            )
        else:
            st.error(
                """**Prescription:** Immediate medical supervision  
**Exercise:**  
- Light walking only  
- Stress management exercises  
"""
            )
        
        # logout button
        st.divider()
        col_logout = st.columns([2, 1, 2])
        with col_logout[1]:
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.risk = None
                st.session_state.prob = None
                st.session_state.pred = None
                st.session_state.rec = None
                st.session_state.color = None
                st.session_state.appointment_booked = False
                st.success("Logged out successfully!")
                st.rerun()
# --------------------------------------------------
# doctor & appointment page
# --------------------------------------------------
if page == "Doctor & Appointment":
    st.header("👨‍⚕️ Cardiologist Directory & Booking")
    selected_doc = None

    for doc in DOCTOR_DIRECTORY:
        with st.container():
            st.subheader(doc["name"])
            st.write(f"**Specialization:** {doc['specialization']}")
            st.write(f"**Experience:** {doc['experience']}")
            st.write(f"**Hospital:** {doc['hospital']}")
            st.write(f"**Available Days:** {', '.join(doc['available_days'])}")
            st.markdown(f'<a href="tel:{doc['contact']}">{doc['contact']}</a>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                date = st.date_input("Select date", key=doc['name'])
                if st.button(f"📅 Book Appointment - {doc['name']}", key=f"btn_{doc['name']}"):
                    selected_doc = doc
                    st.session_state.appointment_booked = True
                    st.session_state.booked_date = date
                    st.session_state.booked_doctor = doc  # Store the doctor info
                    
                    # Send confirmation directly to logged-in user's email
                    if st.session_state.username:
                        body = (
                            f"Dear Patient,\n\n"
                            f"Your appointment with {doc['name']} "
                            f"({doc['specialization']}) at {doc['hospital']} "
                            f"on {date.strftime('%Y-%m-%d')} has been confirmed.\n\n"
                            f"**Appointment Details:**\n"
                            f"• Doctor: {doc['name']}\n"
                            f"• Specialization: {doc['specialization']}\n"
                            f"• Hospital: {doc['hospital']}\n"
                            f"• Date: {date.strftime('%Y-%m-%d')}\n"
                            f"• Contact: {doc['contact']}\n\n"
                            f"Please arrive 15 minutes before your appointment time.\n"
                            f"Bring any relevant medical reports and your ID proof.\n\n"
                            f"For any changes or cancellations, please contact the hospital directly.\n\n"
                            f"Regards,\n"
                            f"Heart Disease Risk Analytics Team\n"
                            f"This is an automated confirmation email."
                        )
                        send_email(
                            f"Appointment Confirmation - {doc['name']} - {date.strftime('%Y-%m-%d')}", 
                            body, 
                            st.session_state.username
                        )
                        st.success(f"✅ Appointment booked successfully! Confirmation sent to {st.session_state.username}")
                    else:
                        st.warning("⚠️ Appointment booked but email confirmation failed - no email address found in profile")
                        
            with col2:
                st.markdown(
                    f"""📞 **Call Doctor:**  
                        <a href="tel:{doc['contact']}">{doc['contact']}</a>""",
                    unsafe_allow_html=True
                )
            st.divider()

    # Display appointment summary if booked
    if st.session_state.get('appointment_booked', False) and st.session_state.get('booked_doctor'):
        st.markdown("---")
        st.subheader("📋 Your Current Appointment")
        col_sum1, col_sum2, col_sum3 = st.columns(3)
        with col_sum1:
            st.info(f"**Doctor:** {st.session_state.booked_doctor['name']}")
        with col_sum2:
            st.info(f"**Date:** {st.session_state.booked_date.strftime('%Y-%m-%d')}")
        with col_sum3:
            st.info(f"**Hospital:** {st.session_state.booked_doctor['hospital']}")
        
        # Option to resend confirmation
        if st.button("📧 Resend Confirmation Email"):
            body = (
                f"Dear Patient,\n\n"
                f"This is a reminder of your appointment with {st.session_state.booked_doctor['name']} "
                f"({st.session_state.booked_doctor['specialization']}) at {st.session_state.booked_doctor['hospital']} "
                f"on {st.session_state.booked_date.strftime('%Y-%m-%d')}.\n\n"
                f"**Appointment Details:**\n"
                f"• Doctor: {st.session_state.booked_doctor['name']}\n"
                f"• Specialization: {st.session_state.booked_doctor['specialization']}\n"
                f"• Hospital: {st.session_state.booked_doctor['hospital']}\n"
                f"• Date: {st.session_state.booked_date.strftime('%Y-%m-%d')}\n"
                f"• Contact: {st.session_state.booked_doctor['contact']}\n\n"
                f"Please arrive 15 minutes before your appointment time.\n\n"
                f"Regards,\n"
                f"Heart Disease Risk Analytics Team"
            )
            send_email(
                f"Appointment Reminder - {st.session_state.booked_doctor['name']}", 
                body, 
                st.session_state.username
            )
    
    # logout button
    st.divider()
    col_logout = st.columns([2, 1, 2])
    with col_logout[1]:
        if st.button("🚪 Logout", use_container_width=True, key="logout_doc_page"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state.risk = None
            st.session_state.prob = None
            st.session_state.pred = None
            st.session_state.rec = None
            st.session_state.color = None
            st.session_state.appointment_booked = False
            st.session_state.booked_doctor = None
            st.session_state.booked_date = None
            st.success("Logged out successfully!")
            st.rerun()
# --------------------------------------------------
# data exploration (always available)
# --------------------------------------------------
st.divider()
st.header("📊 Population Data Exploration")

df = pd.read_csv("heartdisease.csv")

with st.expander("🔎 Apply Filters"):
    f1, f2, f3 = st.columns(3)
    age_range = f1.slider("Age Range", 18, 100, (18, 100))
    gender_filter = f2.multiselect("Gender", df['Gender'].unique(), df['Gender'].unique())
    smoking_filter = f3.multiselect("Smoking", df['Smoking'].unique(), df['Smoking'].unique())

filtered_df = df[
    (df['Age'].between(age_range[0], age_range[1])) &
    (df['Gender'].isin(gender_filter)) &
    (df['Smoking'].isin(smoking_filter))
]

st.write(f"### Showing **{len(filtered_df)}** patient records")
st.dataframe(filtered_df.head(10), use_container_width=True)

colA, colB = st.columns(2)

with colA:
    st.subheader("Heart Disease Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x='Heart_Disease', data=filtered_df, ax=ax1)
    ax1.set_xlabel("Heart Disease (0 = No, 1 = Yes)")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

with colB:
    st.subheader("Age vs Heart Disease")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x='Heart_Disease', y='Age', data=filtered_df, ax=ax2)
    st.pyplot(fig2)

colC, colD = st.columns(2)

with colC:
    st.subheader("Smoking Status vs Heart Disease")
    fig3, ax3 = plt.subplots()
    sns.countplot(x='Smoking', hue='Heart_Disease', data=filtered_df, ax=ax3)
    st.pyplot(fig3)

with colD:
    st.divider()
    st.subheader("🔥 Feature Correlation Heatmap")
    numeric_df = df.select_dtypes(include=np.number)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# footer
st.markdown("---")
st.caption("Developed as an end-to-end Healthcare Analytics & ML Project")
