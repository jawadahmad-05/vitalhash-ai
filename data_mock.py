import pandas as pd

# --- Longitudinal Vitals Data (12 Months) ---
vitals_history = pd.DataFrame({
    'Month': ['Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25', 'Oct 25'],
    'HbA1c': [6.2, 6.3, 6.1, 6.5, 6.8, 7.1, 7.3, 7.5, 7.9, 8.1, 8.4, 8.6],
    'Systolic BP': [120, 118, 122, 125, 130, 135, 138, 142, 145, 148, 150, 155],
    'Weight (kg)': [78, 79, 79, 80, 82, 83, 85, 86, 88, 89, 90, 91]
})

# --- Localized Healthcare Facilities (Gujranwala / GC) ---
# Lat: 32.1664, Lon: 74.1959
care_network = pd.DataFrame({
    'name': [
        'Dr. Salman (Cardiologist)', 
        'Dr. Aisha (Diabetologist)', 
        'Dr. Hamza (GP)',
        'Fazal Din Pharmacy', 
        'Clinix Plus Pharmacy', 
        'D Watson Gujranwala'
    ],
    'type': ['Doctor', 'Doctor', 'Doctor', 'Pharmacy', 'Pharmacy', 'Pharmacy'],
    'specialty': ['Heart Health', 'Diabetes', 'General', 'Medicine/Store', 'Medicine/Store', 'Medicine/Store'],
    'lat': [32.1620, 32.1700, 32.1650, 32.1680, 32.1630, 32.1600],
    'lon': [74.1850, 74.2050, 74.1900, 74.2000, 74.2100, 74.1800]
})

# --- Regional Disease Surveillance (Hotspots) ---
disease_stats = pd.DataFrame({
    'region': ['Gujranwala Cantt', 'City Center', 'Aroop', 'Model Town', 'Nandipur'],
    'Dengue_Cases': [12, 45, 8, 22, 5],
    'Diabetic_Risk_Cluster': [85, 40, 30, 90, 20], # Scaling 0-100
    'lat': [32.1800, 32.1600, 32.1400, 32.2000, 32.2200],
    'lon': [74.2000, 74.1800, 74.1600, 74.2200, 74.2400]
})

# --- AI Health Planner Content ---
diet_plans = {
    "Diabetes Type 2": {
        "title": "Low Glycemic Index Diet",
        "title_ur": "شوگر کنٹرول ڈائٹ پلان",
        "items": [
            "Whole grains (Oats, Barley) / چکی کا آٹا",
            "Lean protein (Chicken, Fish) / مرغی اور مچھلی",
            "Leafy greens / سبز پتوں والی سبزیاں",
            "Avoid processed juices / مصنوعی جوس سے پرہیز"
        ]
    },
    "Hypertension": {
        "title": "DASH Diet (High BP Specialized)",
        "title_ur": "ہائی بلڈ پریشر ڈائٹ پلان",
        "items": [
            "Potassium-rich foods (Bananas, Spinach) / کیلے اور پالک",
            "Unsalted nuts / بغیر نمک والے میوے",
            "Garlic (1 clove daily) / لہسن کا استعمال",
            "Limit Salt to < 1 tsp / روزانہ ایک چمچ سے کم نمک"
        ]
    }
}

avoidance_tips = [
    {"en": "Avoid high-sodium snacks like chips and samosas.", "ur": "نمکین اشیاء جیسے چپس اور سموسوں سے پرہیز کریں۔"},
    {"en": "Stop sedentary activity; aim for a 20min evening walk.", "ur": "سست طرز زندگی چھوڑیں؛ شام کو 20 منٹ پیدل چلیں۔"},
    {"en": "Reduce white sugar and refined flour (Maida).", "ur": "سفید چینی اور میدہ کا استعمال کم کریں۔"}
]

daily_suggestions = [
    "Log your morning fasting glucose / نہار منہ شوگر چیک کریں",
    "Drink at least 3 liters of water / کم از کم 3 لیٹر پانی پییں",
    "Record any dizziness or evening BP spikes / شام کے بلڈ پریشر میں تبدیلی نوٹ کریں"
]
