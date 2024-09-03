# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:14:18 2023

@author: cy83r-3x71nc710n
"""

# imports required libraries

import sys


# Grabs balance and checking amount

balance_checking = input("\n What is the balance of your checking account? \n")
balance_checking = float(balance_checking)
balance_saving = input("\n What is the balance of your savings account? \n")
balance_saving = float(balance_saving)

# Prints balance and checking amount

print("--------------------------------------")
print("\n Your checking balance is equal to \n" + str(balance_saving))
print("\n Your savings balance is equal to \n" + str(balance_checking))
print("--------------------------------------")

# Asks if you want to withdraw or deposit money

withdraw_takeout = input("\n Would you like to withdraw your money, deposit or transfer your money w/d/t \n")
withdraw_takeout = str(withdraw_takeout)

# Asks if you want to access checking or savings

account = input("\n Which account would you like to access checking or savings account? c/s \n")
account = str(account)

# Asks the amount of money you want to withdraw, deposit, or transfer

money = input("\n What amount of money would you like to withdraw, deposit, or transfer? \n")
money = float(money)

# Checks if withdraw == true and then checks if you have enough money to make a withdraw

if withdraw_takeout == "w" or withdraw_takeout == "W" or withdraw_takeout == "withdraw" or withdraw_takeout == "Withdraw":
    print("\n You have a selected a withdraw \n")
    if money > balance_checking or money > balance_saving:
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

# Checks if you have enough money to make a deposit and then makes a deposit if true
if withdraw_takeout == "d" or withdraw_takeout == "D" or withdraw_takeout == "deposit" or withdraw_takeout == "Deposit":
    print("\n You have a selected a deposit \n")
    if money > balance_checking or money > balance_saving:
        print("\n You do not have that amount of money \n")
        sys.exit(0)
    else:
        print("Doing a deposit of: ", str(money))
    if account == "c":
        print("\n Doing a withdraw from checking account your new balance is: \n")
        print(balance_checking - money)
    if account == "s":
        print("\n Doing a withdraw from saving account your new balance is: \n")
        print(balance_saving - money)

# Checks if you have enough money to do the transfer and then transfers the selected money to the respective places selected.
if withdraw_takeout == "t" or withdraw_takeout == "T" or withdraw_takeout == "transfer" or withdraw_takeout == "Transfer":
    print("\n You have a selected a transfer \n")
    if money > balance_checking or money > balance_saving:
        print("\n You do not have that amount of money \n")
        sys.exit(0)
    else:
        print("Doing a transfer of: ", str(money))
    if account == "c":
        print("\n Doing a transfer from checking account to your savings account your new balance is: \n")
        print("\n Your new balance amount is: \n")
        print(balance_checking - money)
        print("\n Your new checking amount is: \n")
        print(balance_saving + money)
    if account == "s":
        print("\n Doing a transfer from checking account to your savings account your new balance is: \n")
        print("\n Your new savings balance amount is: \n")
        print(balance_checking - money)
        print("\n Your new checking amount is: \n")
        print(balance_checking + money)
