import gradio as gr
from accounts import Account

# Create an instance of Account for demonstration
demo_account = Account(username="DemoUser", initial_deposit=1000.00)

def deposit_funds(amount):
    demo_account.deposit(amount)
    return f"Deposited: {amount}, New Balance: {demo_account.balance}"

def withdraw_funds(amount):
    try:
        demo_account.withdraw(amount)
        return f"Withdrew: {amount}, New Balance: {demo_account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        demo_account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}, New Balance: {demo_account.balance}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        demo_account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}, New Balance: {demo_account.balance}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Total Portfolio Value: {demo_account.total_portfolio_value()}"

def holdings():
    return f"Current Holdings: {demo_account.get_holdings()}"

def profit_loss():
    return f"Profit/Loss: {demo_account.get_profit_loss()}"

def transactions():
    return demo_account.list_transactions()

# Setting up Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Trading Account Management Demo")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Deposit Funds")
            deposit_amount = gr.Number(label="Deposit Amount")
            deposit_button = gr.Button("Deposit")
            deposit_output = gr.Textbox()
            deposit_button.click(deposit_funds, inputs=deposit_amount, outputs=deposit_output)

        with gr.Column():
            gr.Markdown("### Withdraw Funds")
            withdraw_amount = gr.Number(label="Withdraw Amount")
            withdraw_button = gr.Button("Withdraw")
            withdraw_output = gr.Textbox()
            withdraw_button.click(withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Buy Shares")
            buy_symbol = gr.Textbox(label="Stock Symbol (e.g., AAPL)")
            buy_quantity = gr.Number(label="Quantity")
            buy_button = gr.Button("Buy Shares")
            buy_output = gr.Textbox()
            buy_button.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

        with gr.Column():
            gr.Markdown("### Sell Shares")
            sell_symbol = gr.Textbox(label="Stock Symbol (e.g., AAPL)")
            sell_quantity = gr.Number(label="Quantity")
            sell_button = gr.Button("Sell Shares")
            sell_output = gr.Textbox()
            sell_button.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Row():
        portfolio_button = gr.Button("Get Portfolio Value")
        portfolio_output = gr.Textbox()
        portfolio_button.click(portfolio_value, outputs=portfolio_output)

        holdings_button = gr.Button("Get Holdings")
        holdings_output = gr.Textbox()
        holdings_button.click(holdings, outputs=holdings_output)

        profit_loss_button = gr.Button("Get Profit/Loss")
        profit_loss_output = gr.Textbox()
        profit_loss_button.click(profit_loss, outputs=profit_loss_output)

    transactions_button = gr.Button("List Transactions")
    transactions_output = gr.Textbox()
    transactions_button.click(transactions, outputs=transactions_output)

# Launch the Gradio app
demo.launch()