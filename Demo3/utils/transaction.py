"""Utility functions for handling transactions."""

from ui.writer_layout import get_new_transaction_details
# from utils.account import get_accounts, get_account_names

def add_new_transaction(state, console):
    """
    Add a transaction to an account in the shared state
    """

    # Get list of accounts
    accounts = state.get("accounts", [])

    # Ensure there are accounts to add transactions to
    if not accounts:
        return console.print("[red]No accounts available. Please add an account first.[/red]\n")
    
    # Get list of account names
    account_names = [account['name'] for account in accounts]

    # Get transaction details from user
    transaction_details = get_new_transaction_details(account_names, console)
    
    # Update state with new transaction
    account_name = transaction_details['account_name']

    # Extract transaction details
    amount = transaction_details['amount']
    description = transaction_details['description']

    # Update account balance
    subtract_from_balance(account_name, amount, state)

    # Add transaction to account
    for account in accounts:
        if account['name'] == account_name:
            account.setdefault('transactions', []).append({
                "amount": amount,
                "description": description
            })

    # Return updated state
    return state

def subtract_from_balance(account_name, amount, state):
   """
   Subtract the transaction amount from the account balance
   param account_name: str - The name of the account
   param amount: float - The transaction amount
   param state: dict - The current state dictionary
   """
    # Get list of accounts
   accounts = state.get("accounts", [])

   # Subtract amount from the specified account's balance
   for account in accounts:
       if account['name'] == account_name:
           account['balance'] -= amount


# Get a list of transactions for a given account
def get_transactions(account):
    """
    Get the list of transactions for a given account
    param account: dict - The account dictionary
    return: list - A list of transaction dictionaries
    """
    # Get transactions from account
    transactions = account.get("transactions", [])
    return transactions
