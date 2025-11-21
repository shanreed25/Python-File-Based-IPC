from rich.text import Text
from rich.table import Table
from rich import box

def create_transaction_table(transactions_with_account_names):
    """
    Create a Rich Table to display transaction information
    param transactions_with_account_names: list - List of transactions with account names
    return: Table - A Rich Table object containing the transaction data
    """

    if not transactions_with_account_names:
        content = Text("No transactions available.", justify="center", style="white")
        return content
    else:
        table = Table(title="Transactions", box=box.SIMPLE_HEAVY)

        table.add_column("Account Name", style="cyan", no_wrap=True)
        table.add_column("Amount", style="magenta")
        table.add_column("Description", style="green")

        for transaction in transactions_with_account_names:
            account_name = transaction.get("account_name", "Unknown")
            amount = str(transaction.get("amount", "0.00"))
            description = transaction.get("description", "")

            table.add_row(account_name, amount, description)

    return table
