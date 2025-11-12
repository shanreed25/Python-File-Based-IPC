# ==============================================
# FILE BASED IPC DEMONSTRATION: READER PROCESS
# ==============================================
import json
from pathlib import Path
from time import sleep

from rich.text import Text
from rich.console import Console
from rich.layout import Layout

from ui.layout import display_reader_layout

console = Console()
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

def initialize_reader():
    """Initialize the state file"""
    initial_state = {
        "current_view": "reader",
        "content": "Welcome to FILE-BASED IPC READER!",
        "data": {}
    }
    with open(SHARED_STATE_FILE, 'w') as f:
        json.dump(initial_state, f)
    return initial_state

def read_state():
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")
        return None

def update_state(new_state):
    with open(SHARED_STATE_FILE, "w") as file:
        json.dump(new_state, file, indent=2)

        
            
def main():
    state = initialize_reader()
    try:
        while True:
            state = read_state()
            if state:
                display_reader_layout(console, state)
            
            sleep(5)

    except KeyboardInterrupt:
        console.print("[bold red]Reader stopped[/bold red]")

if __name__ == "__main__":
    main()