from rich.prompt import Prompt
from utils.account import get_accounts

def create_new_transaction(console, account_names, state):
    """
    Prompt user for new transaction details and return as a dictionary.
    param console: Console - The Rich Console object to use for input/output
    param account_names: list - A list of account names to choose from
    return: dict - A dictionary containing the new transaction details
    """
    console.print("\n[bold green]Add Transaction[/bold green]")
    account_name = Prompt.ask("Select Account", choices=account_names)
    amount = float(Prompt.ask("Enter Amount"))
    description = Prompt.ask("Enter Description")

    subtract_from_balance(account_name, amount, state)

    transaction_details = {
        "account_name": account_name,
        "amount": amount,
        "description": description
    }

    console.print(f"[bold green]Transaction added to account '{account_name}' successfully![/bold green]\n")
    return transaction_details

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