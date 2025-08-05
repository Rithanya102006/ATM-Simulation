

class ATM:
    def __init__(self):
        self.users = {
            "12345678": {"pin": "1234", "balance": 5000},
            "87654321": {"pin": "4321", "balance": 3000}
        }
        self.current_user = None

    def authenticate_user(self):
        print("Welcome to the ATM!")
        card_number = input("Enter your card number: ")
        pin = input("Enter your PIN: ")

        user = self.users.get(card_number)
        if user and user["pin"] == pin:
            print("Authentication successful!")
            self.current_user = card_number
            return True
        else:
            print("Authentication failed. Try again.")
            return False

    def show_menu(self):
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        print(f"Your current balance is ₹{balance}")

    def deposit_money(self):
        amount = float(input("Enter amount to deposit: ₹"))
        self.users[self.current_user]["balance"] += amount
        print(f"₹{amount} deposited successfully!")

    def withdraw_money(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        balance = self.users[self.current_user]["balance"]
        if amount > balance:
            print("Insufficient funds!")
        else:
            self.users[self.current_user]["balance"] -= amount
            print(f"₹{amount} withdrawn successfully!")

    def run(self):
        if not self.authenticate_user():
            return

        while True:
            self.show_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
