"""Utility functions for handling transactions."""

from ui.writer_layout import get_new_transaction_details

def add_new_transaction(state, console):
    """
    Add a transaction to an account in the shared state
    param state: dict - The current state dictionary
    param console: Console - The Rich Console object to use for input/output
    return: dict - The updated state dictionary
    """
    accounts = state.get("accounts", [])

    if not accounts:
        return console.print("[red]No accounts available. Please add an account first.[/red]\n")
    
    account_names = [account['name'] for account in accounts]

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

    return state

def subtract_from_balance(account_name, amount, state):
   """
   Subtract the transaction amount from the account balance
   param account_name: str - The name of the account
   param amount: float - The transaction amount
   param state: dict - The current state dictionary
   """
   accounts = state.get("accounts", [])
   for account in accounts:
       if account['name'] == account_name:
           account['balance'] -= amount
