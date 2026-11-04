<p align="center"><img src="intro-banner.png" alt="Banking-Program introduction" width="800"></p>

<p align="center"><img src="logo.png" alt="Banking-Program logo" width="200"></p>

# Banking-Program

**The Little Ledger**
_A tiny clay bank in sage and brass, where coins roll from one vault to the other and the balance scale stays level at the center._

A small interactive banking program in Python. It works with a checking account and a savings account for a single run: you enter both starting balances, choose one operation and one account, enter an amount, and the program prints the resulting balance. Nothing is saved between runs.


![Banking-Program](assets/banner.png)

![The Little Ledger, animated clay bank scene](assets-scene.svg)

![Minor separator](sep-light.svg)

## Contents

- [Requirements](#requirements)
- [How to run](#how-to-run)
- [What it asks, in order](#what-it-asks-in-order)
- [What each operation does](#what-each-operation-does)
- [Files](#files)
- [License](#license)

## Requirements

Python 3. The program uses only the standard library (`math` and `sys`), so there is nothing to install.

![Major separator](sep-heavy.svg)

![Minor separator](sep-light.svg)

## How to run

```
python3 banking.py
```

![Major separator](sep-heavy.svg)

![Minor separator](sep-light.svg)

## What it asks, in order

1. The balance of your checking account (a number).
2. The balance of your savings account (a number).
3. Whether you want to withdraw, deposit, or transfer: `w`, `d`, or `t` (the full words `withdraw`, `deposit`, and `transfer` also work, in any case).
4. Which account to use: `c` for checking or `s` for savings (any case).
5. The amount of money for the operation (a number, not negative).

The program first prints both balances back, with checking shown as checking and savings shown as savings.

![Major separator](sep-heavy.svg)

![Minor separator](sep-light.svg)

## What each operation does

<!-- deco -->
> **Watch order, chalked on the slate:** amounts larger than the source balance are refused with the words chalked in the section below, and every fault leaves by status 1.
<!-- /deco -->

- Withdraw (`w`): subtracts the amount from the selected account and prints its new balance. If the amount is more than the selected account holds, it prints "You do not have that amount of money" and exits. Only the selected account is checked.
- Deposit (`d`): adds the amount to the selected account and prints its new balance. A deposit has no upper limit based on the current balances.
- Transfer (`t`): moves the amount out of the selected account and into the other one, and prints both new balances. Choosing `c` transfers from checking to savings; choosing `s` transfers from savings to checking. If the amount is more than the source account holds, it prints "You do not have that amount of money" and exits.

Non-numeric input for a balance or amount, a non-finite value such as `inf`, or closed input (EOF) prints "Please enter a number." and exits with status 1 instead of showing a traceback. An account choice other than `c` or `s`, an action choice other than `w`, `d`, or `t`, a negative amount, a negative starting balance, and an amount larger than the source balance are each reported with a short message and exit with status 1. Balances print to two decimal places. Tests: `python3 -m unittest` covers the operation math and scripted runs.

Example inputs and outputs:

```
Checking balance 100, savings balance 1000, then w, c, 50
prints a new checking balance of 50.00

Checking balance 100, savings balance 1000, then d, c, 50
prints a new checking balance of 150.00

Checking balance 100, savings balance 1000, then t, s, 50
prints a new savings balance of 950.00 and a new checking balance of 150.00
```

![Major separator](sep-heavy.svg)

![Minor separator](sep-light.svg)

## Files

- `banking.py`: the program.
- `Flowchart.pdf`: a flowchart for the program.
- `assets/logo.png` and `assets/banner.png`: project branding.

![Major separator](sep-heavy.svg)

![Minor separator](sep-light.svg)

## License

GPL-3.0; see `LICENSE`.
