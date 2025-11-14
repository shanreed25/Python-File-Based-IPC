from ui.common_layouts import create_header, create_footer


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
    console.print("  [green]4[/green] - Add Account")
    console.print("  [green]5[/green] - Show Current State")
    console.print("  [green]0[/green] - Exit")
    console.print()


# def new_account_prompt(console):
#    """  
#    Add a new account by prompting the user for details.
#    param console: Console - The Rich Console object to use for input/output
#    """
#    console.print("\n[bold green]Add New Account[/bold green]")
    
#    account_name = console.input("Enter Account Name: ")
#    account_type = console.input("Enter Account Type (e.g., Savings, Checking): ")
#    initial_balance = console.input("Enter Initial Balance: ")