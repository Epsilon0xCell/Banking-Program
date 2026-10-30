# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:14:18 2023

@author: cy83r-3x71nc710n
"""

# imports required libraries

import sys


# Grabs balance and checking amount

def read_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a number.")
        sys.exit(1)


balance_checking = read_amount("\n What is the balance of your checking account? \n")
balance_saving = read_amount("\n What is the balance of your savings account? \n")

# Prints balance and checking amount

print("--------------------------------------")
print("\n Your checking balance is equal to \n" + str(balance_checking))
print("\n Your savings balance is equal to \n" + str(balance_saving))
print("--------------------------------------")

# Asks if you want to withdraw or deposit money

withdraw_takeout = input("\n Would you like to withdraw your money, deposit or transfer your money w/d/t \n")
withdraw_takeout = str(withdraw_takeout).strip().lower()

# Asks if you want to access checking or savings

account = input("\n Which account would you like to access checking or savings account? c/s \n")
account = str(account).strip().lower()

# Asks the amount of money you want to withdraw, deposit, or transfer

money = read_amount("\n What amount of money would you like to withdraw, deposit, or transfer? \n")
if money < 0:
    print("The amount must not be negative")
    sys.exit(0)
if account not in ("c", "s"):
    print("Please choose c for checking or s for savings")
    sys.exit(0)

# Balance of the account the user selected
selected_balance = balance_checking if account == "c" else balance_saving

# Checks if withdraw == true and then checks if you have enough money to make a withdraw

if withdraw_takeout == "w" or withdraw_takeout == "withdraw":
    print("\n You have a selected a withdraw \n")
    if money > selected_balance:
        print("You do not have that amount of money")
        sys.exit(0)
    else:
        print("Doing a withdraw of: ", str(money))
    if account == "c":
        print("\n Doing a withdraw from checking account your new balance is: \n")
        print(balance_checking - money)
    if account == "s":
        print("\n Doing a withdraw from saving account your new balance is: \n")
        print(balance_saving - money)

# Makes a deposit (a deposit adds money, so there is no balance check)
if withdraw_takeout == "d" or withdraw_takeout == "deposit":
    print("\n You have a selected a deposit \n")
    print("Doing a deposit of: ", str(money))
    if account == "c":
        print("\n Doing a deposit into checking account your new balance is: \n")
        print(balance_checking + money)
    if account == "s":
        print("\n Doing a deposit into saving account your new balance is: \n")
        print(balance_saving + money)

# Checks if you have enough money to do the transfer and then transfers the selected money to the respective places selected.
if withdraw_takeout == "t" or withdraw_takeout == "transfer":
    print("\n You have a selected a transfer \n")
    if money > selected_balance:
        print("\n You do not have that amount of money \n")
        sys.exit(0)
    else:
        print("Doing a transfer of: ", str(money))
    if account == "c":
        print("\n Doing a transfer from checking account to your savings account your new balance is: \n")
        print("\n Your new checking balance amount is: \n")
        print(balance_checking - money)
        print("\n Your new savings amount is: \n")
        print(balance_saving + money)
    if account == "s":
        print("\n Doing a transfer from savings account to your checking account your new balance is: \n")
        print("\n Your new savings balance amount is: \n")
        print(balance_saving - money)
        print("\n Your new checking amount is: \n")
        print(balance_checking + money)

# Any other action choice is not recognised
if withdraw_takeout not in ("w", "withdraw", "d", "deposit", "t", "transfer"):
    print("Please choose w, d, or t")
