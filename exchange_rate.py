def get_exchange_rates():
    """
    Manually sets exchange rates for USD, IQD, EUR, and GBP.
    Returns a dictionary of rates.
    """
    rates = {
        "USD": 1.0,       # Base currency
        "IQD": 1510.0,    # 1 USD = 1510 IQD (manual rate)
        "EUR": 0.85,      # Example rate for Euro
        "GBP": 0.75,      # Example rate for British Pound
    }
    return rates
