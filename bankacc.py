import os
import sys
import random
import math
import logging
import csv
import datetime
import json
import string

class Bank_Account:
    def __init__(self) -> None:
        self.account_balance = 0
        self.options = ["Deposit", "Withdrawal", "Check Balance"]
        self.account_holder = None
        self.password = None
        self.logged_in = False
        save_directory = r"D:\Python\VS CODE PYTHON\Bank Prototype"
        self.accounts_file = os.path.join(save_directory, "Accounts.csv")    #File to store account information
        self.log_file = os.path.join(save_directory, "login.log")  # Log file for login activities

        # Configure logging to write to a file
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

    def create_account(self):            # Function to create an account.
        allowed_special_characters = "!@#$%^&*()-_=+[]{};:'\"\\|,.<>/?`~"
        while True:     # Check for valid name
            self.account_holder = input("Please enter your full name: ").lower().strip()
            if len(self.account_holder) > 3 and self.account_holder.replace(" ", "").isalpha():
                break
            else:
                print("Please enter a valid full name with at least 3 characters.")
        while True:     # Check if password is valid
            self.password = input("Set a passcode (Special Characters allowed): ")
            if all(char.isalnum() or char in allowed_special_characters for char in self.password):
                break
            else:
                print("Invalid Password.")
        
        # Generate User ID
        user_id = self.generate_user_id(self.account_holder)

        with open(self.accounts_file, "a") as file:
            if os.path.getsize(self.accounts_file) == 0:
                file.write("Name | User ID | Password | Balance\n")
            file.write(f"{self.account_holder} | {user_id} | {self.password} | {self.account_balance}\n")
        
        print("Account created successfully!")
        print(f"Your new User ID is {user_id}")
    
    def generate_user_id(self, account_holder):
        # Extract initials
        names = self.account_holder.split()
        first_initials = names[0][:2].upper()
        last_initials = names[-1][:2].upper()

        # Generate random number
        random_number = ''.join(random.choices(string.digits, k=4))
        # Combine initials and random number
        user_id = f"{first_initials}{last_initials}{random_number}"
        return user_id

    def login(self):        # Function for account login
        if not os.path.exists(self.accounts_file):
            print("No accounts found. Please create an account first or contact support.")
            return False
        
        print("Attempting to log in...")
        
        while True:
            username = input("Enter your User ID: ").lower()
            password = input("Enter your password: ")

            # Check if username and password match any account in the file
            with open(self.accounts_file, "r") as file:
                for line in file:
                    parts = line.strip().split(" | ")
                    if len(parts) == 4:
                        _, user_id, acc_password, _ = line.strip().split(" | ")
                        print("Checking:", user_id, acc_password)
                        if username == user_id.lower() and password == acc_password:
                            print("Login successful!")
                            self.user_id = user_id
                            self.account_balance = int(parts[3])
                            return True
                print("Invalid username or password. Please Try again.")
                return False
    
    def logout(self):
        pass

    def log_login_attempt(self, username, success):
        with open(self.log_file, "a") as log_file:
            log_file.write(f"Login Attepmt: Username={username}, Success={success}, Timestamp={datetime.datetime.now()}\n")

    def option_select(self):             # Option select function with 1, 2, 3 or x to quit
        while not self.logged_in:
            choice = input("Enter 1 to log in, 2 to create a new account, or x to quit: ")
            if choice == "1":
                if self.login():
                    break
            elif choice == "2":
                self.create_account()
            elif choice == "x":
                sys.exit()
            else:
                print("Invalid option.")

        while True:
            print("\nOptions: ")
            for index, option in enumerate(self.options, start=1):
                print(f"{index}. {option}")

            choice = input("Select an option 1. Deposit, 2. Withdrawal, 3. Check Balance or press x to quit: ")

            if choice == "x":
                sys.exit()
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
        print("Thank you for your deposit.")
        self.update_account_file()  # Update account_file with new balance
    
    def withdrawal(self):               # How the withdrawal is calculated with return message + return message if not enough funds.
        how_much_w = int(input("How much would you like to withdraw: "))
        if self.account_balance >= how_much_w:
            self.account_balance -= how_much_w
            print("Here is your request.") 
            print(f"Your remaining funds are {self.account_balance}€\n")
            self.update_account_file()  # Update new balance
        else:
            print("Insufficient funds!")
            print(f"You only have {self.account_balance}€ in your account.")
    
    def update_account_file(self):
        with open(self.accounts_file, "r") as file:
            lines = file.readlines()

        with open(self.accounts_file, "w") as file:
            for line in lines:
                parts = line.strip().split(" | ")
                if len(parts) == 4 and parts[1] == self.user_id:
                    line = f"{parts[0]} | {parts[1]} | {parts[2]} | {self.account_balance}\n"
                file.write(line)
    
    def check_balance(self):           # Checking how much balance is in the account.
        balance_found = False
        with open(self.accounts_file, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 4 and parts[1] == self.user_id:
                    balance = int(parts[3])
                    print(f"Your current balance is {balance}€.")
                    balance_found = True
                    break

        if not balance_found:
            print("Unable to fetch account balance. Please try again later.")

account = Bank_Account()
account.option_select()
account.create_account()