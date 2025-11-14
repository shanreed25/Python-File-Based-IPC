def new_account_prompt(console):
   """  
   Prompt user for new account details and return as a dictionary.
   param console: Console - The Rich Console object to use for input/output
   return: dict - A dictionary containing the new account details

   """
   console.print("\n[bold green]Add New Account[/bold green]")
    
   account_name = console.input("Enter Account Name: ")
   account_type = console.input("Enter Account Type (e.g., Savings, Checking): ")
   initial_balance = console.input("Enter Initial Balance: ")

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

    
