# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path


from rich.prompt import Prompt
from rich.console import Console

from ui.writer_layout import create_writer_layout, update_writer_layout, create_menu
from ui.account import new_account_prompt

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
    
def add_account():
   """
    Prompt user for new account details and add to shared state
   """
   new_account_details = new_account_prompt(console)

# Load existing state
   state = read_shared_state()

   state["accounts"] = new_account_details

   with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)



def show_choice(choice):
    """
    Handle the user's menu choice
    param choice: str - The user's menu choice
    return: int - 0 to exit, else None
    """
    if choice == "0":
        console.print("\n[yellow]Exiting Command Client. Goodbye! 👋[/yellow]\n")
        return 0
    elif choice == "1":
        console.print("\n[yellow]Switching View! 👋[/yellow]\n")
    elif choice == "2":
        console.print("\n[yellow]Updating Content! 👋[/yellow]\n")
    elif choice == "3":
        console.print("\n[yellow]Adding Transaction Data! 👋[/yellow]\n")
    elif choice == "4":
        add_account()
    elif choice == "5":
        console.print("\n[yellow]Showing Current State! 👋[/yellow]\n")

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
        create_menu(console)
        choice = Prompt.ask(
            "[green]Enter command[/green]",
            choices=["0", "1", "2", "3", "4", "5"]
        )
        result = show_choice(choice)

        if result == 0:
            break

        input("\nPress Enter to continue...")
     

if __name__ == "__main__":
    main()