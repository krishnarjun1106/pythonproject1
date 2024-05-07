class BankAccount:
    def _init_(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        if entered_pin == self.pin:
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN. Login failed.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs{amount} successful. Current balance: Rs{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs{amount} successful. Current balance: Rs{self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        else:
            print("Insufficient funds. Withdrawal failed.")


if __name__ == "_main_":

    account_number = "123456789"
    pin = "1234"
    initial_balance = 1000
    user_account = BankAccount(account_number, pin, initial_balance)


    entered_pin = input("Enter your PIN to log in: ")
    if user_account.login(entered_pin):
        act=int(input("Enter the action(1-deposit,2-Withdraw):" ))
        if act==1:
            amt = int(input("Enter the Amount: "))
            user_account.deposit(amt)
        elif act==2:
            amt2=int(input("Enter the Amount: "))
            user_account.withdraw(amt2)
        else:
            print("Invalid Input")