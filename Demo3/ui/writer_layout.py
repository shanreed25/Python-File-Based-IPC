from ast import If
from rich.prompt import Prompt
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
    table.add_row("1", "Add New Account")
    table.add_row("2", "Add New Transaction")
    table.add_row("3", "Change View")
    # table.add_row("4", "View Accounts")
    # table.add_row("5", "View Transactions")
    # table.add_row("6", "Update Content")
    # table.add_row("7", "Show Current State")
    table.add_row("0", "Exit")
    
    return table

def show_menu(console):
    menu = create_menu()
    console.print(menu)

    choice = Prompt.ask(
            "[green]Enter command[/green]",
            choices=["0", "1", "2", "3"]
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