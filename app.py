import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase-key.json")  # Path to your key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOUR_PROJECT_ID.firebaseio.com/'  # Replace with your actual DB URL
})


    # Table
    st.subheader("Device Logs")
    st.dataframe(df[['device_id', 'timestamp', 'lat', 'lon']].sort_values("timestamp", ascending=False))

else:
    st.warning("No data available yet from SentriTrack devices.")
