import streamlit as st
from datetime import datetime
import pytz

def setup_ui():
    # Set up Streamlit page configuration
    st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

    # Add custom CSS for styling, including clock design
    st.markdown(
        """
        <style>
        @font-face {
            font-family: 'Rabar_021';
            src: url('https://www.kurdfonts.com/storage/fonts/Rabar021/Rabar_021.woff') format('woff');
        }
        body {
            background-color: #00008b;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
            border: none;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .special-message {
            font-family: 'Rabar_021', sans-serif;
            font-size: 24px;
            color: gold;
            text-align: center;
            margin-top: 20px;
        }
        .clock {
            font-size: 24px;
            font-family: Arial, sans-serif;
            color: #fff;
            text-align: center;
            position: fixed;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display title and intro text
    st.markdown("<h1>💱 Currency Converter: USD ↔ IQD ↔ EUR ↔ GBP</h1>", unsafe_allow_html=True)
    st.markdown("This app helps you convert between **Iraqi Dinar (IQD)**, **US Dollar (USD)**, **Euro (EUR)**, and **British Pound (GBP)** based on the latest exchange rates.")

def display_conversion_section(exchange_rates):
    st.markdown("---")

    # Dropdowns for currency selection
    source_currency = st.selectbox("From:", list(exchange_rates.keys()))
    target_currency = st.selectbox("To:", list(exchange_rates.keys()))

    # Display the latest exchange rate between the selected currencies
    if source_currency != target_currency:
        exchange_rate = exchange_rates[target_currency] / exchange_rates[source_currency]
        st.info(f"💱 Latest Exchange Rate: **1 {source_currency} = {exchange_rate:.2f} {target_currency}**")
    else:
        st.warning("Please select two different currencies.")

    # Input field for amount
    amount = st.number_input("Enter Amount:", min_value=0.0, value=0.0, step=1.0, format="%.2f")

    # Single conversion button
    if st.button("Convert"):
        if source_currency == target_currency:
            st.warning("Please select two different currencies.")
        else:
            # Calculate the conversion
            converted_amount = amount * exchange_rates[target_currency] / exchange_rates[source_currency]
            st.success(f"{amount:,.2f} {source_currency} = {converted_amount:,.2f} {target_currency}")

            # Display special message for large IQD values
            if target_currency == "IQD" and converted_amount > 1_000_000_000:
                st.markdown('<div class="special-message">وەڵاهی دەوڵەمەندی</div>', unsafe_allow_html=True)

    # Dynamic clock for Erbil time
    erbil_time = datetime.now(pytz.timezone("Asia/Baghdad")).strftime("%H:%M:%S")
    st.markdown(f'<div class="clock">🕒 Erbil Time: {erbil_time}</div>', unsafe_allow_html=True)
    st.experimental_rerun()
