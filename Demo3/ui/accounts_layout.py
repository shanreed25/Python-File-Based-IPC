from rich.text import Text
from rich.table import Table
from rich import box

def account_table(accounts):
    """
    Create a Rich Table to display account information
    param accounts: list - A list of account dictionaries
    return: Table - A Rich Table object containing account information
    """
    if not accounts:
        content = Text("No accounts available.", justify="center", style="white")
        return content
    else:
        table = Table(title="Accounts Overview", box=box.SIMPLE_HEAVY)
        table.add_column("Account Name", style="cyan", no_wrap=True)
        table.add_column("Account Type", style="magenta")
        table.add_column("Balance", justify="right", style="green")

        for account in accounts:
            table.add_row(
                account.get("name", "Unnamed"),
                account.get("type", "N/A"),
                f"${account.get('balance', 0):.2f}"
            )
    return table