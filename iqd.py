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
            st.error("IQD rate not found in the API response.")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching the exchange rate: {e}")
        return None

# Streamlit app
st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

# Add custom CSS for background color
st.markdown(
    """
    <style>
    body {
        background-color: #00008b;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💱 Currency Converter: USD ↔ IQD")
st.markdown("This app helps you easily convert between **USD** and **IQD** based on the latest exchange rates.")

# Fetch the exchange rate
usd_to_iqd_rate = get_exchange_rate()

if usd_to_iqd_rate:
    st.markdown(f"### 📈 Current Exchange Rate: **1 USD = {usd_to_iqd_rate:,.2f} IQD**")

    # Add some spacing
    st.markdown("---")

    # Input fields for conversion with improved layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Convert USD to IQD")
        usd_amount = st.number_input("Enter amount in USD:", min_value=0.0, value=0.0, step=1.0, format="%.2f")
        if st.button("Convert to IQD"):
            iqd_result = usd_amount * usd_to_iqd_rate
            st.success(f"{usd_amount:,.2f} USD = {iqd_result:,.2f} IQD")
            if iqd_result > 1_000_000_000:
                st.warning("زۆر دەوڵەمەندی غەزەب")
            st.write("**سوپاس**")

    with col2:
        st.subheader("Convert IQD to USD")
        iqd_amount = st.number_input("Enter amount in IQD:", min_value=0.0, value=0.0, step=1.0, format="%.2f")
        if st.button("Convert to USD"):
            usd_result = iqd_amount / usd_to_iqd_rate
            st.success(f"{iqd_amount:,.2f} IQD = {usd_result:,.2f} USD")
            st.write("**سوپاس**")

    # Footer section
    st.markdown("---")
    st.markdown(
        "**Tip:** Exchange rates are updated automatically based on the latest data from a reliable API. For accurate conversions, ensure your input values are correct.")

    # Attribution
    st.markdown("---")
    st.write("**This app made by Farman GPT**")

else:
    st.error("Unable to fetch the exchange rate. Please try again later.")
