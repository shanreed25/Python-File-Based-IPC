
from numpy import info
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.table import Table
from rich.align import Align
from rich.prompt import Prompt
from rich import box


#=============================================
# COMMON LAYOUT COMPONENTS
# Used by both reader and writer layouts
#=============================================
def create_header(header_text, color):
    """
    Create the header section
    param header_text: str - The text to display in the header
    param color: str - The color style for the header text and border
    return: Panel - A Rich Panel object containing the header
    """
    header_text = Text(header_text, style=f"bold {color}", justify="center")
    return Panel(header_text, box=box.DOUBLE, border_style=color)

def create_footer(footer_text):
    """
    Create the footer section
    param footer_text: str - The text to display in the footer
    return: Panel - A Rich Panel object containing the footer
    """
    footer_text = Text(
        footer_text,
        style="dim cyan",
        justify="center"
    )
    return Panel(footer_text, box=box.SIMPLE)





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

    header_text = "🔄 FILE-BASED IPC READER STARTED 🔄"
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




#=============================================
# WRITER LAYOUT FUNCTIONS
#=============================================
#=============================================
# WRITER LAYOUT FUNCTIONS
#=============================================
def create_writer_layout(console):
    """
    Creates the base layout for the writer process
    param console: Console - The Rich Console object to use for output
    """

    header_text = "📝 FILE-BASED IPC WRITER STARTED 📝"
    color = "cyan"
    footer_text = "Writing to: shared_state.json | Press Ctrl+C to stop the writer process."
    console.print(create_header(header_text, color))
    console.print(create_footer(footer_text))


def update_writer_layout(console, new_message):
    """
    Update the writer's layout with a new message
    param console: Console - The Rich Console object to use for output
    param new_message: str - The new message to display in the header
    """
    console.clear()
    header_text = "📝 Writer Updated State To: " + new_message
    color = "yellow"
    console.print(create_header(header_text, color))


def create_menu(console):
    console.print()
    console.print("[yellow]Available Commands:[/yellow]")
    console.print("  [green]1[/green] - Switch View")
    console.print("  [green]2[/green] - Update Content")
    console.print("  [green]3[/green] - Add Transaction Data")
    console.print("  [green]4[/green] - Clear Data")
    console.print("  [green]5[/green] - Show Current State")
    console.print("  [green]0[/green] - Exit")
    console.print()