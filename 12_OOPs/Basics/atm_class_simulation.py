# Question: Create an ATM class with details, deposit, withdrawal, and balance display methods.

class ATM:
    bank_name = "SBI"
    location = "Kochi"

    def details(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        print(f"User account for '{name}' initialized with balance Rs. {balance}")

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Rs. {amount} deposited successfully.")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Transaction Failed: Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")

    def display(self):
        print(f"Account Holder: {self.name} | Current Balance: Rs. {self.balance}")

# ATM Simulation execution
user_account = ATM()
user_account.details("Arjun", 5000)
user_account.deposit(2000)
user_account.withdraw(2000)
user_account.display()
