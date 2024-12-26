from visualization import setup_ui, display_conversion_section
from exchange_rate import get_exchange_rates

def main():
    # Setup the UI (page title, layout, and styles)
    setup_ui()

    # Fetch the exchange rates
    exchange_rates = get_exchange_rates()

    if exchange_rates:
        # Display the conversion section
        display_conversion_section(exchange_rates)
    else:
        st.error("Unable to fetch the exchange rates. Please try again later.")

if __name__ == "__main__":
    main()
