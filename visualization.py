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
            background-color: red;
            color: white;
            border-radius: 5px;
            padding: 10px;
            border: none;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: darkred;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display title and intro text
    st.title("💱 Currency Converter: USD ↔ IQD")
    st.markdown("This app helps you easily convert between **USD** and **IQD** based on the latest exchange rates.")

def display_conversion_section(usd_to_iqd_rate):
    st.markdown("---")

    # Dropdown for currency selection
    currency = st.selectbox("Select Currency Type:", ["Dollar (USD)", "Dinar (IQD)"])

    # Input field for amount
    amount = st.number_input("Enter Amount:", min_value=0.0, value=0.0, step=1.0, format="%.2f")

    # Single conversion button
    if st.button("Convert"):
        if currency == "Dollar (USD)":
            # Convert USD to IQD
            converted_amount = amount * usd_to_iqd_rate
            st.success(f"{amount:,.2f} USD = {converted_amount:,.2f} IQD")
        else:
            # Convert IQD to USD
            converted_amount = amount / usd_to_iqd_rate
            st.success(f"{amount:,.2f} IQD = {converted_amount:,.2f} USD")

        # Special message for large conversions
        if converted_amount > 1_000_000_000 and currency == "Dollar (USD)":
            st.warning("زۆر دەوڵەمەندی غەزەب")
        st.write("**سوپاس**")

    st.markdown("---")
    st.markdown("**Tip:** Exchange rates are updated automatically based on the latest data from a reliable API.")
    st.markdown("---")
    st.write("**This app made by Farman GPT**")
