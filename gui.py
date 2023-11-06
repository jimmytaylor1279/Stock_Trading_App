import tkinter as tk
from tkinter import ttk

class StockAppGUI:
    """
    Class to handle the GUI components of the Stock Trading App.
    """

    def __init__(self, trader, symbol_utilities, data_importer):
        """
        Initialize the GUI components.
        """
        self.trader = trader
        self.symbol_utilities = symbol_utilities
        self.data_importer = data_importer

        self.master = tk.Tk()
        self.master.title("Stock Trading App")
        
        # Label to display stock price
        self.stock_price_label = tk.Label(self.master, text="Stock Price: $0.00")
        self.stock_price_label.grid(row=0, column=1)
        
        # Label to display stock symbol
        self.stock_symbol_label = tk.Label(self.master, text="Stock Symbol:")
        self.stock_symbol_label.grid(row=1, column=0)
        
        # Dropdown for stock symbols
        self.stock_symbol_var = tk.StringVar()
        self.stock_symbol_dropdown = ttk.Combobox(self.master, textvariable=self.stock_symbol_var)
        self.stock_symbol_dropdown.grid(row=1, column=1)
        self.stock_symbol_dropdown.bind("<<ComboboxSelected>>", self.update_stock_price)
        
        # Button to update stock symbols
        self.update_symbols_button = tk.Button(self.master, text="Update Symbols", command=self.update_symbols)
        self.update_symbols_button.grid(row=2, column=0)
        
        # Button to start trading
        self.start_trading_button = tk.Button(self.master, text="Start Trading", command=self.start_trading)
        self.start_trading_button.grid(row=2, column=1)
        
        # Initialize dropdown values
        self.update_dropdown_values()
        
    def update_symbols(self):
        """
        Function to update trading symbols.
        """
        self.symbol_utilities.update_most_active_symbols()
        self.update_dropdown_values()
    
    def update_dropdown_values(self):
        """
        Function to update dropdown values.
        """
        symbols = self.symbol_utilities.get_symbols_from_file()
        self.stock_symbol_dropdown['values'] = symbols
        if symbols:
            self.stock_symbol_dropdown.current(0)
            self.update_stock_price(None)

    def update_stock_price(self, event):
        """
        Function to update the stock price label for the selected symbol.
        """
        selected_symbol = self.stock_symbol_var.get()
        if selected_symbol:
            # Fetch the latest price for the selected symbol
            price = self.trader.get_stock_price(selected_symbol)
            self.stock_price_label.config(text=f"Stock Price: ${price:.2f}")

    def start_trading(self):
        """
        Function to start trading the selected symbol.
        """
        selected_symbol = self.stock_symbol_var.get()
        if selected_symbol:
            # Fetch the 30-day history for the selected symbol
            historical_data = self.data_importer.fetch_historical_data(selected_symbol)
            # Start trading logic here
            self.trader.start_trading(selected_symbol, historical_data)

if __name__ == "__main__":
    # For testing purposes, you can create mock instances of Trader, SymbolUtilities, and DataImporter here
    # trader = Trader()
    # symbol_utilities = SymbolUtilities()
    # data_importer = DataImporter()
    # app = StockAppGUI(trader, symbol_utilities, data_importer)
    # app.master.mainloop()
    pass
