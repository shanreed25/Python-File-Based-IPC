# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path

from rich.text import Text
from rich.prompt import Prompt
from rich.console import Console

from ui.layout import create_writer_layout, update_writer_layout

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
    
def update(new_message):
    """
    Update the shared state file with a new message
    param new_message: str - The new message to write to the shared state
    param layout: Layout - The current Rich Layout object
    """
    state = read_shared_state()

    state["data"] = {"message": new_message}

    with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)
    
    update_writer_layout(console, new_message)

def main():
    """
    Main function to run the writer process
    """

    create_writer_layout(console)

    while True:
        try:
            user_input = Prompt.ask("[bold yellow]Enter your message[/bold yellow]").strip()
            if not user_input:
                continue
            else:
                update(user_input)

        except KeyboardInterrupt:
            print("\n" + "="*50)
            console.print("\n[bold red]Writer stopped[/bold red]")
            break

if __name__ == "__main__":
    main()