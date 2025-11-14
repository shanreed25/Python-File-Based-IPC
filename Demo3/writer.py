# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path


from rich.prompt import Prompt
from rich.console import Console

from ui.layout import create_writer_layout, update_writer_layout, create_menu

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
        return {
            "message": "Hello from writer process!",
        }
    
def update(new_message, layout):
    """
    Update the shared state file with a new message
    param new_message: str - The new message to write to the shared state
    param layout: Layout - The current Rich Layout object
    """
    state = read_shared_state()

    state["data"] = {"message": new_message}

    with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)
    
    
    updated_layout = update_writer_layout(layout, new_message)
    console.print(updated_layout)

def main():
    """
    Main function to run the writer process
    """

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

                
        if choice == "0":
            console.print("\n[yellow]Exiting Command Client. Goodbye! 👋[/yellow]\n")
            break
        elif choice == "1":
            console.print("\n[yellow]Switching View! 👋[/yellow]\n")
        elif choice == "2":
            console.print("\n[yellow]Updating Content! 👋[/yellow]\n")
        elif choice == "3":
            console.print("\n[yellow]Adding Transaction Data! 👋[/yellow]\n")
        elif choice == "4":
            console.print("\n[yellow]Clearing Data! 👋[/yellow]\n")
        elif choice == "5":
            console.print("\n[yellow]Showing Current State! 👋[/yellow]\n")
        input("\nPress Enter to continue...")
     

if __name__ == "__main__":
    main()