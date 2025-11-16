from rich.text import Text
from rich.table import Table
from rich import box

def transaction_table(transactions):
    """
    Create a Rich Table to display transaction information
    param transactions: list - A list of transaction dictionaries
    return: Table - A Rich Table object containing transaction information
    """
    if not transactions:
        content = Text("No transactions available.", justify="center", style="white")
        return content
    else:
        table = Table(title="Transactions", box=box.SIMPLE_HEAVY)
        table.add_column("Amount", justify="right", style="green")
        table.add_column("Description", style="yellow")

        for transaction in transactions:
            table.add_row(
                f"${transaction.get('amount', 0):.2f}",
                transaction.get("description", "No description")
            )
    return table