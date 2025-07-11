import tkinter as tk
from tkinter import ttk
import requests

CURRENCIES = [
    "USD - United States Dollar",
    "EUR - Euro",
    "GBP - British Pound",
    "JPY - Japanese Yen",
    "AUD - Australian Dollar",
    "CAD - Canadian Dollar",
    "CHF - Swiss Franc",
    "CNY - Chinese Yuan",
    "INR - Indian Rupee",
    "BRL - Brazilian Real",
    "ZAR - South African Rand",
    "Other"
]

def convert_currency(base, target, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][target]
    return round(amount * rate, 2)

def on_convert():
    try:
        # Get selected currencies or typed currency codes
        base = base_currency.get().split(" - ")[0] if base_currency.get() != "Other" else base_currency_other.get()
        target = target_currency.get().split(" - ")[0] if target_currency.get() != "Other" else target_currency_other.get()
        amount = float(amount_entry.get())

        # Perform conversion
        result = convert_currency(base, target, amount)
        result_label.config(text=f"{amount} {base} = {result} {target}")
    except Exception as e:
        result_label.config(text="Conversion failed!")

def on_other_selected(event, combobox, entry_field):
    """Show or hide the entry field when 'Other' is selected."""
    if combobox.get() == "Other":
        entry_field.pack(pady=(5, 10))  # Show entry field directly under the combobox
    else:
        entry_field.pack_forget()  # Hide entry field

# Create the main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x400")

# Amount input
tk.Label(window, text="Amount:").pack(pady=(10, 0))
amount_entry = tk.Entry(window)
amount_entry.pack()

# Base currency selection
tk.Label(window, text="Base Currency:").pack(pady=(10, 0))
base_currency = ttk.Combobox(window, values=CURRENCIES, state="readonly")
base_currency.set("Select base currency")
base_currency.pack()
base_currency.bind("<<ComboboxSelected>>", lambda e: on_other_selected(e, base_currency, base_currency_other))

# Custom entry for 'Other' base currency (appears directly below the dropdown when 'Other' is selected)
base_currency_other = tk.Entry(window)
base_currency_other.pack_forget()  # Initially hidden

# Target currency selection
tk.Label(window, text="Target Currency:").pack(pady=(10, 0))
target_currency = ttk.Combobox(window, values=CURRENCIES, state="readonly")
target_currency.set("Select target currency")
target_currency.pack()
target_currency.bind("<<ComboboxSelected>>", lambda e: on_other_selected(e, target_currency, target_currency_other))

# Custom entry for 'Other' target currency (appears directly below the dropdown when 'Other' is selected)
target_currency_other = tk.Entry(window)
target_currency_other.pack_forget()  # Initially hidden

# Convert button
convert_button = tk.Button(window, text="Convert", command=on_convert)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Exit button
quit_button = tk.Button(window, text="Exit", command=window.quit)
quit_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
