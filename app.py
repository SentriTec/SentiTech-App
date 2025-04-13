
import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import datetime

# Initialize Firebase
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sentritech-app-default-rtdb.firebaseio.com/'
})

st.title("SentriDrive - Vehicle Tracking Dashboard")
st.subheader("Device Logs")

# Input form for vehicle data
with st.form("vehicle_form"):
    plate = st.text_input("Vehicle Plate Number")
    location = st.text_input("Current Location")
    speed = st.number_input("Speed (km/h)", min_value=0, max_value=300, step=1)
    submitted = st.form_submit_button("Send to Firebase")

if submitted and plate and location:
    timestamp = datetime.datetime.now().isoformat()
    data = {
        "plate": plate,
        "location": location,
        "speed": speed,
        "timestamp": timestamp
    }
    ref = db.reference("sentridrive/vehicles")
    ref.push(data)
    st.success(f"Data for vehicle {plate} sent successfully!")
    # Fill out the form (plate, location, speed) and click Send to Firebase

# Display latest vehicle entries
st.subheader("Latest Vehicle Entries")
vehicles_ref = db.reference("sentridrive/vehicles")
vehicles = vehicles_ref.get()

if vehicles:
    for key, value in reversed(list(vehicles.items())[-5:]):
        st.write(f"🚗 {value['plate']} | 📍 {value['location']} | 💨 {value['speed']} km/h | 🕒 {value['timestamp']}")
else:
    st.write("No data available.")
