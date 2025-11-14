# ==============================================
# FILE BASED IPC DEMONSTRATION: READER PROCESS
# ==============================================
import json
from pathlib import Path
from time import sleep

from rich.text import Text
from rich.console import Console
from rich.layout import Layout
from rich.live import Live

from ui.reader_layout import create_reader_layout, update_reader_body

console = Console()
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

def initialize_state():
    """
    Initialize the state file with default values
    This function is called if file does not exist in the load_state()
    return: dict - The initial state dictionary
    """
    initial_state = {
        "current_view": "SUMMARY",
        "content": "Welcome To Your Budget Tracker!",
        "accounts": []
    }
    with open(SHARED_STATE_FILE, 'w') as f:
        json.dump(initial_state, f)
    return initial_state

def load_state():
    """
    Load current state from file if file does not exist, 
    initialize it with default values using initialize_state()
    return: dict - The current state dictionary
    """
    try:
        if SHARED_STATE_FILE.exists():
            with open(SHARED_STATE_FILE, 'r') as f:
                return json.load(f)
        else:
            return initialize_state()
    except:
        return initialize_state()

def update_reader_content(state, layout):
    """
    Update body based on state
    param state: dict - The current state of the reader process
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """

    
    #.get() is used to avoid KeyError if "content" key is missing, it is a safe way to access dictionary values
    content_text = state.get("content", "No content")# this line of code will get the content from state dictionary
    
    # Add any data from state
    if state.get("data"):# if there is a "data" key in state dictionary

        data_items_list = [f"{k}: {v}" for k, v in state["data"].items()]# create a list of strings for each key-value pair in the data dictionary

        data_str = "\n\n" + "\n".join(data_items_list)#create a single string with each key-value pair on a new line, separated by two new lines from the main content
        content_text += data_str
    
    update_reader_body(content_text, layout)        
            
def main():
    """
    Main loop to display and update reader layout
    based on the shared state file

    """
    layout = create_reader_layout()
    try:
        #=================================================================================
        # Use Live to continuously update the layout
        # it allows dynamic updates in the terminal
        # so we can see changes in real-time, using the same layout object
        # so we dont see flickering or re-creation of layout
        #=================================================================================
        with Live(layout) as live:
            while True:
                state = load_state()
                if state:
                    update_reader_content(state, layout)
                
                sleep(5)

    except KeyboardInterrupt:
        console.print("[bold red]Reader stopped[/bold red]")

if __name__ == "__main__":
    main()