"""Utility functions for handling transactions."""

from ui.writer_layout import get_new_transaction_details
from utils.account import get_accounts,get_account_names

def add_new_transaction(state, console):
    """
    Add a transaction to an account in the shared state
    """
    accounts = get_accounts(state)

    if not accounts:
        return console.print("[red]No accounts available. Please add an account first.[/red]\n")
    
    account_names = get_account_names(accounts)

    transaction_details = get_new_transaction_details(account_names, console)
    account_name = transaction_details['account_name']
    amount = transaction_details['amount']
    description = transaction_details['description']

    subtract_from_balance(account_name, amount, state)

    for account in accounts:
        if account['name'] == account_name:
            account.setdefault('transactions', []).append({
                "amount": amount,
                "description": description
            })
            break
    return state

def subtract_from_balance(account_name, amount, state):
   """
   Subtract the transaction amount from the account balance
   param account_name: str - The name of the account
   param amount: float - The transaction amount
   param state: dict - The current state dictionary
   """

   accounts = get_accounts(state)
   for account in accounts:
       if account['name'] == account_name:
           account['balance'] -= amount
           break

def get_transactions(account):
    """
    Get the list of transactions for a given account
    param account: dict - The account dictionary
    return: list - A list of transaction dictionaries
    """
    transactions = account.get("transactions", [])
    return transactions