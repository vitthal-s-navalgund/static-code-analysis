import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item, qty=0, logs=None):
    """Add an item and its quantity to stock."""
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove an item from stock or reduce its quantity."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")
    except TypeError as e:
        print(f"Invalid quantity type for {item}: {e}")


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """Save current stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Display all items and quantities."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return items with stock quantity below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function for testing inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, triggers exception
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Program executed successfully.")


if __name__ == "__main__":
    main()
