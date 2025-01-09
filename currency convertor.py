import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch exchange rate data from API
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and target_currency in data['conversion_rates']:
            return data['conversion_rates'][target_currency]
        else:
            messagebox.showerror("Error", "Unable to fetch exchange rates. Please try again later.")
            return None
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return None

# Function to perform currency conversion
def convert_currency():
    try:
        base_amount = float(entry_amount.get())
        base_currency = combo_base_currency.get()
        target_currency = combo_target_currency.get()

        if base_amount <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive amount.")
            return

        # Fetch exchange rate
        rate = get_exchange_rate(base_currency, target_currency)
        if rate is None:
            return

        converted_amount = base_amount * rate
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {target_currency}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")

# Create main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x300")

# Create labels, entry boxes, and buttons
label_amount = tk.Label(window, text="Amount:")
label_amount.pack(pady=5)

entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

label_base_currency = tk.Label(window, text="From Currency:")
label_base_currency.pack(pady=5)

# Currency options
currencies = ["USD", "EUR", "GBP", "INR", "CAD", "AUD", "JPY"]

combo_base_currency = tk.StringVar(window)
combo_base_currency.set(currencies[0])  # Default selection
drop_base_currency = tk.OptionMenu(window, combo_base_currency, *currencies)
drop_base_currency.pack(pady=5)

label_target_currency = tk.Label(window, text="To Currency:")
label_target_currency.pack(pady=5)

combo_target_currency = tk.StringVar(window)
combo_target_currency.set(currencies[1])  # Default selection
drop_target_currency = tk.OptionMenu(window, combo_target_currency, *currencies)
drop_target_currency.pack(pady=5)

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=20)

# Result label
result_label = tk.Label(window, text="Converted Amount: ")
result_label.pack(pady=5)

# Run the application
window.mainloop()

