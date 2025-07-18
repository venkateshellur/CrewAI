// Module: accounts.cs
using System;
using System.Collections.Generic;

public class Account
{
    private string accountId;
    private double balance;
    private Dictionary<string, int> holdings; // Dictionary to store stock symbol and respective quantity
    private List<Transaction> transactions;   // List to store transaction history

    public Account(string accountId)
    {
        this.accountId = accountId;
        this.balance = 0.0;
        this.holdings = new Dictionary<string, int>();
        this.transactions = new List<Transaction>();
    }

    public string AccountId
    {
        get { return accountId; }
    }

    public double Balance
    {
        get { return balance; }
    }

    public void Deposit(double amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Deposit amount must be positive.");
        }
        balance += amount;
        transactions.Add(new Transaction(DateTime.Now, $"Deposit: {amount}"));
    }

    public void Withdraw(double amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Withdrawal amount must be positive.");
        }
        if (balance - amount < 0)
        {
            throw new InvalidOperationException("Insufficient funds for withdrawal.");
        }
        balance -= amount;
        transactions.Add(new Transaction(DateTime.Now, $"Withdrawal: {amount}"));
    }

    public void BuyShares(string symbol, int quantity)
    {
        double sharePrice = GetSharePrice(symbol);
        double totalCost = sharePrice * quantity;

        if (totalCost > balance)
        {
            throw new InvalidOperationException("Insufficient funds to buy shares.");
        }

        if (holdings.ContainsKey(symbol))
        {
            holdings[symbol] += quantity;
        }
        else
        {
            holdings[symbol] = quantity;
        }

        balance -= totalCost;
        transactions.Add(new Transaction(DateTime.Now, $"Bought {quantity} shares of {symbol} at {sharePrice} each."));
    }

    public void SellShares(string symbol, int quantity)
    {
        if (!holdings.ContainsKey(symbol) || holdings[symbol] < quantity)
        {
            throw new InvalidOperationException("Not enough shares to sell.");
        }

        double sharePrice = GetSharePrice(symbol);
        double totalRevenue = sharePrice * quantity;

        holdings[symbol] -= quantity;
        if (holdings[symbol] == 0)
        {
            holdings.Remove(symbol);
        }

        balance += totalRevenue;
        transactions.Add(new Transaction(DateTime.Now, $"Sold {quantity} shares of {symbol} at {sharePrice} each."));
    }

    public double CalculatePortfolioValue()
    {
        double totalValue = balance;
        foreach (var holding in holdings)
        {
            totalValue += GetSharePrice(holding.Key) * holding.Value;
        }
        return totalValue;
    }

    public double CalculateProfitLoss(double initialDeposit)
    {
        return CalculatePortfolioValue() - initialDeposit;
    }

    public Dictionary<string, int> GetHoldings()
    {
        return new Dictionary<string, int>(holdings); // Return a copy to avoid modification
    }

    public double GetProfitLoss()
    {
        return CalculateProfitLoss(balance); // Assuming initial deposit equals current balance for simplicity
    }

    public List<Transaction> GetTransactions()
    {
        return new List<Transaction>(transactions); // Return a copy to avoid modification
    }

    private double GetSharePrice(string symbol)
    {
        // For testing purposes, we return fixed prices
        switch (symbol)
        {
            case "AAPL":
                return 150.0;
            case "TSLA":
                return 700.0;
            case "GOOGL":
                return 2800.0;
            default:
                throw new ArgumentException("Unknown stock symbol.");
        }
    }
}

public class Transaction
{
    public DateTime Timestamp { get; }
    public string Description { get; }

    public Transaction(DateTime timestamp, string description)
    {
        Timestamp = timestamp;
        Description = description;
    }
}