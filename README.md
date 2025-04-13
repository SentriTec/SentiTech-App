import streamlit as st
from datetime import datetime
import pytz

# Set South African timezone
sast = pytz.timezone("Africa/Johannesburg")
now = datetime.now(sast)

st.set_page_config(page_title="SentriTech Dashboard", layout="wide", page_icon="🔐")

# Sidebar navigation
st.sidebar.image("assets/sentritech-logo.png", use_column_width=True)
st.sidebar.title("SentriTech App")
selection = st.sidebar.radio("Navigate", ["🏠 SentriHome", "🚗 SentriDrive"])

# Show date/time
st.caption(f"📅 {now.strftime('%A, %d %B %Y – %H:%M')} (SAST)")

# Routing
if selection == "🏠 SentriHome":
    from Home import show_home
    show_home()
elif selection == "🚗 SentriDrive":
    from Drive import show_drive
    show_drive()

# Footer
st.markdown("---")
st.markdown("© 2025 SentriTech Solutions | Proudly South African 🇿🇦")
import streamlit as st

def show_home():
    st.title("🏠 SentriHome – Smart Home Control")
    st.subheader("Monitor and control your smart devices")

    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Living Room Lights", value=True)
        st.checkbox("Main Gate Lock")
    with col2:
        st.slider("Thermostat", 16, 30, 22)
        st.button("Activate Alarm")
import streamlit as st

def show_drive():
    st.title("🚗 SentriDrive – Vehicle Tracker")
    st.subheader("Real-time GPS vehicle tracking and alerts")

    st.map({
        "lat": [-33.918861],
        "lon": [18.423300]
    })

    st.success("Vehicle 1 is active and moving.")
streamlit
pytz

