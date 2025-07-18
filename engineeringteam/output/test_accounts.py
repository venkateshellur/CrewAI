import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('12345', 1000.0)

    def test_initialization(self):
        self.assertEqual(self.account.account_id, '12345')
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertIn('Deposited: 500', self.account.transactions)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800.0)
        self.assertIn('Withdrew: 200', self.account.transactions)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1200)

    def test_buy_shares(self):
        with unittest.mock.patch('accounts.get_share_price', return_value=100.0):
            self.account.buy_shares('AAPL', 5)
            self.assertEqual(self.account.holdings['AAPL'], 5)
            self.assertEqual(self.account.balance, 500.0)
            self.assertIn('Bought 5 shares of AAPL at 100.0 each.', self.account.transactions)

    def test_buy_shares_insufficient_funds(self):
        with unittest.mock.patch('accounts.get_share_price', return_value=2000.0):
            with self.assertRaises(ValueError):
                self.account.buy_shares('AAPL', 1)

    def test_sell_shares(self):
        with unittest.mock.patch('accounts.get_share_price', return_value=100.0):
            self.account.buy_shares('AAPL', 5)
            self.account.sell_shares('AAPL', 2)
            self.assertEqual(self.account.holdings['AAPL'], 3)
            self.assertEqual(self.account.balance, 700.0)
            self.assertIn('Sold 2 shares of AAPL at 100.0 each.', self.account.transactions)

    def test_sell_shares_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 1)

    def test_calculate_portfolio_value(self):
        with unittest.mock.patch('accounts.get_share_price', side_effect=lambda s: 100.0 if s == 'AAPL' else 0.0):
            self.account.buy_shares('AAPL', 5)
            self.assertEqual(self.account.calculate_portfolio_value(), 500.0)
            self.assertEqual(self.account.balance, 1000.0)

    def test_calculate_profit_loss(self):
        self.account.deposit(500)
        with unittest.mock.patch('accounts.get_share_price', return_value=150.0):
            self.account.buy_shares('AAPL', 5)
        self.assertEqual(self.account.calculate_profit_loss(), 250.0)

    def test_get_holdings(self):
        self.assertEqual(self.account.get_holdings(), {})
        with unittest.mock.patch('accounts.get_share_price', return_value=100.0):
            self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.get_holdings(), {'AAPL': 2})

    def test_list_transactions(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(len(self.account.list_transactions()), 2)

if __name__ == '__main__':
    unittest.main()