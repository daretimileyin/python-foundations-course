"""Mini-project solution – Bank Account System."""
from datetime import datetime


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self.history = []

    @property
    def balance(self):
        return self._balance

    def _record(self, kind, amount):
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.history.append(f"{stamp}  {kind:<10} {amount:>10.2f}  → {self._balance:>10.2f}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._record("deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(f"Balance is only {self._balance:.2f}")
        self._balance -= amount
        self._record("withdraw", amount)

    def __str__(self):
        return f"{self.owner}'s account: {self._balance:,.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._record("interest", interest)

    def __str__(self):
        return super().__str__() + f" (savings @ {self.interest_rate:.0%})"


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account):
        self.accounts[account.owner] = account

    def transfer(self, from_acc, to_acc, amount):
        from_acc.withdraw(amount)     # raises if not enough money, so nothing changes
        to_acc.deposit(amount)


def ask_amount():
    try:
        return float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return None


def main():
    owner = input("Your name: ")
    kind = input("Savings account? (y/n): ").lower()
    account = SavingsAccount(owner) if kind == "y" else BankAccount(owner)

    while True:
        print(f"\n🏦 {account}")
        print("1. Deposit\n2. Withdraw\n3. History\n4. Add interest (savings)\n5. Quit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                amount = ask_amount()
                if amount is not None:
                    account.deposit(amount)
            elif choice == "2":
                amount = ask_amount()
                if amount is not None:
                    account.withdraw(amount)
            elif choice == "3":
                print("\n".join(account.history) or "No transactions yet.")
            elif choice == "4":
                if isinstance(account, SavingsAccount):
                    account.add_interest()
                else:
                    print("Only savings accounts earn interest.")
            elif choice == "5":
                break
        except (ValueError, InsufficientFundsError) as error:
            print(f"❌ {error}")


if __name__ == "__main__":
    main()
