# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path


from rich.prompt import Prompt
from rich.console import Console

from ui.writer_layout import create_writer_layout, show_menu, choose_account
from utils.account import add_new_account
from utils.transaction import add_new_transaction, get_transactions


console = Console()

SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

def read_shared_state():
    """
    Read the shared state from the JSON file.
    return: dict - The current state dictionary
    """
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")

def write_shared_state(state):
    """
    Write the shared state to the JSON file.
    param state: dict - The state dictionary to write
    """
    with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)

def change_current_view(new_view):
    """
    Change the current view in the shared state.
    param new_view: str - The new view to set
    """
    state = read_shared_state()
    if state:
        state["current_view"] = new_view
        write_shared_state(state)
    

def handle_menu__choice(choice):
    """
    Handle the user's menu choice
    param choice: str - The user's menu choice
    return: int - 0 to exit, else None
    """
    match choice:
        case "0":
            console.print("\n[yellow]Exiting Command Client. Goodbye! 👋[/yellow]\n")
            return 0
        case "1":# View Summary
            console.print("\n[yellow]Viewing Summary! 👋[/yellow]\n")
            change_current_view("SUMMARY")
        case "2":# Add New Account
            new_account = add_new_account(read_shared_state(), console)
            if new_account:
                write_shared_state(new_account)
            else:
                console.print("[red]Failed to add new account.[/red]")
        case "3":# Add New Transaction
            new_transaction = add_new_transaction(read_shared_state(), console)
            if new_transaction:
                write_shared_state(new_transaction)
            else:
                console.print("[red]Failed to add new transaction.[/red]")
        case "4":# View Accounts
            console.print("\n[yellow]Viewing Accounts! 👋[/yellow]\n")
            change_current_view("ACCOUNTS")
            
        case "5":# View Account Transactions
            console.print("\n[yellow]Viewing Transactions! 👋[/yellow]\n")
            state = read_shared_state()
            accounts = state.get("accounts", [])
            account = choose_account(accounts, console)
            transactions = get_transactions(account)
            console.print(f"\n[yellow]Transactions for account '{account['name']}':[/yellow]")
            if transactions:
                for idx, transaction in enumerate(transactions, start=1):
                    console.print(f"{idx}. Amount: {transaction['amount']}, Description: {transaction['description']}")
            else:
                console.print("[red]No transactions available for this account.[/red]")
        case _:
            console.print("[red]❌Invalid choice. Please try again.[/red]")

def main():
    """
    Main function to run the writer process

    """
    create_writer_layout(console)
        # Prompt the user to ensure the reader.py is running
    console.print("[cyan]Command Client Started![/cyan]")
    console.print("[yellow]Make sure interface_server.py is running in another terminal[/yellow]\n")
    input("Press Enter to continue...")


    while True:
        
        choice = show_menu(console)
        result = handle_menu__choice(choice)

        if result == 0:
            break

        input("\nPress Enter to continue...")
     

if __name__ == "__main__":
    main()