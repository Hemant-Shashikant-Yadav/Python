import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import json
import barcode
from barcode.writer import ImageWriter
import os
import platform
from datetime import datetime

# File to store inventory data and transactions
DATA_FILE = 'inventory.json'
BARCODE_DIR = 'barcodes'
TRANSACTION_FILE = 'transactions.json'

# Ensure barcode directory exists
os.makedirs(BARCODE_DIR, exist_ok=True)

# Load inventory data from JSON file
def load_inventory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save inventory data to JSON file
def save_inventory(inventory):
    with open(DATA_FILE, 'w') as file:
        json.dump(inventory, file)

# Load transaction records
def load_transactions():
    if os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, 'r') as file:
            return json.load(file)
    return []

# Save transaction records
def save_transactions(transactions):
    with open(TRANSACTION_FILE, 'w') as file:
        json.dump(transactions, file)

# Generate a barcode for a product
def generate_barcode(product_name, product_code, save_to_desktop=False):
    ean = barcode.get('ean13', product_code, writer=ImageWriter())
    filename = os.path.join(BARCODE_DIR, f'{product_name}.png')
    
    if save_to_desktop:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') if platform.system() == 'Windows' else os.path.join(os.path.expanduser('~'), 'Desktop')
        filename = os.path.join(desktop, f'{product_name}.png')
    
    ean.save(filename)
    return filename

# Calculate check digit for EAN-13
def calculate_check_digit(ean):
    total = sum(int(ean[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)

# Add product to inventory
def add_product():
    product_name = simpledialog.askstring("Input", "Enter Product Name:")
    product_code = simpledialog.askstring("Input", "Enter Product Code (12 digits):")
    quantity = simpledialog.askinteger("Input", "Enter Quantity:")
    
    if product_name and product_code and quantity is not None:
        if len(product_code) != 12 or not product_code.isdigit():
            messagebox.showwarning("Warning", "Product code must be 12 digits.")
            return

        check_digit = calculate_check_digit(product_code)
        full_code = product_code + check_digit
        
        inventory = load_inventory()
        inventory[full_code] = {
            'name': product_name,
            'quantity': quantity
        }
        save_inventory(inventory)
        generate_barcode(product_name, full_code)  # Default save to barcode directory
        record_transaction(f"Added {product_name} with code {full_code} and quantity {quantity}.")
        messagebox.showinfo("Success", f"Added {product_name} with code {full_code} and quantity {quantity}.")
    else:
        messagebox.showwarning("Warning", "All fields are required.")

# Remove product from inventory
def remove_product():
    product_code = simpledialog.askstring("Input", "Enter Product Code (EAN-13) to remove:")
    
    if product_code:
        inventory = load_inventory()
        if product_code in inventory:
            quantity = simpledialog.askinteger("Input", "Enter Quantity to Remove:")
            if quantity is not None and quantity <= inventory[product_code]['quantity']:
                inventory[product_code]['quantity'] -= quantity
                if inventory[product_code]['quantity'] == 0:
                    del inventory[product_code]
                save_inventory(inventory)
                record_transaction(f"Removed {quantity} from {inventory[product_code]['name']}.")
                messagebox.showinfo("Success", f"Removed {quantity} from {inventory[product_code]['name']}.")
            else:
                messagebox.showwarning("Warning", "Invalid quantity.")
        else:
            messagebox.showwarning("Warning", "Product code not found.")
    else:
        messagebox.showwarning("Warning", "Product code is required.")

# Update quantity (add or reduce)
def update_quantity(action):
    inventory = load_inventory()
    if not inventory:
        messagebox.showwarning("Warning", "No items in inventory to select from.")
        return

    # Create a new window for product selection
    select_window = tk.Toplevel(app)
    select_window.title(f"{action.capitalize()} Product Quantity")

    product_names = [details['name'] for details in inventory.values()]
    selected_product = tk.StringVar()

    # Create a dropdown for product selection
    product_combobox = ttk.Combobox(select_window, textvariable=selected_product, values=product_names)
    product_combobox.pack(pady=10)

    def on_update():
        product_name = selected_product.get()
        if product_name:
            # Find the corresponding product code
            product_code = next(code for code, details in inventory.items() if details['name'] == product_name)
            new_quantity = simpledialog.askinteger("Input", f"Enter new quantity for {product_name}:")
            if new_quantity is not None:
                inventory[product_code]['quantity'] = new_quantity
                save_inventory(inventory)
                record_transaction(f"{action.capitalize()}d quantity for {product_name} to {new_quantity}.")
                messagebox.showinfo("Success", f"{action.capitalize()}d quantity for {product_name} to {new_quantity}.")
                select_window.destroy()
            else:
                messagebox.showwarning("Warning", "Quantity is required.")
        else:
            messagebox.showwarning("Warning", "Please select a product.")

    update_button = tk.Button(select_window, text=f"{action.capitalize()} Quantity", command=on_update)
    update_button.pack(pady=10)

# Record transaction
def record_transaction(message):
    transactions = load_transactions()
    transaction_entry = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'message': message
    }
    transactions.append(transaction_entry)
    save_transactions(transactions)

# View inventory
def view_inventory():
    inventory = load_inventory()
    if not inventory:
        messagebox.showinfo("Inventory", "No items in inventory.")
        return
    
    inventory_list = "Product Code\tName\tQuantity\n"
    inventory_list += "-" * 50 + "\n"
    for product_code, details in inventory.items():
        inventory_list += f"{product_code}\t{details['name']}\t{details['quantity']}\n"
    
    messagebox.showinfo("Inventory", inventory_list)

# View transaction history
def view_transactions():
    transactions = load_transactions()
    if not transactions:
        messagebox.showinfo("Transactions", "No transactions recorded.")
        return
    
    transaction_list = "Timestamp\tMessage\n"
    transaction_list += "-" * 50 + "\n"
    for transaction in transactions:
        transaction_list += f"{transaction['timestamp']}\t{transaction['message']}\n"
    
    messagebox.showinfo("Transaction History", transaction_list)

# Generate and save barcode to desktop
def generate_and_save_barcode():
    inventory = load_inventory()
    if not inventory:
        messagebox.showwarning("Warning", "No items in inventory to select from.")
        return

    # Create a new window for product selection
    select_window = tk.Toplevel(app)
    select_window.title("Select Product for Barcode")

    product_names = [details['name'] for details in inventory.values()]
    selected_product = tk.StringVar()

    # Create a dropdown for product selection
    product_combobox = ttk.Combobox(select_window, textvariable=selected_product, values=product_names)
    product_combobox.pack(pady=10)

    def on_generate():
        product_name = selected_product.get()
        if product_name:
            # Find the corresponding product code
            product_code = next(code for code, details in inventory.items() if details['name'] == product_name)
            generate_barcode(product_name, product_code, save_to_desktop=True)
            messagebox.showinfo("Success", f"Barcode for {product_name} saved to Desktop.")
            select_window.destroy()  # Close the selection window
        else:
            messagebox.showwarning("Warning", "Please select a product.")

    generate_button = tk.Button(select_window, text="Generate Barcode", command=on_generate)
    generate_button.pack(pady=10)

# Create main application window
app = tk.Tk()
app.title("Inventory Management System")

# Create buttons
add_button = tk.Button(app, text="Add Product", command=add_product)
add_button.pack(pady=10)

remove_button = tk.Button(app, text="Remove Product", command=remove_product)
remove_button.pack(pady=10)

view_button = tk.Button(app, text="View Inventory", command=view_inventory)
view_button.pack(pady=10)

generate_barcode_button = tk.Button(app, text="Generate Barcode for Desktop", command=generate_and_save_barcode)
generate_barcode_button.pack(pady=10)

# Add quantity buttons
add_quantity_button = tk.Button(app, text="Add Product Quantity", command=lambda: update_quantity("add"))
add_quantity_button.pack(pady=10)

reduce_quantity_button = tk.Button(app, text="Reduce Product Quantity", command=lambda: update_quantity("reduce"))
reduce_quantity_button.pack(pady=10)

# View transactions button
view_transactions_button = tk.Button(app, text="View Transactions", command=view_transactions)
view_transactions_button.pack(pady=10)

# Start the application
app.mainloop()
