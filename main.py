from exchange_rate import get_exchange_rates
from visualization import setup_ui, display_conversion_section

def main():
    setup_ui()
    exchange_rates = get_exchange_rates()
    if exchange_rates:
        display_conversion_section(exchange_rates)
    else:
        st.error("Unable to fetch exchange rates.")

if __name__ == "__main__":
    main()
