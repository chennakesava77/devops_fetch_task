from tabulate import tabulate

def print_table(data):
    if not data:
        print("No data found.")
        return

    # Ensure all dicts have the same keys
    all_keys = set()
    for row in data:
        all_keys.update(row.keys())
    headers = list(all_keys)

    # Fill missing keys with empty string
    normalized_data = []
    for row in data:
        normalized_row = {key: row.get(key, "") for key in headers}
        normalized_data.append(normalized_row)

    table = tabulate(normalized_data, headers="keys", tablefmt="grid")
    print(table)
