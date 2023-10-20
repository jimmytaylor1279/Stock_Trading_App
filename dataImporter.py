import pandas as pd

class DataImporter:
    def __init__(self, symbol_utilities, api):
        self.symbol_utilities = symbol_utilities
        self.api = api  # Alpaca API object passed from Trader

    def fetch_data(self):
        """
        Fetch historical and real-time data for the most active stock symbols.
        """
        # Get the most active stock symbols directly
        most_active_symbols = self.symbol_utilities.fetch_most_active_symbols()

        # Fetch historical data
        historical_data = {}
        real_time_data = {}
        for symbol in most_active_symbols:
            # Fetch historical data for the past 30 days
            historical_data[symbol] = self.api.get_barset(symbol, 'day', limit=30).df[symbol]
            
            # Fetch real-time data (latest available)
            real_time_data[symbol] = self.api.get_latest_trade(symbol)

        return historical_data, real_time_data

    def fetch_latest_news(self):
        """
        Fetch the latest stock market news. (This can be implemented later)
        """
        pass
