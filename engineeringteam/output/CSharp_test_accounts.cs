using NUnit.Framework; using TradingSimulation; using System; using System.Collections.Generic;

namespace TradingSimulationTests
{
    [TestFixture]
    public class AccountTests
    {
        private Account _account;

        [SetUp]
        public void Setup()
        {
            _account = new Account("12345", 1000m);
        }

        [Test]
        public void Deposit_ShouldIncreaseBalance_WhenValidAmount()
        {
            _account.Deposit(500m);
            Assert.AreEqual(1500m, _account.Balance);
        }

        [Test]
        public void Deposit_ShouldThrowException_WhenNegativeAmount()
        {
            Assert.Throws<ArgumentException>(() => _account.Deposit(-100m));
        }

        [Test]
        public void Withdraw_ShouldDecreaseBalance_WhenValidAmount()
        {
            _account.Withdraw(200m);
            Assert.AreEqual(800m, _account.Balance);
        }

        [Test]
        public void Withdraw_ShouldThrowException_WhenInsufficientFunds()
        {
            Assert.Throws<InvalidOperationException>(() => _account.Withdraw(2000m));
        }

        [Test]
        public void BuyShares_ShouldDecreaseBalanceAndIncreaseHoldings_WhenSufficientFunds()
        {
            _account.BuyShares("AAPL", 3);
            Assert.AreEqual(450.00m, _account.Balance);
            Assert.AreEqual(3, _account.Holdings["AAPL"]);
        }

        [Test]
        public void BuyShares_ShouldThrowException_WhenInsufficientFunds()
        {
            Assert.Throws<InvalidOperationException>(() => _account.BuyShares("AAPL", 10));
        }

        [Test]
        public void SellShares_ShouldIncreaseBalanceAndDecreaseHoldings_WhenSold()
        {
            _account.BuyShares("AAPL", 2);
            _account.SellShares("AAPL", 1);
            Assert.AreEqual(600.00m, _account.Balance);
            Assert.AreEqual(1, _account.Holdings["AAPL"]);
        }

        [Test]
        public void SellShares_ShouldThrowException_WhenNotEnoughShares()
        {
            _account.BuyShares("AAPL", 1);
            Assert.Throws<InvalidOperationException>(() => _account.SellShares("AAPL", 2));
        }

        [Test]
        public void CalculatePortfolioValue_ShouldReturnCorrectValue()
        {
            _account.BuyShares("AAPL", 1);
            decimal value = _account.CalculatePortfolioValue();
            Assert.AreEqual(600.00m, value);
        }

        [Test]
        public void ReportHoldings_ShouldReturnCurrentHoldings()
        {
            _account.BuyShares("AAPL", 2);
            var holdings = _account.ReportHoldings();
            Assert.AreEqual(2, holdings["AAPL"]);
        }

        [Test]
        public void ListTransactions_ShouldReturnAllTransactions()
        {
            _account.Deposit(500m);
            _account.Withdraw(200m);
            var transactions = _account.ListTransactions();
            Assert.AreEqual(2, transactions.Count);
        }
    }
}