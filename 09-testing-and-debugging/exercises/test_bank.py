"""
⭐⭐ Exercise 3 – Test your Bank Account

1. Copy your bank.py from Module 08 into this folder.
2. Write tests using a fixture that creates a fresh account:

    @pytest.fixture
    def account():
        return BankAccount("Ada", 100)

Test at least:
  - the starting balance
  - deposit increases the balance
  - withdraw decreases the balance
  - withdrawing too much raises InsufficientFundsError, and the balance is unchanged
  - depositing a negative amount raises ValueError
  - history records each transaction
  - SavingsAccount.add_interest() adds the right amount (use pytest.approx)
"""
import pytest

# from bank import BankAccount, SavingsAccount, InsufficientFundsError

# TODO: write your fixture and tests 👇
