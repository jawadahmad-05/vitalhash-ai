import streamlit as st
import pandas as pd
import time

# --- Page Config ---
st.set_page_config(
    page_title="VitalHash AI | Secure Collaborative Healthcare",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Design System (VitalGlass Theme) ---
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">', unsafe_allow_html=True)

st.markdown("""
<style>
/* Global Styles */
:root {
    --primary: #8b0707;
    --bg-dark: #0a0b0d;
    --glass: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
}

.stApp {
    background: radial-gradient(circle at 10% 20%, #1a0202 0%, #0a0b0d 100%);
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    font-family: 'Montserrat', sans-serif;
}

/* Style native Streamlit containers with border=True as Glass Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--glass);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 15px;
    border: 1px solid var(--glass-border) !important;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

.glass-card {
    background: var(--glass);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 15px;
    border: 1px solid var(--glass-border);
    padding: 20px;
    margin-bottom: 20px;
}

/* Premium Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #8b0707 0%, #5e0505 100%);
    color: white;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
    padding: 0.6rem 2.5rem;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    letter-spacing: 0.5px;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(139, 7, 7, 0.4);
    border: 1px solid rgba(255,255,255,0.3);
}

/* Animated AI Status */
.pulse-dot {
    height: 10px;
    width: 10px;
    background-color: #8b0707;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 8px #8b0707;
    animation: pulse 1.5s infinite;
    margin-right: 8px;
}

@keyframes pulse {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(139, 7, 7, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(139, 7, 7, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(139, 7, 7, 0); }
}

/* Sidebar Customization */
[data-testid="stSidebar"] {
    background-color: rgba(15, 17, 21, 0.95);
    border-right: 1px solid var(--glass-border);
}

.main-header {
    font-family: 'Montserrat', sans-serif;
    color: var(--primary);
    font-weight: 800;
    font-size: 3rem;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.sub-header {
    color: #808080;
    font-size: 1.2rem;
    margin-bottom: 2.5rem;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# --- Initialize State ---
if 'role' not in st.session_state:
    st.session_state.role = None
if 'access_granted' not in st.session_state:
    st.session_state.access_granted = False
if 'otp_requested' not in st.session_state:
    st.session_state.otp_requested = False
if 'active_patient_cnic' not in st.session_state:
    st.session_state.active_patient_cnic = None
if 'notifications' not in st.session_state:
    st.session_state.notifications = []
if 'emergency_mode' not in st.session_state:
    st.session_state.emergency_mode = False

# --- Business Logic / Mock Data ---
def logout():
    st.session_state.role = None
    st.rerun()

# --- Main App Logic ---
def main():
    st.markdown('<h1 class="main-header">VitalHash <span style="color:white;">AI</span></h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Secure Collaborative Health Ecosystem</p>', unsafe_allow_html=True)

    if st.session_state.role is None:
        # SOS Emergency Mode Trigger
        with st.container(border=True):
            st.write("### 🚨 Life-Saving Emergency Mode")
            st.write("First responders can access critical vitals (Blood Group, Allergies) instantly.")
            if st.button("🔴 ACTIVATE EMERGENCY SOS"):
                 st.session_state.role = 'Patient'
                 st.session_state.emergency_mode = True
                 st.rerun()
        
        st.write("### Welcome. Please select your portal to continue:")
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("### 👤 Patient Portal")
            st.write("Manage your records, upload papers, and chat with your AI medical twin.")
            if st.button("Enter as Patient", use_container_width=True):
                st.session_state.role = 'Patient'
                st.rerun()
        
        with col2:
            st.error("### 👨‍⚕️ Doctor Portal")
            st.write("Securely access patient history via OTP and collaborate on shared health data.")
            if st.button("Enter as doctor", use_container_width=True):
                st.session_state.role = 'Doctor'
                st.rerun()
    
    else:
        # Sidebar Navigation
        with st.sidebar:
            st.write(f"Logged in as: **{st.session_state.role}**")
            if st.button("Logout / Switch Role"):
                logout()
            
            st.divider()
            
            if st.session_state.role == 'Patient':
                st.write("### 🔔 Active Access")
                if st.session_state.access_granted:
                    st.warning("⚠️ Dr. Salman is currently viewing your record.")
                    if st.button("REVOKE ACCESS NOW", key="revoke_btn"):
                        st.session_state.access_granted = False
                        st.success("Access revoked successfully.")
                        st.rerun()
                else:
                    st.write("No active doctor sessions.")

        # Load View based on role
        if st.session_state.role == 'Patient':
            render_patient_view()
        else:
            render_doctor_view()

# --- Placeholder Views (Will move to files later) ---
def render_patient_view():
    import patient_view
    patient_view.render()

def render_doctor_view():
    import doctor_view
    doctor_view.render()

if __name__ == "__main__":
    main()
