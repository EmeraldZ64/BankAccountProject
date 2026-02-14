import BankAccountClass

# define new class with parent class being BankAccount from BankAccountClass.py
class SavingsAccount(BankAccountClass.BankAccount):

    days_passed = 0
    APR = 0.04

    def __init__(self, name, balance, min_balance):
        super().__init__(name, balance, min_balance)

    # method to pass a number of days and gain interest
    def pass_days(self, number_of_days):
        self.days_passed += number_of_days

        # simple interest formula
        self.balance = self.balance * self.APR * (number_of_days / 365)

