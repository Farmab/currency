from visualization import setup_ui, display_conversion_section
from exchange_rate import get_exchange_rate
import streamlit as st

def main():
    # Setup the UI (page title, layout, and styles)
    setup_ui()

    # Fetch exchange rate
    usd_to_iqd_rate = get_exchange_rate()

    if usd_to_iqd_rate:
        # Display the conversion sections for USD ↔ IQD
        display_conversion_section(usd_to_iqd_rate)
    else:
        st.error("Unable to fetch the exchange rate. Please try again later.")

if __name__ == "__main__":
    main()
