from rich import box
from rich.text import Text
from rich.panel import Panel

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