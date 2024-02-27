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
        current_directory = os.getcwd()     # To get the current working directory
        self.accounts_file = os.path.join(current_directory, "Accounts.txt")    #File to store account information

    def create_account(self):            # Function to create an account.
        allowed_special_characters = "!@#$%^&*()-_=+[]{};:'\"\\|,.<>/?`~"
        while True:     # Check for valid name
            self.account_holder = input("Please enter your full name: ").lower().strip()
            if len(self.account_holder) > 3 and self.account_holder.replace(" ", "").isalpha():
                break
            else:
                print("Please enter a valid full name with at least 3 characters.")
        while True:     # Check if password is valid
            self.password = input(f"Set a passcode (Special Characters allowed): ")
            if all(char.isalnum() or char in allowed_special_characters for char in self.password):
                break
            else:
                print("Invalid Password.")
        
        # Generate User ID
        user_id = self.generate_user_id(self.account_holder)

        # Save account information to file
        with open(self.accounts_file, "a") as file:
            file.write(f"{self.account_holder}, {user_id}, {self.password}, {self.account_balance}\n")
        
        print("Account created successfully!")
    
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
        while True:
            username = input("Enter your username(Full Name): ").lower()
            password = input("Enter your password: ")
            # Check if username and password match any account in the file
            with open(self.accounts_file, "r") as file:
                for line in file:
                    acc_holder, acc_password, _ = line.strip().split(",")
                    if username == acc_holder and password == acc_password:
                        print("Login successful!")
                        return True
                print("Invalid username or password. Please Try again.")
                return False

    def option_select(self):             # Option select function with 1, 2, 3 or x to quit
        while not self.logged_in:
            choice = input("Enter 1 to log in, 2 to create a new account, or x to quit: ")
            if choice == "1":
                self.login()
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
account.create_account()