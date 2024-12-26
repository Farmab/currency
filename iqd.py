import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to fetch exchange rate from Google
def get_exchange_rate():
    url = "https://www.google.com/search?q=usd+to+iqd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        rate = soup.find("span", class_="DFlfde SwHCTb").text
        return float(rate.replace(",", ""))
    except Exception as e:
        st.error(f"Error fetching exchange rate: {e}")
        return None

# Streamlit App
st.title("Currency Converter: USD to IQD")
usd_to_iqd_rate = get_exchange_rate()

if usd_to_iqd_rate:
    st.write(f"Exchange Rate (USD to IQD): {usd_to_iqd_rate}")
    start = st.number_input("Enter the Start Amount (USD):", min_value=0.0, value=10.0)
    end = st.number_input("Enter the End Amount (USD):", min_value=start, value=100.0)
    step = st.number_input("Enter the Step:", min_value=1.0, value=10.0)

    st.write("### Conversion Results")
    for amount in range(int(start), int(end + 1), int(step)):
        usd_to_iqd = amount * usd_to_iqd_rate
        iqd_to_usd = amount / usd_to_iqd_rate
        st.write(f"{amount} USD = {usd_to_iqd:.2f} IQD | {amount} IQD = {iqd_to_usd:.2f} USD")
