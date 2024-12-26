import streamlit as st

def setup_ui():
    # Set up Streamlit page configuration
    st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

    # Add custom CSS for styling
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
            border-radius: 5px;
            padding: 10px;
            border: none;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        h1 {
            font-size: 18px; /* Adjusted smaller font size */
            text-align: center;
            white-space: nowrap; /* Prevent title from wrapping */
            margin-bottom: 20px; /* Add spacing below the title */
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
