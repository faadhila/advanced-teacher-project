"""Discount Calculator (GUI)
Menghitung harga akhir setelah diskon.
Input: harga asli, diskon (%), jumlah barang.
"""

import tkinter as tk
from tkinter import messagebox


def calculate_final_price(price, discount_percent, quantity):
    """Hitung harga akhir: (harga x jumlah) dikurangi diskon."""
    subtotal = price * quantity
    discount_amount = subtotal * discount_percent / 100
    return subtotal - discount_amount


def on_calculate():
    """Dipanggil saat tombol Calculate diklik."""
    try:
        price = float(price_entry.get())
        discount = float(discount_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    if price < 0 or quantity < 1:
        messagebox.showerror("Input Error", "Price must be 0 or more and quantity at least 1.")
        return
    if not 0 <= discount <= 100:
        messagebox.showerror("Input Error", "Discount must be between 0 and 100.")
        return

    final_price = calculate_final_price(price, discount, quantity)
    result_label.config(text=f"Final Price: Rp. {final_price:.2f}")


# --- Window ---
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("320x300")

tk.Label(root, text="Original Price:").pack(pady=(15, 0))
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Discount (%):").pack(pady=(10, 0))
discount_entry = tk.Entry(root)
discount_entry.pack()

tk.Label(root, text="Quantity:").pack(pady=(10, 0))
quantity_entry = tk.Entry(root)
quantity_entry.insert(0, "1")
quantity_entry.pack()

tk.Button(root, text="Calculate", command=on_calculate).pack(pady=15)

result_label = tk.Label(root, text="Final Price: Rp. 0.00", font=("Arial", 11, "bold"))
result_label.pack()

root.mainloop()