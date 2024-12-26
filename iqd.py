import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch exchange rate from Google
def get_exchange_rate():
    url = "https://www.google.com/search?q=usd+to+iqd"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rate_element = soup.find("span", class_="DFlfde SwHCTb")
        if rate_element:
            rate = rate_element.text
            return float(rate.replace(",", ""))
        else:
            st.error("Exchange rate element not found on the page.")
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
