import tkinter as tk
from tkinter import ttk, messagebox
import requests
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import datetime

# Load the .env file to get the API key
load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

# Function to fetch exchange rates and perform conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get().split()[0]
        to_currency = to_currency_combobox.get().split()[0]

        if from_currency == "" or to_currency == "":
            messagebox.showwarning("Input Error", "Please select both currencies.")
            return

        # API request to get exchange rates
        api_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response = requests.get(api_url)
        data = response.json()

        if response.status_code != 200 or "conversion_rates" not in data:
            messagebox.showerror("API Error", "Unable to fetch currency conversion rates.")
            return

        # Perform the currency conversion
        rate = data["conversion_rates"][to_currency]
        converted_amount = amount * rate
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")

# Function to dynamically fetch all available currency codes from the API and prioritize common currencies
def get_currency_options():
    try:
        api_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
        response = requests.get(api_url)
        data = response.json()
        
        if "supported_codes" in data:
            all_currencies = [f"{code[0]} ({code[1]})" for code in data["supported_codes"]]
            all_currencies.sort()  # Sort alphabetically

            # Common currencies to prioritize
            common_currencies = [
                "GBP (British Pound)", 
                "EUR (Euro)", 
                "USD (United States Dollar)",
                "CNY (Chinese Renminbi)", 
                "JOD (Jordanian Dinar)",
                "AED (UAE Dirham)"
            ]

            # Combine common currencies with the rest
            return common_currencies + all_currencies
        else:
            return ["USD (United States Dollar)", "EUR (Euro)", "GBP (British Pound)", "INR (Indian Rupee)", "JPY (Japanese Yen)", "CAD (Canadian Dollar)"]
    except:
        messagebox.showerror("API Error", "Unable to fetch available currencies.")
        return ["USD (United States Dollar)", "EUR (Euro)", "GBP (British Pound)", "INR (Indian Rupee)", "JPY (Japanese Yen)", "CAD (Canadian Dollar)"]

# Function to plot historical exchange rates
def plot_exchange_rate_trend():
    try:
        from_currency = from_currency_combobox.get().split()[0]
        to_currency = to_currency_combobox.get().split()[0]
        if from_currency == "" or to_currency == "":
            messagebox.showwarning("Input Error", "Please select both currencies.")
            return

        # Dummy historical data: We can simulate it for now or use an API that provides historical data
        dates = [datetime.date.today() - datetime.timedelta(days=i) for i in range(7)]
        rates = [1 + i*0.01 for i in range(7)]  # Replace with actual data from an API

        plt.plot(dates, rates, label=f'{from_currency} to {to_currency}')
        plt.title(f'Exchange Rate Trend ({from_currency} to {to_currency})')
        plt.xlabel('Date')
        plt.ylabel('Exchange Rate')
        plt.legend()
        plt.show()

    except:
        messagebox.showerror("Error", "Unable to plot the exchange rate trend.")

# Function to swap the selected currencies
def swap_currencies():
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    from_currency_combobox.set(to_currency)
    to_currency_combobox.set(from_currency)

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Entry for the amount to be converted
amount_label = tk.Label(root, text="Enter Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, width=20)
amount_entry.pack(pady=5)

# Dropdown for 'From Currency'
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
currency_options = get_currency_options()  # Get the dynamic list of currencies
from_currency_combobox = ttk.Combobox(root, values=currency_options, width=30)
from_currency_combobox.pack(pady=5)

# Dropdown for 'To Currency'
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_combobox = ttk.Combobox(root, values=currency_options, width=30)
to_currency_combobox.pack(pady=5)

# Add 'Convert' button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Add 'Swap' button to swap the currencies
swap_button = tk.Button(root, text="Swap", command=swap_currencies)
swap_button.pack(pady=5)

# Add 'Plot Trend' button to plot historical exchange rates
plot_button = tk.Button(root, text="Plot Exchange Rate Trend", command=plot_exchange_rate_trend)
plot_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
