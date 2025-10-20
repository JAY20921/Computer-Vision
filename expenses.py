import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime

# Database setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        amount REAL NOT NULL
    )
""")
conn.commit()

# Insert expense into database
def add_expense():
    date = date_entry.get()
    category = category_var.get()
    description = description_entry.get()
    amount = amount_entry.get()

    if not date or not category or not amount:
        messagebox.showerror("Error", "Please fill all mandatory fields")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    cursor.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
                   (date, category, description, float(amount)))
    conn.commit()
    messagebox.showinfo("Success", "Expense added!")
    clear_fields()
    load_expenses()

def clear_fields():
    date_entry.delete(0, tk.END)
    category_var.set("Food")
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def load_expenses():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

def delete_expense():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    item = tree.item(selected)
    expense_id = item["values"][0]
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    load_expenses()

# GUI setup
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("700x500")
root.resizable(False, False)

# Top frame (input)
input_frame = tk.Frame(root, pady=10)
input_frame.pack(fill="x")

tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(input_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)
date_entry.insert(0, datetime.date.today().isoformat())

tk.Label(input_frame, text="Category:").grid(row=0, column=2, padx=5, pady=5)
category_var = tk.StringVar(value="Food")
category_menu = ttk.Combobox(input_frame, textvariable=category_var, values=["Food", "Transport", "Utilities", "Entertainment", "Other"], state="readonly")
category_menu.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame, width=50)
description_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

tk.Label(input_frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white")
add_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="we")

# Middle frame (table)
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

tree = ttk.Treeview(table_frame, columns=("ID", "Date", "Category", "Description", "Amount"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=100 if col != "Description" else 250)

tree.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Bottom frame (delete button)
bottom_frame = tk.Frame(root, pady=10)
bottom_frame.pack()

delete_button = tk.Button(bottom_frame, text="Delete Selected", command=delete_expense, bg="#f44336", fg="white")
delete_button.pack()

# Load existing expenses on start
load_expenses()

root.mainloop()
