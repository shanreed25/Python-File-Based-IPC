from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich import box

from ui.common_layouts import create_header, create_footer
from ui.accounts_layout import account_table
#=============================================
# READER LAYOUT FUNCTIONS
#=============================================

def create_reader_layout():
    """
    Creates the base layout for the reader process
    return: Layout - A Rich Layout object with header, body, and footer sections
    """
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", size=16),
        Layout(name="footer", size=3)
    )

    header_text = "💸  BUDGET TRACKER CLI 💸"
    color = "magenta"
    # body_text = "Waiting for updates from writer process..."
    footer_text = "Monitoring: shared_state.json | Use writer.py to send commands | Press Ctrl+C to stop the reader process"


    layout["header"].update(create_header(header_text, color))
    layout["footer"].update(create_footer(footer_text))
    # layout["body"].update(create_reader_main_content(body_text))

    return layout


def update_reader_body(state, layout):
    """
    Update the reader's body with new content and state
    param state: dict - The current state dictionary
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """

    current_view = state.get("current_view", "SUMMARY")
    accounts = state.get("accounts", [])
    content = account_table(accounts)
    body = Panel(
        Align.center(content, vertical="middle"),
        title=current_view,
        border_style="green",
        box=box.ROUNDED
    )
    return layout["body"].update(body)




    
