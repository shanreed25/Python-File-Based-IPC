# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path

from rich.text import Text
from rich.prompt import Prompt
from rich.console import Console

console = Console()

SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

def read_shared_state():
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")
        return {
            "message": "Hello from writer process!",
        }
    
def update(new_message):
    state = read_shared_state()

    state["message"] = new_message

    with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)
    
    
    message_styled = Text("Updated message to:", style="bold green")
    message_value_styled = Text(new_message, style="bold yellow")
    print("\n" + "="*50)
    console.print(message_styled, message_value_styled)

def main():
    print("\n")
    print("\n" + "="*50)
    print("✍️  FILE-BASED IPC WRITER STARTED")
    print("Writing to: shared_state.json")
    print("Press Ctrl+C to stop the writer process.")
    print("=" * 50)
    while True:
        try:
            print("\n" + "="*50)
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