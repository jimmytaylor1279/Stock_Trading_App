import alpaca_trade_api as tradeapi  # Import Alpaca API

class SymbolUtilities:
    def __init__(self, api):
        self.api = api  # Initialize Alpaca API object

    def fetch_most_active_symbols(self):
        assets = self.api.list_assets(status='active')
        tradable_assets = [asset for asset in assets if asset.tradable]
        symbols = [asset.symbol for asset in tradable_assets]
        
        # Fetch bars data for each symbol individually
        most_active_symbols = []
        for symbol in symbols:
            try:
                bars = self.api.get_bars(symbol, '1D', limit=1)
                if bars:
                    volume = bars[-1].v  # Get the volume of the last bar
                    most_active_symbols.append((symbol, volume))
            except Exception as e:
                print(f"Error fetching bars for {symbol}: {e}")
        
        # Sort by volume and take top 20
        most_active_symbols = sorted(most_active_symbols, key=lambda x: x[1], reverse=True)[:20]
        
        return [symbol for symbol, _ in most_active_symbols]

    def update_dropdown(self, symbols):
        with open("most_active_symbols.txt", "w") as f:
            for symbol in symbols:
                f.write(f"{symbol}\n")

if __name__ == "__main__":
    # Initialize Alpaca API
    api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets')

    symbol_utilities = SymbolUtilities(api)  # Pass the api object here
    most_active_symbols = symbol_utilities.fetch_most_active_symbols()
    symbol_utilities.update_dropdown(most_active_symbols)
