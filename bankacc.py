class Bank_Account:
    def __init__(self) -> None:
        self.account_balance = 0
        self.options = ["Deposit", "Withdrawal", "Check Balance"]
        self.account_holder = None
        self.password = None

    def create_account(self):            # Function to create an account.
        allowed_special_characters = "!@#$%^&*()-_=+[]{};:'\"\\|,.<>/?`~"
        while True:
            self.account_holder = input("Please enter your full name: ").lower()
            if self.account_holder.replace(" ", "").isalpha():
                break
            else:
                print("Please enter only letters.")
        while True:
            self.password = input(f"Set a passcode (Special Characters allowed): ")
            if all(char.isalnum() or char in allowed_special_characters for char in self.password):
                break
            else:
                print("Invalid Password.")
        
        print("Account created successfully!")

    def option_select(self):             # Option select function with 1, 2, 3 or x to quit
        while True:
            print("\nOptions: ")
            for index, option in enumerate(self.options, start=1):
                print(f"{index}. {option}")

            choice = input("Select an option 1. Deposit, 2. Withdrawal, 3. Check Balance or press x to quit: ")

            if choice == "x":
                break
            elif choice.isdigit() and 1 <= int(choice) <= 3:
                if choice == "1":
                    self.deposit()
                elif choice == "2":
                    self.withdrawal()
                elif choice == "3":
                    self.check_balance()
            else:
                print("Invalid option!")

    def deposit(self):                   # How the deposit is calculated with return message
        how_much_d = int(input("How much would you like to deposit: "))
        self.account_balance += how_much_d
        return ("Thank you for your deposit.")
    
    def withdrawal(self):               # How the withdrawal is calculated with return message + return message if not enough funds.
        how_much_w = int(input("How much would you like to withdraw: "))
        if self.account_balance >= how_much_w:
            self.account_balance -= how_much_w
            print("Here is your request."), 
            print(f"Your remaining funds are {self.account_balance}\n")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):           # Checking how much balance is in the account.
        print(f"Your account contains {self.account_balance}.")

account = Bank_Account()
account.option_select()
