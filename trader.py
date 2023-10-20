import alpaca_trade_api as tradeapi
import os

class Trader:
    def __init__(self):
        self.api_key = os.environ.get('APCA_API_KEY_ID')
        self.api_secret = os.environ.get('APCA_API_SECRET_KEY')
        self.base_url = "https://paper-api.alpaca.markets"  # Use paper trading URL

        self.api = tradeapi.REST(self.api_key, self.api_secret, self.base_url, api_version='v2')

        # Fetch account information
        account_info = self.api.get_account()
        
        if account_info.status == 'ACTIVE':
            self.account_balance = float(account_info.cash)
        else:
            raise Exception("Account is not active. Please check your Alpaca account.")

# Initialize the Trader class
try:
    trader = Trader()
    print(f"Account balance: {trader.account_balance}")
except Exception as error:
    print(error)
