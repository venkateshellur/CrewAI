using System;
using System.Windows;
using Gradio;

namespace TradingSimulation
{
    public class App
    {
        private static Account account;

        [STAThread]
        public static void Main(string[] args)
        {
            account = new Account("user1", 1000M); // Create account with an initial deposit

            var app = new GradioInterface();

            app.AddInput("Deposit Funds", "amount", DataType.Decimal);
            app.AddButton("Deposit", data => {
                try
                {
                    account.Deposit((decimal)data);
                    return $"Deposited: {data}, New Balance: {account.Balance}";
                }
                catch (Exception ex)
                {
                    return ex.Message;
                }
            });

            app.AddInput("Withdraw Funds", "amount", DataType.Decimal);
            app.AddButton("Withdraw", data => {
                try
                {
                    account.Withdraw((decimal)data);
                    return $"Withdrew: {data}, New Balance: {account.Balance}";
                }
                catch (Exception ex)
                {
                    return ex.Message;
                }
            });

            app.AddInput("Buy Shares", "symbol", DataType.String);
            app.AddInput("Buy Quantity", "quantity", DataType.Integer);
            app.AddButton("Buy", data => {
                try
                {
                    account.BuyShares((string)data[0], (int)data[1]);
                    return $"Bought {data[1]} shares of {data[0]}, New Balance: {account.Balance}";
                }
                catch (Exception ex)
                {
                    return ex.Message;
                }
            });

            app.AddInput("Sell Shares", "symbol", DataType.String);
            app.AddInput("Sell Quantity", "quantity", DataType.Integer);
            app.AddButton("Sell", data => {
                try
                {
                    account.SellShares((string)data[0], (int)data[1]);
                    return $"Sold {data[1]} shares of {data[0]}, New Balance: {account.Balance}";
                }
                catch (Exception ex)
                {
                    return ex.Message;
                }
            });

            app.AddButton("Portfolio Value", _ => $"Portfolio Value: {account.CalculatePortfolioValue()}");
            app.AddButton("Profit/Loss", _ => $"Profit/Loss: {account.CalculateProfitOrLoss()}");
            app.AddButton("Report Holdings", _ => {
                var holdings = account.ReportHoldings();
                string report = "Holdings:\n";
                foreach (var holding in holdings)
                {
                    report += $"{holding.Key}: {holding.Value}\n";
                }
                return report;
            });

            app.AddButton("List Transactions", _ => {
                var transactions = account.ListTransactions();
                string report = "Transactions:\n";
                foreach (var transaction in transactions)
                {
                    report += $"{transaction.TransactionType} of {transaction.Amount} on {transaction.TransactionDate}\n";
                }
                return report;
            });

            app.Start();
        }
    }
}