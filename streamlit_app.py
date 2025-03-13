
import streamlit as st
import requests


# Function to get location details
def get_location_details(phone_number, api_key):
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Streamlit UI
st.title("📍 Phone Number Location Tracker")
phone_number = st.text_input("Enter Phone Number (with country code):")
api_key = kH0AfMzrUpmtHs18PXQY2giISbU3dYTI

if st.button("Track Location"):
    if phone_number:
        data = get_location_details(phone_number, api_key)
        if data and data.get("valid"):
            st.success("Location Found!")
            country = data.get("country_name", "N/A")
            location = f"{data.get('location', 'Unknown')}, {country}"
            carrier = data.get("carrier", "Unknown")
            lat, lon = data.get("latitude"), data.get("longitude")

            st.write(f"**Country:** {country}")
            st.write(f"**Location:** {location}")
            st.write(f"**Carrier:** {carrier}")
            
            if lat and lon:
                m = folium.Map(location=[lat, lon], zoom_start=10)
                folium.Marker([lat, lon], tooltip=location).add_to(m)
                folium_static(m)
        else:
            st.error("Invalid phone number or location not found.")
    else:
        st.warning("Please enter a valid phone number.")
