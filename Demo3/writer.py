# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path


from rich.prompt import Prompt
from rich.console import Console

from ui.writer_layout import create_writer_layout, show_menu, get_new_account_details
from utils.account import add_new_account
from utils.transaction import add_new_transaction


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
        case "1":
            new_account = add_new_account(read_shared_state(), console)
            if new_account:
                write_shared_state(new_account)
            else:
                console.print("[red]Failed to add new account.[/red]")
        case "2":
            new_transaction = add_new_transaction(read_shared_state(), console)
            if new_transaction:
                write_shared_state(new_transaction)
            else:
                console.print("[red]Failed to add new transaction.[/red]")
        case "3":
            console.print("\n[yellow]Viewing Accounts! 👋[/yellow]\n")
        case "4":
            console.print("\n[yellow]Viewing Transactions! 👋[/yellow]\n")
        case "5":
            console.print("\n[yellow]Switching View! 👋[/yellow]\n")
        case "6":
            console.print("\n[yellow]Updating Content! 👋[/yellow]\n")
        case "7":
            console.print("\n[yellow]Showing Current State! 👋[/yellow]\n")
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