# ==============================================
# FILE BASED IPC DEMONSTRATION: READER PROCESS
# ==============================================
import json
from pathlib import Path
from time import sleep

from rich.console import Console
from rich.live import Live

from ui.reader_layout import create_reader_layout, switch_view_content

console = Console()
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"



#===================================================
# Initialize
#===================================================
def initialize_state():
    """
    Initialize the state file with default values
    This function is called if file does not exist in the load_state()
    return: dict - The initial state dictionary
    """
    initial_state = {
        "current_view": "SUMMARY",
        "accounts": []
    }
    with open(SHARED_STATE_FILE, 'w') as f:
        json.dump(initial_state, f)
    return initial_state

#===================================================
# Load State
#===================================================
def load_state():
    """
    Load current state from file if file does not exist, 
    initialize it with default values using initialize_state()
    return: dict - The current state dictionary
    """
    try:
        if SHARED_STATE_FILE.exists():
            with open(SHARED_STATE_FILE, 'r') as f:
                current_data = json.load(f)
                # get current view
                current_view = current_data.get("current_view", "SUMMARY")
                if current_view != "SUMMARY":
                    current_data["current_view"] = "SUMMARY"
                    # write back to file
                    with open(SHARED_STATE_FILE, 'w') as fw:
                        json.dump(current_data, fw)
                return current_data
        else:
            return initialize_state()
    except:
        return initialize_state()

def main():
    """
    Main function to run the reader process
    Creates layout using  create_reader_layout()
    Periodically updates body using update_reader_body()
    return: None

    """
    layout = create_reader_layout()
    try:
        with Live(layout) as live:
            while True:
                state = load_state()
                if state:
                    switch_view_content(state, layout)
                sleep(5)

    except KeyboardInterrupt:
        console.print("[bold red]Reader stopped[/bold red]")

if __name__ == "__main__":
    main()