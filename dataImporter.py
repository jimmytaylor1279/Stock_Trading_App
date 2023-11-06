import pandas as pd
import os

class DataImporter:
    def __init__(self, symbol_utilities, api):
        self.symbol_utilities = symbol_utilities
        self.api = api  # Alpaca API object passed from Trader

    def fetch_data_for_selected_symbol(self, selected_symbol):
        """
        Fetch historical and real-time data for the selected stock symbol.
        """
        # Fetch historical data for the past 30 days
        historical_data = self.api.get_barset(selected_symbol, 'day', limit=30).df[selected_symbol]
        
        # Fetch real-time data (latest available)
        real_time_data = self.api.get_latest_trade(selected_symbol)

        return historical_data, real_time_data

    def fetch_latest_news(self):
        """
        Fetch the latest stock market news. (This can be implemented later)
        """
        pass
