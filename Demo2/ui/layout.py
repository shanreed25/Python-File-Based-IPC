
from numpy import info
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.table import Table
from rich.align import Align
from rich.prompt import Prompt
from rich import box

def create_header(header_text, color):
    """Create the header section"""
    header_text = Text(header_text, style=f"bold {color}", justify="center")
    return Panel(header_text, box=box.DOUBLE, border_style=color)

def create_footer(footer_text):
    """Create the footer section"""
    footer_text = Text(
        footer_text,
        style="dim cyan",
        justify="center"
    )
    return Panel(footer_text, box=box.SIMPLE, border_style="dim")



#=============================================
# READER LAYOUT FUNCTIONS
#=============================================
def create_reader_content(state):
    """Create the main content area based on state"""

    
    #.get() is used to avoid KeyError if "content" key is missing, it is a safe way to access dictionary values
    content_text = state.get("content", "No content")# this line of code will get the content from state dictionary
    
    # Add any data from state
    if state.get("data"):# if there is a "data" key in state dictionary

        data_items_list = [f"{k}: {v}" for k, v in state["data"].items()]# create a list of strings for each key-value pair in the data dictionary

        data_str = "\n\n" + "\n".join(data_items_list)#create a single string with each key-value pair on a new line, separated by two new lines from the main content
        content_text += data_str
    
    content = Text(content_text, justify="center", style="white")
    return Panel(
        Align.center(content, vertical="middle"),
        title=f"[bold]{state.get('current_view', 'main').upper()}[/bold]",
        border_style="green",
        box=box.ROUNDED
    )


def create_reader_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", size=16),
        Layout(name="footer", size=3)
    )

    return layout

def update_reader_layout(layout, state):
    # .update() method can be used to refresh or change layout components
    # it comes from rich library's Layout class
    header_text = "🔄 FILE-BASED IPC READER STARTED 🔄"
    color = "magenta"
    footer_text = "Monitoring: shared_state.json | Use writer.py to send commands | Press Ctrl+C to stop the reader process"

    layout["header"].update(create_header(header_text, color))
    layout["footer"].update(create_footer(footer_text))
    layout["body"].update(create_reader_content(state))

def display_reader_layout(console, state):
    layout = create_reader_layout()
    update_reader_layout(layout, state)
    return console.print(layout)


#=============================================
# WRITER LAYOUT FUNCTIONS
#=============================================
def create_writer_layout():
    layout = Layout()
    layout.split_column(
    Layout(name="header", size=3),
    Layout(name="footer", size=3)
    )
    return layout

def update_writer_layout(layout):
    header_text = "📝 FILE-BASED IPC WRITER STARTED 📝"
    color = "cyan"
    footer_text = "Writing to: shared_state.json | Press Ctrl+C to stop the writer process."
    layout["header"].update(create_header(header_text, color))
    layout["footer"].update(create_footer(footer_text))

def display_writer_layout(console):
    layout = create_writer_layout()
    update_writer_layout(layout)
    return console.print(layout)