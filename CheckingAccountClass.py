import BankAccountClass

class CheckingAccount(BankAccountClass.BankAccount):
    # TODO: the whole thing
    def __init__(self, name, balance, min_balance):
        super().__init__(name, balance, min_balance)

    def transfer(self, amount):
        if amount <= 0:
            print("Invalid transfer amount")
            return False
        if amount <= self.balance:
            self.balance -= amount

            print(f"Transferred ${amount:.2f}")

            return True
        else:
            print(f"Insufficient funds.")
            return False
    pass
