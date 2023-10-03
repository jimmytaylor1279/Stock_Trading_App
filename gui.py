import tkinter as tk
from tkinter import ttk
from symbolUtilities import update_symbols, get_default_symbol, get_stock_price


class StockAppGUI:
    """Class to create the GUI for the Stock Trading App."""
    
    def __init__(self, master):
        """Initialize the GUI components."""
        self.master = master
        self.master.title("Stock Trading App")
        self.master.geometry("400x400")

        self.label = tk.Label(
            self.master, text="Welcome to the Stock Trading App")
        self.label.pack()

        self.update_button = tk.Button(
            self.master, text="Update Symbols", command=self.update_symbols)
        self.update_button.pack()

        self.default_symbol = get_default_symbol()
        self.stock_price = get_stock_price(self.default_symbol)

        self.symbol_label = tk.Label(
            self.master, text=f"Current Symbol: {self.default_symbol}")
        self.symbol_label.pack()

        self.price_label = tk.Label(
            self.master, text=f"Stock Price: {self.stock_price}")
        self.price_label.pack()

        self.symbol_dropdown = ttk.Combobox(
            self.master, values=[], postcommand=self.update_dropdown)
        self.symbol_dropdown.pack()

        self.exit_button = tk.Button(
            self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack()

    def update_symbols(self):
        """Update the trading symbols and refresh the GUI."""
        update_symbols()
        self.default_symbol = get_default_symbol()
        self.stock_price = get_stock_price(self.default_symbol)
        self.symbol_label.config(text=f"Current Symbol: {self.default_symbol}")
        self.price_label.config(text=f"Stock Price: {self.stock_price}")

    def update_dropdown(self):
        """Update the dropdown values based on available symbols."""
        # Logic to update dropdown values
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = StockAppGUI(root)
    root.mainloop()
