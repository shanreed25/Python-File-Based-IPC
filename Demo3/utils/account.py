from rich.prompt import Prompt

def create_new_account(console):
   """  
   Prompt user for new account details and return as a dictionary.
   param console: Console - The Rich Console object to use for input/output
   return: dict - A dictionary containing the new account details

   """
   console.print("\n[bold green]Add New Account[/bold green]")
    
   account_name = Prompt.ask("Enter Account Name: ")
   account_type = Prompt.ask("Enter Account Type (e.g., Savings, Checking): ")
   initial_balance = Prompt.ask("Enter Initial Balance: ")

   try:
        initial_balance = float(initial_balance)
   except ValueError:
        console.print("[red]Invalid balance amount. Please enter a numeric value.[/red]")
        return

       # Add new account to state
   new_account_details = {
        "name": account_name,
        "type": account_type,
        "balance": initial_balance
    }
    
   console.print(f"[bold green]Account '{account_name}' added successfully![/bold green]\n")
   return new_account_details

def get_accounts(state):
    """
    Get the list of accounts from the shared state
    return: list - A list of account dictionaries
    """
    accounts = state.get("accounts", [])
    return accounts

def get_account_names(accounts):
    """
    Get a list of account names from the shared state
    return: list - A list of account names
    """
    accounts_names = [account['name'] for account in accounts]

    return accounts_names
