# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:14:18 2023

@author: cy83r-3x71nc710n
"""

# A single run banking program: two starting balances, one operation,
# printed result, nothing stored. The flow now sits inside main() and
# the arithmetic sits in apply_operation(), so the money logic can be
# tested without scripting the prompts. The prompt order below is the
# order the README lists, and I kept it.

import math
import sys


def read_amount(prompt):
    # I exit here instead of returning a sentinel because every caller
    # needs a real number before it can do anything at all. Bad text,
    # a non-finite value, and closed input all exit 1 with one line;
    # the first version let EOFError escape as a traceback, which I
    # reproduced with an empty pipe before fixing it.
    try:
        value = float(input(prompt))
    except (ValueError, EOFError):
        print("Please enter a number.")
        sys.exit(1)
    if not math.isfinite(value):
        print("Please enter a number.")
        sys.exit(1)
    return value


def read_text(prompt):
    # Text answers get the same closed input treatment as amounts:
    # EOF is a user ending the run, not a crash.
    try:
        return str(input(prompt)).strip().lower()
    except EOFError:
        print("Input ended before the operation was chosen.")
        sys.exit(1)


def apply_operation(action, account, money, balance_checking, balance_saving):
    """Return (new_checking, new_saving) for one operation.

    Returns None when a withdraw or transfer exceeds the source
    balance. The account answer names the source for a transfer:
    c sends from checking into savings, s sends the other way.
    Taking the full balance is allowed and leaves 0.
    """
    if action in ("w", "withdraw"):
        if money > (balance_checking if account == "c" else balance_saving):
            return None
        if account == "c":
            return balance_checking - money, balance_saving
        return balance_checking, balance_saving - money
    if action in ("d", "deposit"):
        # A deposit is not limited by what is already in the account,
        # so it never reads the balance for a funds check.
        if account == "c":
            return balance_checking + money, balance_saving
        return balance_checking, balance_saving + money
    # transfer
    if money > (balance_checking if account == "c" else balance_saving):
        return None
    if account == "c":
        return balance_checking - money, balance_saving + money
    return balance_checking + money, balance_saving - money


def format_money(value):
    # Balances print to two places. The first version printed the raw
    # float, so a deposit of 0.2 onto 0.1 showed 0.30000000000000004;
    # for a money program that spelling is a bug worth fixing even
    # though nothing is stored between runs.
    return f"{value:.2f}"


def main():
    balance_checking = read_amount("\n What is the balance of your checking account? \n")
    balance_saving = read_amount("\n What is the balance of your savings account? \n")

    # Starting balances get the negativity check the amount already
    # had. A negative balance used to pass here, and then every
    # withdraw or transfer out of that account failed for a reason
    # the output never named.
    if balance_checking < 0 or balance_saving < 0:
        print("Balances must not be negative")
        return 1

    print("--------------------------------------")
    print("\n Your checking balance is equal to \n" + format_money(balance_checking))
    print("\n Your savings balance is equal to \n" + format_money(balance_saving))
    print("--------------------------------------")

    # I strip and lower both text answers in read_text. Every
    # comparison below is written against lower case with no spaces,
    # and that helper is the only thing that makes it safe. Before it
    # existed, typing a capital C for checking silently did nothing.
    withdraw_takeout = read_text("\n Would you like to withdraw your money, deposit or transfer your money w/d/t \n")
    account = read_text("\n Which account would you like to access checking or savings account? c/s \n")

    # I ask for the amount before I validate the action word. That
    # order is the prompt order the README lists, so I keep it even
    # though validating earlier would read better.
    money = read_amount("\n What amount of money would you like to withdraw, deposit, or transfer? \n")

    # Every rejected input in this program now exits 1. The first
    # version mixed 0 and 1 across its checks, so a caller checking
    # $? could not tell a refused operation from a finished one.
    if money < 0:
        print("The amount must not be negative")
        return 1
    if account not in ("c", "s"):
        print("Please choose c for checking or s for savings")
        return 1
    if withdraw_takeout not in ("w", "withdraw", "d", "deposit", "t", "transfer"):
        print("Please choose w, d, or t")
        return 1

    result = apply_operation(
        withdraw_takeout, account, money, balance_checking, balance_saving
    )
    if result is None:
        print("You do not have that amount of money")
        return 1
    new_checking, new_saving = result

    if withdraw_takeout in ("w", "withdraw"):
        print("\n You have a selected a withdraw \n")
        print("Doing a withdraw of: ", format_money(money))
        if account == "c":
            print("\n Doing a withdraw from checking account your new balance is: \n")
        else:
            print("\n Doing a withdraw from saving account your new balance is: \n")
        print(format_money(new_checking if account == "c" else new_saving))
    elif withdraw_takeout in ("d", "deposit"):
        print("\n You have a selected a deposit \n")
        print("Doing a deposit of: ", format_money(money))
        if account == "c":
            print("\n Doing a deposit into checking account your new balance is: \n")
        else:
            print("\n Doing a deposit into saving account your new balance is: \n")
        print(format_money(new_checking if account == "c" else new_saving))
    else:
        # A transfer prints both new balances because it is the one
        # operation where showing only one number could hide a
        # mistake.
        print("\n You have a selected a transfer \n")
        print("Doing a transfer of: ", format_money(money))
        if account == "c":
            print("\n Doing a transfer from checking account to your savings account your new balance is: \n")
            print("\n Your new checking balance amount is: \n")
            print(format_money(new_checking))
            print("\n Your new savings amount is: \n")
            print(format_money(new_saving))
        else:
            print("\n Doing a transfer from savings account to your checking account your new balance is: \n")
            print("\n Your new savings balance amount is: \n")
            print(format_money(new_saving))
            print("\n Your new checking amount is: \n")
            print(format_money(new_checking))
    return 0


if __name__ == "__main__":
    sys.exit(main())
