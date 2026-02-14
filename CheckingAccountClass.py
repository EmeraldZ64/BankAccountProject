import BankAccountClass

   

# define new class with parent class being BankAccount from BankAccountClass.py
class CheckingAccount(BankAccountClass.BankAccount):
    # TODO: the whole thing

    def __init__(self, account_number, routing_number, name, initial_balance=0, monthly_transfer_limit=5000):
        super().__init__(account_number, routing_number, name, initial_balance)
        
        self.__monthly_transfer_limit = monthly_transfer_limit
        self.__transfers_this_month = 0
        self.__transfer_count = 0
   
    # Transactions

    def transfer(self, amount, destination_account):
        if amount <= 0:
            print("Invalid transfer amount")
            return False
        if self.__transfers_this_month + amount > self.__monthly_transfer_limit:
            print(f"Transfer denied. Monthly limit of ${self.__monthly_transfer_limit} would be exceeded")
            return False
        
        if amount <= self.balance:
            self._balance -= amount
            destination_account.deposit(amount)
            
            self.__transfers_this_month += amount
            self.__transfer_count += 1
            
            print(f"Transferred ${amount:.2f} to {destination_account._name}")
            print(f"Monthly transfers so far: ${self.__transfers_this_month:.2f}")
            return True
        else: 
            print(f"Insufficient funds. Overdraft fee of ${self._overdraft_fee} would apply")
            return False

    def get_transfer_limit(self):
        return self.__monthly_transfer_limit
    
    def get_transfers_this_month(self):
        return self.__transfers_this_month
    
    def reset_monthly_transfers(self):
        self.__transfers_this_month = 0
        self.__transfer_count = 0
        print("Monthly transfer counter reset")

    def display_checking_info(self):
        print(f"Monthly Transfer Limit: ${self.__monthly_transfer_limit}")
        print(f"Transfers This Month: ${self.__transfers_this_month:.2f}")
        print(f"Transfer Count: {self.__transfer_count}")
    pass