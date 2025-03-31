class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_interest_rate):
        # function for adjusting the interest rate
        self.interest_rate = new_interest_rate
        print(f"Interest rate adjusted to {self.interest_rate}%")

    def withdraw(self, amount):
        # function for withdrawing a specified amount
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
            print(f"Withdrew {amount}. New balance is {self.amount}")

    def deposit(self, amount):
        # function for depositing a specified amount into the account
        self.amount += amount
        print(f"Deposited {amount}. New balance is {self.amount}")

    def get_balance(self):
        # function for returning the current balance
        return self.amount

    def calculate_interest(self, days):
        # function for calculating the interest earned based on the number of days
        interest = (self.amount * self.interest_rate / 100) * (days / 365)
        return interest

    def __str__(self):
        #function for returning a string representation of the account
        return f"Account Name: {self.name}\nAccount Number: {self.account_number}\nBalance: {self.amount}\nInterest Rate: {self.interest_rate}%"

def test_bank_account():
    # Creating a BankAcct instance
    account = BankAcct("Cindy Velazquez-Santana", "123456789", 5000, 5)

    # Display account information
    print(account)

    # Deposit money
    account.deposit(500)
    print(account)

    # Withdraw money
    account.withdraw(200)
    print(account)

    # Adjust interest rate
    account.adjust_interest_rate(6)
    print(account)

    # Calculate interest
    interest = account.calculate_interest(30)
    print(f"Interest earned in 30 days: {interest:.2f}")

    # Check final balance
    print(f"Final Balance: {account.get_balance()}")

if __name__ == "__main__":
    test_bank_account()
