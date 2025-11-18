
from utils.transaction import add_new_transaction
from utils.account import add_new_account


def choice_exit(console):
    """
    Return the choice string for exiting the menu
    return: str - The choice string for exiting
    """
    console.print("\n[yellow]Exiting Command Client. Goodbye! 👋[/yellow]\n")
    return 0

def choice_view_summary(console):
    """
    Return the choice string for viewing summary
    return: str - The choice string for viewing summary
    """
    console.print("\n[yellow]Viewing Summary! 👋[/yellow]\n")


def choice_add_new_account(console, state, write_shared_state):
    new_account = add_new_account(state, console)
    if new_account:
        write_shared_state(new_account)
    else:
        console.print("[red]Failed to add new account.[/red]")


def choice_add_new_transaction(console, state, write_shared_state):
    new_transaction = add_new_transaction(state, console)
    if new_transaction:
        write_shared_state(new_transaction)
    else:
        console.print("[red]Failed to add new transaction.[/red]")


def choice_view_accounts(console, read_shared_state, write_shared_state):
    state = read_shared_state()
    state["current_view"] = "ACCOUNTS"
    write_shared_state(state)
    console.print("\n[yellow]Viewing Accounts! 👋[/yellow]\n")