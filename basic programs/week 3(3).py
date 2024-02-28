class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def deposit(self,amount):
            if amount>0:
                self.balance+=amount
                print(f"Deposit of Rs.{amount} successful.")
            else:
                print("Invalind deposit amount.")
    def withdrawal(self,amount):
            if 0<amount<=self.balance:
                self.balance-=amount
                print(f"Withdrawal of Rs.{amount} successful.")
            else:
                print("Invalid withdrawal amount or insuffient funds.")
    def bank_fees(self):
        fees=0.05*self.balance
        self.balance-=fees
        print(f"Bank fees of Rs.{fees}applied.")
    def display(self):
        print(f"Account Number:{self.accountNumber}")
        print(f"Account Holder:{self.name}")
        print(f"Balance:Rs.{self.balance}")
        account1=BankAccount(accountNumber=123456,name="John Doe",balance=1000)
        account1.display()
        account1.deposit(500)
        account1.withdrawal(200)
        account1.bank_fees()
        account1.display()
