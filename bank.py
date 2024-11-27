class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def withdraw(self, amnt):
        if self.balance >= amnt:
            self.balance = amnt
        else:
            print("Insufficient balance")   

    def deposit(self, amnt):
        if amnt > 0 :
            self.__balance += amnt
        else:
            print ("u cannot deposit it ")

    def get_balance(self):
        print(f"{self.__balance}") 


ac = BankAccount(50000)
ac.deposit(10000)

# print(ac.__balance)
ac.get_balance()


# print(dir(ac))

print(ac._BankAccount__balance)

# __ = private
# _ = protected

