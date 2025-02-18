# Python Banking Program

## Overview
This is a simple command-line banking application that allows users to perform basic banking operations such as checking their balance, making deposits, and withdrawing funds. The program is interactive and validates user inputs to ensure a smooth banking experience.

## Features
- **Show Balance**: Displays the current account balance.
- **Deposit**: Allows users to deposit money, preventing negative deposits.
- **Withdraw**: Enables users to withdraw money, ensuring sufficient balance and preventing negative amounts.
- **Input Validation**: Handles invalid inputs and provides appropriate feedback.
- **Looped Execution**: Runs continuously until the user chooses to exit.

## Requirements
- Python 3.9

## How to Run
1. Ensure you have Python installed on your system.
2. Save the `banking.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory where `banking.py` is saved.
5. Run the script using the command:
   ```bash
   python banking.py
   ```
6. Follow the on-screen prompts to interact with the banking system.

## Functionality
### `show_balance(balance)`
Displays the user's current account balance.

### `deposit()`
- Prompts the user to enter a deposit amount.
- Prevents negative deposits.
- Returns the valid deposit amount.

### `withdraw(balance)`
- Prompts the user to enter a withdrawal amount.
- Checks if the balance is sufficient.
- Prevents negative withdrawals.
- Returns the valid withdrawal amount.

### `main()`
- Initializes the balance to zero.
- Runs a loop allowing users to choose banking operations.
- Calls appropriate functions based on user choice.
- Handles invalid inputs.
- Exits gracefully when the user chooses to exit.

## Example Usage
```
************
   Welcome to Enzu's Bank   
************
1.Show Balance
2.Deposit
3.Withdraw
4.Exit
************
Enter your choice (1-4): 2
************
Enter an amount to be deposited: 100
************
```

## Further improvements
- Add user authentication (PIN/password).
- Store balances persistently (e.g., using a SQL database or file storage).
- Implement a graphical user interface (GUI).


