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

# Color palette
DARK_BLUE = "#1a5f7a"
MEDIUM_BLUE = "#159895"
LIGHT_BLUE = "#57c5b6"
VERY_LIGHT_BLUE = "#e6f4f1"

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

from PIL import Image, ImageDraw, ImageFont

# Generate a barcode for a product
def generate_barcode(product_name, product_code, save_to_downloads=False):
    ean = barcode.get('ean13', product_code, writer=ImageWriter())
    filename = os.path.join(BARCODE_DIR, f'{product_name}.png')
    
    if save_to_downloads:
        Downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads') if platform.system() == 'Windows' else os.path.join(os.path.expanduser('~'), 'Downloads')
        filename = os.path.join(Downloads, f'{product_name}')
    
    ean.save(filename)
    filename = os.path.join(Downloads, f'{product_name}.png')
    # Open the saved image
    img = Image.open(filename)
    
    # Create a new image with extra space for text
    new_img = Image.new('RGB', (img.width, img.height + 30), color='white')
    new_img.paste(img, (0, 0))
    
    # Add the product name text
    draw = ImageDraw.Draw(new_img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    
    text_width = draw.textlength(product_name, font=font)
    text_position = ((new_img.width - text_width) / 2, img.height)
    draw.text(text_position, product_name, fill='black', font=font)
    
    # Save the new image
    new_img.save(filename)
    
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
    select_window.configure(bg=VERY_LIGHT_BLUE)

    product_names = [details['name'] for details in inventory.values()]
    selected_product = tk.StringVar()

    # Create a dropdown for product selection
    product_combobox = ttk.Combobox(select_window, textvariable=selected_product, values=product_names, width=30)
    product_combobox.pack(pady=20, padx=20)

    def on_update():
        product_name = selected_product.get()
        if product_name:
            # Find the corresponding product code
            product_code = next(code for code, details in inventory.items() if details['name'] == product_name)
            current_quantity = inventory[product_code]['quantity']
            
            if action == "add":
                quantity_to_add = simpledialog.askinteger("Input", f"Enter quantity to add for {product_name}:")
                if quantity_to_add is not None and quantity_to_add >= 0:
                    new_quantity = current_quantity + quantity_to_add
                    inventory[product_code]['quantity'] = new_quantity
                    save_inventory(inventory)
                    record_transaction(f"Added {quantity_to_add} to {product_name}. New quantity: {new_quantity}.")
                    messagebox.showinfo("Success", f"Added {quantity_to_add} to {product_name}. New quantity: {new_quantity}.")
                else:
                    messagebox.showwarning("Warning", "Invalid quantity. Please enter a non-negative number.")
            elif action == "reduce":
                quantity_to_reduce = simpledialog.askinteger("Input", f"Enter quantity to reduce for {product_name}:")
                if quantity_to_reduce is not None and 0 <= quantity_to_reduce <= current_quantity:
                    new_quantity = current_quantity - quantity_to_reduce
                    inventory[product_code]['quantity'] = new_quantity
                    save_inventory(inventory)
                    record_transaction(f"Reduced {quantity_to_reduce} from {product_name}. New quantity: {new_quantity}.")
                    messagebox.showinfo("Success", f"Reduced {quantity_to_reduce} from {product_name}. New quantity: {new_quantity}.")
                else:
                    messagebox.showwarning("Warning", "Invalid quantity. Please enter a number between 0 and the current quantity.")
            
            select_window.destroy()
        else:
            messagebox.showwarning("Warning", "Please select a product.")

    update_button = tk.Button(select_window, text=f"{action.capitalize()} Quantity", command=on_update,
                              bg=MEDIUM_BLUE, fg="white", font=("Arial", 12), width=20, height=2)
    update_button.pack(pady=20)

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

# Generate and save barcode to Downloads
def generate_and_save_barcode():
    inventory = load_inventory()
    if not inventory:
        messagebox.showwarning("Warning", "No items in inventory to select from.")
        return

    # Create a new window for product selection
    select_window = tk.Toplevel(app)
    select_window.title("Select Product for Barcode")
    select_window.configure(bg=VERY_LIGHT_BLUE)

    product_names = [details['name'] for details in inventory.values()]
    selected_product = tk.StringVar()

    # Create a dropdown for product selection
    product_combobox = ttk.Combobox(select_window, textvariable=selected_product, values=product_names, width=30)
    product_combobox.pack(pady=20, padx=20)

    def on_generate():
        product_name = selected_product.get()
        if product_name:
            # Find the corresponding product code
            product_code = next(code for code, details in inventory.items() if details['name'] == product_name)
            generate_barcode(product_name, product_code, save_to_downloads=True)
            messagebox.showinfo("Success", f"Barcode for {product_name} saved to Downloads.")
            select_window.destroy()  # Close the selection window
        else:
            messagebox.showwarning("Warning", "Please select a product.")

    generate_button = tk.Button(select_window, text="Generate Barcode", command=on_generate,
                                bg=MEDIUM_BLUE, fg="white", font=("Arial", 12), width=20, height=2)
    generate_button.pack(pady=20)

# Create custom theme for ttk widgets
def create_custom_theme():
    style = ttk.Style()
    if "custom" not in style.theme_names():
        style.theme_create("custom", parent="alt", settings={
            "TCombobox": {
                "configure": {"selectbackground": MEDIUM_BLUE, "fieldbackground": "white",
                              "background": LIGHT_BLUE}
            }
        })
    style.theme_use("custom")

# Create main application window
app = tk.Tk()
app.title("Inventory Management System")
app.configure(bg=VERY_LIGHT_BLUE)
app.geometry("500x600")  # Increased window size

# Create custom theme
create_custom_theme()

# Create a frame for buttons
button_frame = tk.Frame(app, bg=VERY_LIGHT_BLUE)
button_frame.pack(pady=20)

# Create buttons with updated style
button_style = {'bg': MEDIUM_BLUE, 'fg': 'white', 'font': ("Arial", 12), 'width': 25, 'height': 2}

add_button = tk.Button(button_frame, text="Add Product", command=add_product, **button_style)
remove_button = tk.Button(button_frame, text="Remove Product", command=remove_product, **button_style)
view_button = tk.Button(button_frame, text="View Inventory", command=view_inventory, **button_style)
generate_barcode_button = tk.Button(button_frame, text="Generate Barcode for Downloads", command=generate_and_save_barcode, **button_style)
add_quantity_button = tk.Button(button_frame, text="Add Product Quantity", command=lambda: update_quantity("add"), **button_style)
reduce_quantity_button = tk.Button(button_frame, text="Reduce Product Quantity", command=lambda: update_quantity("reduce"), **button_style)
view_transactions_button = tk.Button(button_frame, text="View Transactions", command=view_transactions, **button_style)

# Place buttons in the grid
add_button.grid(row=0, column=0, padx=10, pady=10)
remove_button.grid(row=1, column=0, padx=10, pady=10)
view_button.grid(row=2, column=0, padx=10, pady=10)
generate_barcode_button.grid(row=3, column=0, padx=10, pady=10)
add_quantity_button.grid(row=4, column=0, padx=10, pady=10)
reduce_quantity_button.grid(row=5, column=0, padx=10, pady=10)
view_transactions_button.grid(row=6, column=0, padx=10, pady=10)

# Start the application
app.mainloop()