"""
This program is a trading bot that uses the Alpaca API to trade stocks.
"""

# Importing required modules
import tkinter as tk
import logging  # For logging capabilities
from neuralNetwork import NeuralNetwork
from trader import Trader
from symbolUtilities import SymbolUtilities
from dataImporter import DataImporter
from gui import StockAppGUI  # Import the updated GUI class

class Main:
    """
    The Main class is the central class that connects and
    manages all the components of the trading bot.
    """

    def __init__(self):
        """
        Initialize all the components of the trading bot.
        """
        # Initialize logging capabilities
        logging.basicConfig(filename='tradebot.log', level=logging.INFO)

        self.trader = Trader()  # Initializing the Trader class first
        self.api = self.trader.api  # Get the Alpaca API object from Trader

        # Initialize SymbolUtilities with the Alpaca API object
        self.symbol_utilities = SymbolUtilities(self.api)

        # Initialize DataImporter with SymbolUtilities and the Alpaca API object
        self.data_importer = DataImporter(self.symbol_utilities, self.api)

        input_nodes = 5  # Open, High, Low, Close, Volume
        hidden_nodes = 3  # Average of input and output nodes
        output_nodes = 1  # Buy, Hold, or Sell

        # Initialize NeuralNetwork
        self.neural_network = NeuralNetwork(input_nodes, hidden_nodes, output_nodes)

        # Initialize StockAppGUI with Trader and SymbolUtilities
        self.gui = StockAppGUI(self.trader, self.symbol_utilities)

        # Initialize error handling
        self.initialize_error_handling()

        # Initialize backup mechanism
        self.initialize_backup()

    def initialize_error_handling(self):
        """
        Initialize error handling mechanisms.
        """
        try:
            pass
        except Exception as error:
            logging.error(f"An error occurred: {error}")

    def initialize_backup(self):
        """
        Initialize backup mechanisms.
        """
        try:
            pass
        except Exception as error:
            logging.error(f"Backup failed: {error}")

    def run(self):
        """
        Run the main process of the trading bot. This includes
        fetching the data, training the neural network,
        starting the trading process, and launching the GUI.
        """
        historical_data, real_time_data = self.data_importer.fetch_data()
        self.neural_network.train(historical_data)
        self.trader.start_trading(real_time_data)
        self.trader.place_trade('AAPL')  # Example of placing a trade for Apple stock

        # Implement trading logic based on previous trade outcome
        self.handle_trade_logic()

        # Implement trading limits
        self.set_trading_limits()

        # Implement notifications or alerts
        self.send_notifications()

        # Implement auto-update with latest stock market news
        self.update_market_news()

        # Implement multi-threading
        self.enable_multi_threading()

        # Implement data export to CSV or Excel
        self.export_data()

        # Implement 'Help' section in GUI
        self.add_help_section()

        # Implement GUI theme customization
        self.customize_theme()

        # Update stock symbols and dropdown
        self.update_stock_symbols()

        # Logging the start of the trading bot
        logging.info('Trading bot started.')

        self.gui.mainloop()

    def handle_trade_logic(self):
        prev_trade = self.trader.get_previous_trade()
        if prev_trade['status'] == 'gain':
            self.trader.set_trade_amount(0.05)
        elif prev_trade['status'] == 'loss':
            self.trader.set_trade_amount(prev_trade['loss_amount'] * 2)

    def set_trading_limits(self):
        self.trader.set_max_loss_limit(0.2)  # 20% of account balance

    def send_notifications(self):
        if self.trader.get_significant_price_change():
            self.gui.show_notification("Significant price change detected.")

    def update_market_news(self):
        latest_news = self.data_importer.fetch_latest_news()
        self.gui.update_news_section(latest_news)

    def enable_multi_threading(self):
        self.trader.enable_multi_threading()

    def export_data(self):
        self.trader.export_trading_history("trading_history.csv")

    def add_help_section(self):
        help_text = """
        Welcome to TradeBot. Here's how to use this application:
        1. Select a stock from the dropdown to monitor.
        2. Click on 'Start Trading' to begin.
        3. Use the 'Settings' menu to adjust trading parameters.
        """
        self.gui.add_help_section(help_text)

    def customize_theme(self):
        self.gui.set_theme("dark_mode")

    def update_stock_symbols(self):
        """
        Update the stock symbols using SymbolUtilities.
        """
        most_active_symbols = self.symbol_utilities.fetch_most_active_symbols()  # Assuming this is your updated method
        self.gui.update_dropdown_values(most_active_symbols)  # Update the dropdown with new values


if __name__ == "__main__":
    app = Main()
    app.run()
