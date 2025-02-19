import string

def encode(input_text, shift):

    alphabet = list(string.ascii_lowercase)

    encoded_text = ""

    # Iterate through each character in the input_text

    for char in input_text.lower():

        if char in alphabet: 

            original_index = alphabet.index(char)  # Get the current position

            new_index = (original_index + shift) % 26  # Shift and wrap around

            encoded_text += alphabet[new_index]  # Append the encoded letter

        else:

            encoded_text += char  # If not a letter, stays unchanged

    return (alphabet, encoded_text)

 

def decode(input_text, shift):

    alphabet = list(string.ascii_lowercase)

    decoded_text = ""

    # Iterate through each character in the input_text

    for char in input_text.lower():

        if char in alphabet: 

            original_index = alphabet.index(char)  # Get the current position

            new_index = (original_index - shift) % 26  # Shift and wrap around

            decoded_text += alphabet[new_index]  # Append the encoded letter

        else:

            decoded_text += char  # If not a letter, stays unchanged

    return decoded_text

 

import datetime

class BankAccount:

    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):

        self.name = name

        self.ID = ID

        self.creation_date = creation_date if creation_date else datetime.date.today()

        self.balance = balance

 

        # Ensuring creation_date is not in the future

        if self.creation_date > datetime.date.today():

            raise Exception("Creation date cannot be in the future.")

 

    def deposit(self, amount):

        if amount <= 0:

            return

        

        self.balance += amount

        print(f"Deposit successful! New balance: ${self.balance}")

 

    def withdraw(self, amount):

        """Withdraws money from the account if possible."""

        if amount <= 0:

            raise ValueError("Withdrawal amount must be above 0.")

        if self.balance <=0:

            raise ValueError("Insufficient funds.")

       

        self.balance -= amount

        print(f"Withdrawal successful! New balance: ${self.balance}")

 

    def view_balance(self):

        """Displays the current account balance."""

        print(f"Current balance: ${self.balance}")

        return self.balance

 

class SavingsAccount(BankAccount):

    def withdraw(self, amount):

        """Allows withdrawal only if the account is older than 180 days and prevents overdrafts."""

        if amount > self.balance:

            raise Exception("Insufficient funds. Overdrafts are not permitted.")

       

        today = datetime.date.today()

        account_age = (today - self.creation_date).days

        if account_age < 180:

            raise Exception("No Withdrawals, only 180 days after account creation.")

        super().withdraw(amount)

        print(f"Withdrawal successful! New balance: ${self.balance}")

 

class CheckingAccount(BankAccount):

    def withdraw(self, amount):

        """Allows withdrawals and applies a $30 fee if overdrawing the account."""

        if amount <= 0:

            raise ValueError("Withdrawal amount must be Above 0.")

       

        self.balance -= amount

 

        # Apply overdraft fee if balance goes negative

        if self.balance < 0:

            print("Overdraft fee of $30 applied.")

            self.balance -= 30

            

        print(f"Withdrawal successful! New balance: ${self.balance}")