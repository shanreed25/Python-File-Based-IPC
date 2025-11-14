# ==============================================
# FILE BASED IPC DEMONSTRATION: READER PROCESS
# ==============================================
import json
from pathlib import Path
from time import sleep

from rich.text import Text
from rich.console import Console

console = Console()
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

def initialize_reader():
    if not SHARED_STATE_FILE.exists():
        initial_state = {
            "message": "This will be updated by the writer process. Waiting for writer..."
        }
        with open(SHARED_STATE_FILE, 'w') as f:
            json.dump(initial_state, f, indent=2)

def read_state():
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")
        return None
    
def display_state(state):
    print("="*50)
    print("📖 CURRENT STATE FROM SHARED FILE")
    print("="*50)

    for key, value in state.items():
        key_styled = Text(key, style="bold green")
        value_styled = Text(value, style="bold yellow")
        console.print("  ", key_styled, ": ", value_styled, "\n")

def main():
    print("\n")
    print("\n" + "="*50)
    print("🔄 FILE-BASED IPC READER STARTED")
    print("Monitoring: shared_state.json")
    print("Press Ctrl+C to stop the reader process.")

    initialize_reader()

    try:
        while True:
            state = read_state()
            if state:
                display_state(state)
            
            sleep(5)

    except KeyboardInterrupt:
        console.print("[bold red]Reader stopped[/bold red]")

if __name__ == "__main__":
    main()