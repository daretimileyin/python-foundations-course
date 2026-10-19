import pytest

from bank import BankAccount, InsufficientFundsError, SavingsAccount


@pytest.fixture
def account():
    return BankAccount("Ada", 100)


def test_starting_balance(account):
    assert account.balance == 100


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70


def test_withdraw_too_much_raises_and_keeps_balance(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500)
    assert account.balance == 100


@pytest.mark.parametrize("amount", [0, -10])
def test_invalid_deposit_raises(account, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)


def test_history_records_transactions(account):
    account.deposit(10)
    account.withdraw(5)
    assert len(account.history) == 2
    assert "deposit" in account.history[0]
    assert "withdraw" in account.history[1]


def test_savings_interest():
    savings = SavingsAccount("Grace", 1000, interest_rate=0.035)
    savings.add_interest()
    assert savings.balance == pytest.approx(1035)
