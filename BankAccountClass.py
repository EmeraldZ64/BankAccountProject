class BankAccount:

    bankName = "Fells Wargo"

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amt):
            self.balance += amt

    def withdraw(self, amt):
        if self.validate_balance(amt):
            self.balance -= amt

    def print_customer_info(self):
        print("Bank Name: ", self.bankName)
        print("Account Owner: ", self.name)
        print("Balance: ", self.balance)
        print("Minimum Balance: ", self.min_balance, "\n")

    def validate_balance(self, amt):
        if self.balance - amt < self.min_balance: # if subtracting amount leads to lower than minimum balance
            return False
        else:
            return True