import streamlit as st
import boto3
import pandas as pd
import pydeck as pdk
from datetime import datetime

st.set_page_config(page_title="SentriTrack Dashboard", layout="wide")

# Connect to AWS (Cape Town region)
dynamodb = boto3.resource('dynamodb', region_name='af-south-1')
table = dynamodb.Table('SentriTrackData')

# Fetch data
response = table.scan()
items = response.get('Items', [])

# Convert to DataFrame
df = pd.DataFrame(items)
if not df.empty:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['lat'] = df['lat'].astype(float)
    df['lon'] = df['lon'].astype(float)

    st.title("SentriTrack Realtime Dashboard (South Africa)")

    # Map
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/streets-v11",
        initial_view_state=pdk.ViewState(
            latitude=-33.9249,  # Cape Town
            longitude=18.4241,
            zoom=6,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=4000,
            ),
        ],
    ))

    # Table
    st.subheader("Device Logs")
    st.dataframe(df[['device_id', 'timestamp', 'lat', 'lon']].sort_values("timestamp", ascending=False))

else:
    st.warning("No data available yet from SentriTrack devices.")