# 🩺 VitalHash AI — Secure Collaborative Healthcare Ecosystem

> A hackathon project (HSIL × GIFT University) reimagining the patient health record as a **living, AI-enriched, collaboratively verified** profile — with emergency-first design and bilingual (English / Roman Urdu) intelligence.

VitalHash AI is a **Streamlit** application that reimagines the patient health record as a living, AI-enriched, collaboratively verified profile.

## 🚀 Run the Streamlit App

```bash
# install dependencies
pip install -r requirements.txt

# launch
streamlit run app.py
```

Then open **http://localhost:8501**.

**Features**
- 🚨 Emergency SOS mode — instantly unlocks life-saving vitals for first responders.
- 👤 **Patient Portal**: Record Vault, longitudinal Health Trends, AI Health Planner (bilingual chat twin), interactive Care Map (Gujranwala), Digital Medical Passport (PDF), OTP-based access control.
- 👨‍⚕️ **Doctor Portal**: secure OTP "handshake", clinical dashboard, and a regional disease-surveillance HUD.
- 🤖 Mock AI twin responds in English & Roman Urdu.

> Demo OTP for the doctor handshake (mock): `5291`

---

## 📁 Project Structure

```
Hackathon/
├── app.py                 # Streamlit entry point
├── patient_view.py        # Patient portal UI/logic
├── doctor_view.py         # Doctor portal UI/logic
├── data_mock.py           # Mock longitudinal + geo health data
├── logic/
│   └── pdf_gen.py         # Digital medical passport (PDF) generator
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Tech

`streamlit` · `pandas` · `plotly` · `folium` · `streamlit-folium` · `fpdf2`

---
