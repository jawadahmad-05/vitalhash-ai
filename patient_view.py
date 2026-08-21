import streamlit as st
import time
import plotly.express as px
import folium
from streamlit_folium import st_folium
import pandas as pd
import data_mock
from logic.pdf_gen import create_medical_passport

def render():
    if st.session_state.get('emergency_mode', False):
        st.error("🆘 EMERGENCY MODE ACTIVE: Life-Saving Vitals Only")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Blood Group", "B+")
                st.write("#### ⚠️ Known Allergies")
                st.error("Penicillin, Peanuts")
            with col2:
                st.metric("Risk Level", "High (D-T2)")
                st.info("#### 🧬 VitalHash AI Note")
                st.write("Patient is on Metformin. Erratic BP detected (+15%).")
            
            if st.button("Exit Emergency Mode"):
                st.session_state.emergency_mode = False
                st.session_state.role = None
                st.rerun()
        return

    st.write("## 👤 Patient Portal")
    
    tab_vault, tab_analytics, tab_planner, tab_map, tab_profile, tab_security = st.tabs([
        "📁 Record Vault", 
        "📊 Health Trends",
        "🥗 Health Planner",
        "📍 Care Map",
        "👤 Profile",
        "🔒 Security"
    ])
    
    with tab_vault:
        render_vault()
        
    with tab_analytics:
        render_analytics()

    with tab_planner:
        render_planner()

    with tab_map:
        render_map()

    with tab_profile:
        render_profile()

    with tab_security:
        render_security()

def render_vault():
    with st.container(border=True):
        st.write("### 📤 Upload New Records")
        uploaded_file = st.file_uploader("Drop physical reports or prescriptions here", type=['pdf', 'png', 'jpg'])
        if uploaded_file:
            with st.status("VitalHash AI Scanning Report...", expanded=True) as status:
                time.sleep(1)
                status.update(label="Scanning Complete! Data enriched.", state="complete", expanded=False)
            st.success(f"Report '{uploaded_file.name}' added to your Living Medical Record.")
    
    st.divider()
    st.write("### 🗓️ Longitudinal Record Archive")
    data = {
        "Date": ["12-Oct-2025", "05-Oct-2025", "15-Aug-2025", "22-Jul-2025"],
        "Type": ["Prescription", "Lab Report", "Hospital Transfer", "Radiology"],
        "Source": ["Dr. Salman", "Patient Upload", "Mayo Hospital", "GIFT Medical"],
        "Status": ["✅ Verified", "⏳ Pending Review", "✅ Sync Verified", "✅ Verified"]
    }
    st.table(data)

def render_analytics():
    with st.container(border=True):
        st.write("### 📈 Longitudinal Health Trajectory")
        
        with st.popover("🧠 Why this analysis?"):
            st.write("**AI Insight:** Your Risk Profile is **High** due to a persistent upward slope in HbA1c (+1.5% recently) and erratic Blood Pressure readings. Our algorithm correlates these as a critical Diabetic-Hypertensive risk cluster.")
        
        df = data_mock.vitals_history
        
        col1, col2 = st.columns(2)
        with col1:
            fig1 = px.line(df, x='Month', y='HbA1c', title='HbA1c Trend (%)', color_discrete_sequence=['#8b0707'])
            fig1.update_layout(
                template="plotly_dark", 
                plot_bgcolor='rgba(0,0,0,0)', 
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=20, r=20, t=40, b=20)
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = px.line(df, x='Month', y='Systolic BP', title='Systolic Blood Pressure', color_discrete_sequence=['#ffcc00'])
            fig2.update_layout(
                template="plotly_dark", 
                plot_bgcolor='rgba(0,0,0,0)', 
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=20, r=20, t=40, b=20)
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        st.write("#### ⚖️ Weight Progression (kg)")
        fig3 = px.area(df, x='Month', y='Weight (kg)', color_discrete_sequence=['#e0e0e0'])
        fig3.update_layout(
            template="plotly_dark", 
            plot_bgcolor='rgba(0,0,0,0)', 
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig3, use_container_width=True)

def render_planner():
    st.write("### 🧠 VitalHash AI Planner")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("#### 📅 Daily Suggestions")
        for sug in data_mock.daily_suggestions:
            st.checkbox(sug)
            
        st.divider()
        st.write("#### ⚠️ Things to Avoid")
        for tip in data_mock.avoidance_tips:
            st.warning(f"**Eng:** {tip['en']}\n\n**Urdu:** {tip['ur']}")

    with col2:
        st.write("#### 🥗 Personalized Diet Plan (Diabetes Type 2)")
        plan = data_mock.diet_plans["Diabetes Type 2"]
        st.info(f"**{plan['title']}** / **{plan['title_ur']}**")
        for item in plan['items']:
            st.write(f"- {item}")
        
        st.divider()
        st.write("### 💬 Chat with AI Twin")
        if "messages" not in st.session_state: st.session_state.messages = []
        for message in st.session_state.messages:
            with st.chat_message(message["role"]): st.markdown(message["content"])
        if prompt := st.chat_input("Ask about your health..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                response = get_ai_response(prompt)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

def get_ai_response(prompt):
    prompt = prompt.lower()
    if "sugar" in prompt or "diabetes" in prompt or "hb" in prompt:
        return "Your HbA1c is currently **8.4%**, which is high (Risk Level: High). *Aap ki sugar filhal high hai, aap ko fori tor par cardiologist aur nutritionist se consult krna chahiye.*"
    elif "hello" in prompt or "hi" in prompt:
        return "Hello! I am your VitalHash AI. I can help you understand your records in English or Roman Urdu. *Salam! Main aap ka VitalHash AI assistant hun.*"
    else:
        return "I have analyzed your records. Based on your erratic BP readings (148/95), you should avoid high-sodium foods. *Aap ka blood pressure 148/95 hai, aap ko namak se parhez krna chahiye.*"

def render_map():
    st.write("### 📍 Local Care Network (Gujranwala)")
    st.write("Find specialists for your condition and nearby pharmacies to order medicines.")
    
    m = folium.Map(location=[32.1664, 74.1959], zoom_start=14)
    df = data_mock.care_network
    
    for i, row in df.iterrows():
        icon_color = 'blue' if row['type'] == 'Doctor' else 'green'
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"{row['name']} ({row['specialty']})",
            icon=folium.Icon(color=icon_color, icon='plus' if row['type'] == 'Doctor' else 'shopping-cart', prefix='fa')
        ).add_to(m)

    st_folium(m, width=1100, height=400)
    
    st.divider()
    cols = st.columns(3)
    pharmacies = df[df['type'] == 'Pharmacy']
    for idx, (p_idx, p_row) in enumerate(pharmacies.iterrows()):
        with cols[idx]:
            st.write(f"**{p_row['name']}**")
            st.write(f"Type: {p_row['specialty']}")
            if st.button(f"Order Medicines from {p_row['name']}", key=f"ord_{p_idx}"):
                st.toast(f"Ordering portal for {p_row['name']} initiated...")

def render_profile():
    st.write("### 👤 Patient Profile")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Full Name", value="Syed J.")
        st.text_input("CNIC", value="35202-7654321-1", disabled=True)
        st.date_input("Date of Birth", value=pd.to_datetime("2000-01-01"))
    with col2:
        st.selectbox("Blood Group", ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"], index=1)
        st.text_area("Known Allergies", value="Penicillin, Peanuts")
    
    # PDF Passport Logic
    st.divider()
    st.write("### 🪪 Digital Medical Passport")
    st.info("Download a cryptographically verified summary of your health history for offline use.")
    
    patient_data = {
        'name': 'Syed J.',
        'cnic': '35202-7654321-1',
        'blood_group': 'B+',
        'allergies': 'Penicillin, Peanuts'
    }
    
    if st.button("Generate Passport PDF"):
        with st.spinner("Encrypting your Health Ledger..."):
            pdf_bytes = create_medical_passport(patient_data, data_mock.vitals_history)
            st.download_button(
                label="📥 Download VitalHash Passport",
                data=pdf_bytes,
                file_name=f"VitalHash_Passport_{patient_data['name']}.pdf",
                mime="application/pdf"
            )
    
    st.button("Save Profile Changes")

def render_security():
    st.write("### Security & Access Control")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Your Active Handshake OTP", "5291")
        st.caption("Provide this code to your doctor to grant session access.")
    with col2:
        st.write("### Session Log")
        if st.session_state.access_granted:
            st.error("⚠️ ACCESS ACTIVE: Dr. Salman (Health ID: PK-992)")
            if st.button("REVOKE ALL ACCESS"):
                st.session_state.access_granted = False
                st.rerun()
        else:
            st.success("🟢 No active doctor sessions.")
