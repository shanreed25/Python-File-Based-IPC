
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich import box

from ui.common_layouts import create_header, create_footer
#=============================================
# READER LAYOUT FUNCTIONS
#=============================================
def create_reader_main_content(content_text):
    """
    Creates the reader body area
    param content_text: str - The text to display in the main content area
    return: Panel - A Rich Panel object containing the main content
    """
    content = Text(content_text, justify="center", style="white")
    return Panel(
        Align.center(content, vertical="middle"),
        title="[bold]MAIN CONTENT[/bold]",
        border_style="green",
        box=box.ROUNDED
    )

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
    body_text = "Waiting for updates from writer process..."
    footer_text = "Monitoring: shared_state.json | Use writer.py to send commands | Press Ctrl+C to stop the reader process"

    # .update() method can be used to refresh or change layout components
    # it comes from rich library's Layout class
    layout["header"].update(create_header(header_text, color))
    layout["footer"].update(create_footer(footer_text))
    layout["body"].update(create_reader_main_content(body_text))

    return layout


def update_reader_body(content_text, layout):
    """
    Update the reader's body with new content and state
    param content_text: str - The text to display in the main content area
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """

    body = create_reader_main_content(content_text)
    return layout["body"].update(body)




    
