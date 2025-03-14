# Personal Account Management

## 📌 Description

This project is a personal bank account management system implemented using **Object-Oriented Programming (OOP)** in Python.

The project includes two classes:

- **Amount** – stores transaction details.
- **PersonalAccount** – manages the account, handles deposits, withdrawals, and transaction history.

## 🛠 Project Structure

- `personal_account.py` – main program code.
- `UML_PersonalAccount.png` – class diagram.
- `README.md` – project documentation.

## 📌 How to Run

1. Install Python (if not installed). Check the version with:
   ```bash
   python --version
   ```
2. Download the project files.
3. Run the code:
   ```bash
   python personal_account.py
   ```

## 📌 Features

- Create a bank account.
- Deposit money.
- Withdraw money (with balance validation).
- View transaction history.
- Check current balance.

## 📌 UML Diagram



## 📌 Example Usage

```python
# Creating an account
account = PersonalAccount(123456, "John Doe")

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(200)

# Checking current balance
print(account.get_balance())

# Printing transaction history
account.print_transaction_history()
```

## 📌 Author

**Eldiiar Almazbekov** – Student at Ala-too International University(MATDAIS23)
