from accounts import Account
import gradio as gr

# Initialize the account with a mock account ID and initial deposit
account = Account(account_id="1", initial_deposit=1000.0)

def create_account(initial_deposit):
    global account
    account = Account(account_id="1", initial_deposit=initial_deposit)
    return f"Account created with initial deposit: {initial_deposit}"

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited: {amount}. New balance: {account.balance}"

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew: {amount}. New balance: {account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}. New balance: {account.balance}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}. New balance: {account.balance}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Total Portfolio Value: {account.calculate_portfolio_value()}"

def profit_loss():
    return f"Profit/Loss: {account.calculate_profit_loss()}"

def report_holdings():
    return f"Holdings: {account.get_holdings()}"

def report_transactions():
    return f"Transactions: {account.list_transactions()}"

with gr.Interface(
    title="Trading Simulation Account Management",
    description="Simple UI to manage a trading account.",
    inputs=[
        gr.Number(label="Initial Deposit"),
        gr.Number(label="Deposit Amount"),
        gr.Number(label="Withdraw Amount"),
        gr.Textbox(label="Buy Symbol"),
        gr.Number(label="Buy Quantity"),
        gr.Textbox(label="Sell Symbol"),
        gr.Number(label="Sell Quantity"),
        gr.Button("Create Account"),
        gr.Button("Deposit Funds"),
        gr.Button("Withdraw Funds"),
        gr.Button("Buy Shares"),
        gr.Button("Sell Shares"),
        gr.Button("Check Portfolio Value"),
        gr.Button("Check Profit/Loss"),
        gr.Button("Report Holdings"),
        gr.Button("Report Transactions")
    ],
    outputs=[
        gr.Textbox(label="Output")
    ]
) as interface:
    interface.launch()