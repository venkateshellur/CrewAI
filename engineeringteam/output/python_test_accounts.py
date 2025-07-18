import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('test_user', 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.username, 'test_user')

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.balance, 700.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(800)
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_buy_shares(self):
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.portfolio['AAPL'], 2)
        self.assertEqual(self.account.balance, 700.0)
        with self.assertRaises(ValueError):
            self.account.buy_shares('TSLA', 2)
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', -1)

    def test_sell_shares(self):
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.portfolio['AAPL'], 1)
        self.assertEqual(self.account.balance, 850.0)
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 2)
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', -1)

    def test_total_portfolio_value(self):
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.total_portfolio_value(), 700.0 + 2 * get_share_price('AAPL'))

    def test_profit_loss(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.profit_loss(), -200)

    def test_transactions(self):
        self.account.deposit(500.0)
        self.account.withdraw(200.0)
        transactions = self.account.list_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertIn('Deposited: 500.0', transactions)
        self.assertIn('Withdrew: 200.0', transactions)

if __name__ == '__main__':
    unittest.main()