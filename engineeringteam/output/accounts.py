# accounts.py

class Account:
    def __init__(self, account_id: str, initial_deposit: float):
        """
        Initializes a new account with an ID and an initial deposit.
        
        :param account_id: Unique identifier for the account
        :param initial_deposit: Initial amount of funds deposited into the account
        """
        
        self.account_id = account_id
        self.balance = initial_deposit
        self.holdings = {}  # Dictionary to store stock holdings {symbol: quantity}
        self.transactions = []  # List to log transactions
        self.initial_deposit = initial_deposit
        self.current_value = 0.0

    def deposit(self, amount: float):
        """
        Deposits funds into the account.
        
        :param amount: The amount to deposit
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount: float):
        """
        Withdraws funds from the account.
        
        :param amount: The amount to withdraw
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")

    def buy_shares(self, symbol: str, quantity: int):
        """
        Buys shares of a stock.
        
        :param symbol: The symbol of the stock to buy
        :param quantity: The number of shares to buy
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy these shares.")
        
        self.balance -= total_cost
        
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        
        self.transactions.append(f"Bought {quantity} shares of {symbol} at {share_price} each.")

    def sell_shares(self, symbol: str, quantity: int):
        """
        Sells shares of a stock.
        
        :param symbol: The symbol of the stock to sell
        :param quantity: The number of shares to sell
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")

        share_price = get_share_price(symbol)
        total_income = share_price * quantity

        self.holdings[symbol] -= quantity
        
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.balance += total_income
        self.transactions.append(f"Sold {quantity} shares of {symbol} at {share_price} each.")

    def calculate_portfolio_value(self) -> float:
        """
        Calculates the total value of the user's portfolio based on current share prices.
        
        :return: The total value of the portfolio
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        """
        Calculates the profit or loss from the initial deposit.
        
        :return: Profit or loss amount
        """
        self.current_value = self.calculate_portfolio_value()
        return self.current_value - self.initial_deposit

    def get_holdings(self) -> dict:
        """
        Returns the user's current stock holdings.
        
        :return: Dictionary of the user's holdings {symbol: quantity}
        """
        return self.holdings

    def get_profit_loss(self) -> float:
        """
        Returns the current profit or loss status.
        
        :return: Profit or loss amount
        """
        return self.calculate_profit_loss()

    def list_transactions(self) -> list:
        """
        Lists all transactions made by the user.
        
        :return: List of transactions
        """
        return self.transactions


def get_share_price(symbol: str) -> float:
    """
    Mock function to get share price for testing.
    
    :param symbol: The stock symbol
    :return: Current share price
    """
    prices = {
        "AAPL": 150.00,
        "TSLA": 800.00,
        "GOOGL": 2800.00
    }
    return prices.get(symbol, 0.0) # Returns 0.0 if symbol is not found