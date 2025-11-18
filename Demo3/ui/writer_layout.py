from ast import If
from rich.prompt import Prompt
from rich.text import Text
from rich.table import Table
from rich import box

from ui.common_layouts import create_header, create_footer

#=============================================
# WRITER LAYOUT FUNCTIONS
#=============================================
def create_writer_layout(console):
    """
    Creates the base layout for the writer process
    param console: Console - The Rich Console object to use for output
    """

    header_text = "📝 FILE-BASED IPC WRITER STARTED 📝"
    color = "cyan"
    footer_text = "Writing to: shared_state.json | Press Ctrl+C to stop the writer process."
    console.print(create_header(header_text, color))
    console.print(create_footer(footer_text))

def update_writer_layout(console, new_message):
    """
    Update the writer's layout with a new message
    param console: Console - The Rich Console object to use for output
    param new_message: str - The new message to display in the header
    """
    console.clear()
    header_text = "📝 Writer Updated State To: " + new_message
    color = "yellow"
    console.print(create_header(header_text, color))

def create_menu():

    table = Table(title="Available Commands", box=box.SIMPLE_HEAVY)

    table.add_column("Command", style="green")
    table.add_column("Description")
    table.add_row("1", "View Summary")
    table.add_row("2", "Add New Account")
    table.add_row("3", "Add New Transaction")
    table.add_row("4", "View Accounts")
    table.add_row("5", "View Transactions")
    # table.add_row("6", "Update Content")
    # table.add_row("7", "Show Current State")
    table.add_row("0", "Exit")
    
    return table

def show_menu(console):
    menu = create_menu()
    console.print(menu)

    choice = Prompt.ask(
            "[green]Enter command[/green]",
            choices=["0", "1", "2", "3", "4"]
        )
    
    return choice

def get_new_account_details(console):
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

def get_new_transaction_details(account_names, console):
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

    transaction_details = {
        "account_name": account_name,
        "amount": amount,
        "description": description
    }

    console.print(f"[bold green]Transaction added to account '{account_name}' successfully![/bold green]\n")
    return transaction_details


def choose_account(accounts, console):
    """
    Choose an account from a list of accounts
    param account: dict - The account dictionary
    param console: Console - The Rich Console object to use for output
    """
    account_names = [account['name'] for account in accounts]
    account_name = Prompt.ask("Select Account", choices=account_names)

    #=======================================================================================
    # Generator Expression:
        # Iterates through each account to find the matching account name
        # filtered to only include accounts where the name key matches account_name
        # Yields matching account dictionaries
        # next(...) is a iterator function that retrieves the first item from the generator
            # Stops immediately after finding the first match (efficient!)
            # None - This is the default value:
                # If no matching account is found, next() returns None instead of raising a StopIteration exception
    #=======================================================================================
    # Finds and returns the first account dictionary where account['name'] equals account_name. If no match is found, it returns None.
    account = next((acc for acc in accounts if acc['name'] == account_name), None)


    console.print(f"\n[bold blue]Selected Account: {account_name}[/bold blue]")
    return account







def choose_view(console):
    """
    Choose a view from available views
    param console: Console - The Rich Console object to use for output
    return: str - The selected view name
    """
    views = ["SUMMARY", "ACCOUNTS", "TRANSACTIONS"]
    view = Prompt.ask("Select View", choices=views)
    console.print(f"\n[bold blue]Selected View: {view}[/bold blue]")
    return view