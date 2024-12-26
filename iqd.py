import streamlit as st
import requests

# Function to fetch exchange rate from a global API
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Global exchange rate API
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "IQD" in data["rates"]:
            return data["rates"]["IQD"]
        else:
            st.error("IQD rate not found in API response.")
            return None
    except Exception as e:
        st.error(f"Error fetching exchange rate: {e}")
        return None

# Streamlit app
st.title("Currency Converter: USD ↔ IQD")

# Fetch the exchange rate
usd_to_iqd_rate = get_exchange_rate()

if usd_to_iqd_rate:
    st.write(f"**Exchange Rate:** 1 USD = {usd_to_iqd_rate} IQD")

    # Input fields for conversion
    col1, col2 = st.columns(2)

    with col1:
        usd_amount = st.number_input("Enter amount in USD:", min_value=0.0, value=0.0, step=1.0)
        if st.button("Convert USD to IQD"):
            iqd_result = usd_amount * usd_to_iqd_rate
            st.write(f"{usd_amount} USD = {iqd_result:.2f} IQD")

    with col2:
        iqd_amount = st.number_input("Enter amount in IQD:", min_value=0.0, value=0.0, step=1.0)
        if st.button("Convert IQD to USD"):
            usd_result = iqd_amount / usd_to_iqd_rate
            st.write(f"{iqd_amount} IQD = {usd_result:.2f} USD")
