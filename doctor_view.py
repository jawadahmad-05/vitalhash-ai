import streamlit as st
import plotly.express as px
import folium
from streamlit_folium import st_folium
import pandas as pd
import time
import data_mock

def render():
    st.write("## 👨‍⚕️ Doctor Portal")
    
    tab_overview, tab_surveillance = st.tabs(["📋 Clinical Workspace", "🌍 Global Surveillance"])
    
    with tab_overview:
        if not st.session_state.access_granted:
            render_access_request()
        else:
            render_patient_dashboard()
            
    with tab_surveillance:
        render_surveillance()

def render_access_request():
    st.info("### 🔒 Secure Patient Record Retrieval")
    st.write("Enter Patient Phone/CNIC to request a secure OTP handshake.")
    phone = st.text_input("Patient Phone Number", placeholder="03XXXXXXXXX")
    if st.button("Request Handshake OTP"):
        if len(phone) >= 10:
            st.session_state.otp_requested = True
            st.success("OTP sent. Waiting for patient to provide 4-digit code.")
        else: st.error("Invalid phone format.")

    if st.session_state.otp_requested:
        otp = st.text_input("Enter Handshake OTP", type="password")
        if st.button("Verify & Grant Access"):
            if otp == "5291":
                with st.spinner("Decrypting Lifelong Record..."):
                    time.sleep(1.5)
                    st.session_state.access_granted = True
                    st.session_state.active_patient_cnic = "35202-7654321-1"
                    st.rerun()
            else: st.error("Incorrect OTP.")

def render_patient_dashboard():
    st.success(f"✅ CLINICAL ACCESS ENABLED: {st.session_state.active_patient_cnic}")
    if st.button("End Session"):
        st.session_state.access_granted = False
        st.session_state.otp_requested = False
        st.rerun()

    st.divider()
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.container(border=True):
            st.write("### 📈 Longitudinal Clinical Vitals")
            df = data_mock.vitals_history
            fig = px.line(df, x='Month', y=['HbA1c', 'Systolic BP'], title='Health Trajectory (12 Months)',
                         color_discrete_map={'HbA1c': '#8b0707', 'Systolic BP': '#ffcc00'})
            fig.update_layout(
                template="plotly_dark", 
                plot_bgcolor='rgba(0,0,0,0)', 
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=20, r=20, t=40, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.write("#### Detailed Clinical Archive")
        st.table(pd.DataFrame({
            "Date": ["12-Oct-2025", "05-Oct-2025", "15-Aug-2025"],
            "Event": ["Metformin titration", "Lipid Profile (Patient)", "Mayo Transfer"],
            "Note": ["HbA1c trending up", "High LDL", "Complete Sync"]
        }))

    with col2:
        with st.container(border=True):
            st.write('### <span class="pulse-dot"></span> VitalHash AI Insights', unsafe_allow_html=True)
            
            with st.popover("🛡️ Why High Risk?"):
                st.write("**XAI Logic:** Risk is flagged as **High** because the longitudinal data identifies a simultaneous increase in HbA1c (8.4%) and Systolic BP (148). This pattern historically correlates with a 65% higher risk of acute renal strain in the D-T2 segment.")
    
            st.error("**Risk Level: High (D-T2)**")
            st.info("**AI Analysis Snapshot:**\n- 15% surge in glucose detected\n- Hypertension correlate identified")
            
            st.write("#### 💬 Ask Records")
            st.chat_input("Chat with record summary...")
            
            st.divider()
            st.write("#### ✍️ Add Annotation")
            note = st.text_area("Add clinical finding to living record")
            if st.button("Commit to History"):
                st.toast("Note enriched. Collaborative timeline updated.")

def render_surveillance():
    with st.container(border=True):
        st.write("### 🌍 Regional Disease Surveillance (Real-Time)")
        st.write("Strategic health promotion & resource allocation HUD.")
    
    # Map focused on Gujranwala hotspots
    m = folium.Map(location=[32.1664, 74.1959], zoom_start=12)
    df = data_mock.disease_stats
    
    for i, row in df.iterrows():
        # Circle marker for hotspots
        radius = row['Dengue_Cases'] * 2
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=radius,
            popup=f"{row['region']}: {row['Dengue_Cases']} Dengue Cases",
            color='red' if row['Dengue_Cases'] > 20 else 'orange',
            fill=True,
            fill_opacity=0.4
        ).add_to(m)

    st_folium(m, width=1100, height=450)
    
    st.divider()
    st.write("#### 📊 Top Regional Trends")
    st.bar_chart(df.set_index('region')['Dengue_Cases'])
    st.write("##### 💡 Strategic Insight: City Center shows 4x higher risk for Dengue clusters.")
