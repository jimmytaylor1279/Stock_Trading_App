import tkinter as tk
from tkinter import ttk
import subprocess
import os

class StockAppGUI:
    """
    Class to handle the GUI components of the Stock Trading App.
    """

    def __init__(self, trader, symbol_utilities):
        """
        Initialize the GUI components.
        """
        self.trader = trader
        self.symbol_utilities = symbol_utilities

        self.master = tk.Tk()
        self.master.title("Stock Trading App")
        
        # Label to display stock price
        self.stock_price_label = tk.Label(self.master, text="Stock Price:")
        self.stock_price_label.grid(row=0, column=0)
        
        # Label to display stock symbol
        self.stock_symbol_label = tk.Label(self.master, text="Stock Symbol:")
        self.stock_symbol_label.grid(row=1, column=0)
        
        # Dropdown for stock symbols
        self.stock_symbol_var = tk.StringVar()
        self.stock_symbol_dropdown = ttk.Combobox(self.master, textvariable=self.stock_symbol_var)
        self.stock_symbol_dropdown.grid(row=1, column=1)
        
        # Button to update stock symbols
        self.update_symbols_button = tk.Button(self.master, text="Update Symbols", command=self.update_symbols)
        self.update_symbols_button.grid(row=2, column=0)
        
        # Button to update dropdown values
        self.update_dropdown_button = tk.Button(self.master, text="Update Dropdown", command=self.update_dropdown_values)
        self.update_dropdown_button.grid(row=2, column=1)
        
        # Initialize dropdown values
        self.update_dropdown_values()
        
    def update_symbols(self):
        """
        Function to update trading symbols.
        """
        self.symbol_utilities.update_most_active_symbols()
        
        # Update the dropdown values after updating the symbols
        self.update_dropdown_values()
    
    def update_dropdown_values(self):
        """
        Function to update dropdown values.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
        file_path = os.path.join(script_dir, "active_stocks.txt")  # Join it with the filename

        with open(file_path, "r") as f:  # Use the full file path
            symbols = f.readlines()
        symbols = [symbol.strip() for symbol in symbols]  # Remove any trailing newlines
        self.stock_symbol_dropdown['values'] = symbols



if __name__ == "__main__":
    # For testing purposes, you can create mock instances of Trader and SymbolUtilities here
    # trader = Trader()
    # symbol_utilities = SymbolUtilities()
    # app = StockAppGUI(trader, symbol_utilities)
    pass
