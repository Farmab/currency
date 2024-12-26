import requests
import streamlit as st

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Global exchange rate API
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "IQD" in data["rates"]:
            return data["rates"]["IQD"]
        else:
            st.error("IQD rate not found in the API response.")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching the exchange rate: {e}")
        return None
