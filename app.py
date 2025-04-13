import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")  # Replace with your key file
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://YOUR_PROJECT.firebaseio.com/'  # Replace with your actual DB URL
    })

st.title("🔒 SentriDrive - Vehicle Monitor")

# Firebase DB Reference
ref = db.reference("sentridrive/vehicles")

# --- Input Form ---
st.subheader("🚗 Add Vehicle Info")
with st.form("vehicle_form"):
    plate = st.text_input("License Plate")
    location = st.text_input("Location")
    speed = st.number_input("Speed (km/h)", min_value=0)

    submitted = st.form_submit_button("Send to Firebase")
    if submitted:
        if plate and location:
            ref.push({
                "plate": plate,
                "location": location,
                "speed": speed
            })
            st.success("✅ Data saved successfully!")
        else:
            st.error("Please fill all required fields.")

# --- Display Firebase Data ---
st.subheader("📦 Vehicle Records")
vehicles = ref.get()

if vehicles:
    for key, data in vehicles.items():
        st.write(f"🚘 **{data['plate']}** | 📍 {data['location']} | 🚀 {data['speed']} km/h")
else:
    st.info("No vehicle data found yet.")



