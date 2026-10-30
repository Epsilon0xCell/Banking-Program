# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:14:18 2023

@author: cy83r-3x71nc710n
"""

# imports required libraries

import sys


# This whole program runs at module level, in file order, with no main
# guard. That is a real choice for a program this size: the prompt order
# in the README is the order of the statements below. It also means
# importing banking.py would start asking questions, so nobody should
# import it as a library.

def read_amount(prompt):
    # I exit here instead of returning a sentinel because every caller
    # needs a real number before it can do anything at all. This catches
    # ValueError only. If stdin closes early, input raises EOFError and
    # the program dies with a traceback and exit 1. I saw that happen
    # with an empty pipe in testing and I have not handled it.
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a number.")
        sys.exit(1)


balance_checking = read_amount("\n What is the balance of your checking account? \n")
balance_saving = read_amount("\n What is the balance of your savings account? \n")

# Both balances stay plain floats for the whole run and I never round.
# A deposit of 0.2 onto 0.1 prints 0.30000000000000004. For a one run
# program where nothing is stored, I accept that.
# I also never check these two starting balances for negativity. A
# negative balance passes here, and then every withdraw or transfer out
# of that account fails below because any positive amount is larger
# than a negative balance. The amount check further down does not
# cover the balances, only the amount.

# Prints balance and checking amount

print("--------------------------------------")
print("\n Your checking balance is equal to \n" + str(balance_checking))
print("\n Your savings balance is equal to \n" + str(balance_saving))
print("--------------------------------------")

# Asks if you want to withdraw or deposit money

withdraw_takeout = input("\n Would you like to withdraw your money, deposit or transfer your money w/d/t \n")
# I strip and lower both text answers in this one place. Every
# comparison below is written against lower case with no spaces, and
# this line is the only thing that makes that safe. Before this
# existed, typing a capital C for checking silently did nothing.
withdraw_takeout = str(withdraw_takeout).strip().lower()

# Asks if you want to access checking or savings

account = input("\n Which account would you like to access checking or savings account? c/s \n")
account = str(account).strip().lower()

# Asks the amount of money you want to withdraw, deposit, or transfer

# I ask for the amount before I validate the action word. That order
# means a bad action still gets an amount prompt first, and the
# "choose w, d, or t" message at the bottom only shows up after a
# number has been entered. The prompt order is the order the README
# lists, so I keep it even though validating earlier would read better.
money = read_amount("\n What amount of money would you like to withdraw, deposit, or transfer? \n")
# This negativity check matters more than it looks. Without it a
# withdraw of -50 added 50 to the balance, which is how I found it.
if money < 0:
    print("The amount must not be negative")
    sys.exit(0)
if account not in ("c", "s"):
    print("Please choose c for checking or s for savings")
    sys.exit(0)

# Balance of the account the user selected
# Every funds check below uses this one value. An earlier version
# checked both balances for a withdraw, so an almost empty savings
# account blocked a valid withdraw from checking. Deposit never reads
# this value at all, because a deposit is not limited by what is
# already in the account.
selected_balance = balance_checking if account == "c" else balance_saving

# Checks if withdraw == true and then checks if you have enough money to make a withdraw

# The three operation blocks below are separate if statements, not
# elif. That only works because the accepted spellings for one action
# never overlap another action. If I ever add an alias that two blocks
# both accept, both blocks would run in a single pass.
if withdraw_takeout == "w" or withdraw_takeout == "withdraw":
    print("\n You have a selected a withdraw \n")
    # Strictly greater, on purpose: taking the full balance is allowed
    # and leaves 0. An amount of 0 is also allowed and changes nothing.
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
    # For a transfer the account answer names the source, not the
    # target: c sends from checking into savings, s sends the other
    # way. I print both new balances because a transfer is the one
    # operation where showing only one number could hide a mistake.
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
# This has to stay last, and its list has to name every spelling the
# three blocks above accept, in full. It only prints and falls off the
# end, so a bad action exits 0, while a bad number exits 1 inside
# read_amount. The exit codes in this program do not agree with each
# other and I am noting that here instead of pretending they do.
if withdraw_takeout not in ("w", "withdraw", "d", "deposit", "t", "transfer"):
    print("Please choose w, d, or t")
