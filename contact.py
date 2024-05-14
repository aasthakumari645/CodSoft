#THIS IS A PYTHON CONTACT APPLICATION ALLOWING USERS TO CREATE A NEW CONTACT,
#SAVE IT , RETRIEVE THE CONTACT , DELETE A CONTACT , ALLOWS YOU TO SEARCH FOR A 
#SPECIFIC CONTACT. 


#IMPORTING ALL THE NECESSARY LIBRARIES
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to create the database table
def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 phone TEXT,
                 email TEXT,
                 address TEXT)''')
    conn.commit()
    conn.close()

# new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('''INSERT INTO contacts (name, phone, email, address)
                     VALUES (?, ?, ?, ?)''', (name, phone, email, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

#  view  contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT name, phone FROM contacts''')
    contacts = c.fetchall()
    conn.close()
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]} - {contact[1]}")

# search contact - NAME/NUMBER
def search_contact():
    query = search_entry.get()
    contact_list.delete(0, tk.END)
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT name, phone FROM contacts
                 WHERE name LIKE ? OR phone LIKE ?''', ('%' + query + '%', '%' + query + '%'))
    contacts = c.fetchall()
    conn.close()
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]} - {contact[1]}")

# CLEAR ENTRY FIELDS
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# create the UI
def main():
    create_table()
    root = tk.Tk()
    root.title("Contact Book")

    # labels
    tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="e")

    # entry fields
    global name_entry, phone_entry, email_entry, address_entry, search_entry
    name_entry = tk.Entry(root)
    phone_entry = tk.Entry(root)
    email_entry = tk.Entry(root)
    address_entry = tk.Entry(root)
    search_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)
    email_entry.grid(row=2, column=1, padx=5, pady=5)
    address_entry.grid(row=3, column=1, padx=5, pady=5)
    search_entry.grid(row=5, column=1, padx=5, pady=5, sticky="we")

    # buttons
    add_button = tk.Button(root, text="Add Contact", command=add_contact)
    view_button = tk.Button(root, text="View Contacts", command=view_contacts)
    search_button = tk.Button(root, text="Search", command=search_contact)
    clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
    add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
    view_button.grid(row=6, column=0, columnspan=1, padx=5, pady=5, sticky="we")
    search_button.grid(row=5, column=0, padx=5, pady=5, sticky="we")
    clear_button.grid(row=6, column=1, padx=5, pady=5, sticky="we")

    # displaying contacts
    global contact_list
    contact_list = tk.Listbox(root)
    contact_list.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # grid resizing
    root.columnconfigure(1, weight=1)
    root.rowconfigure(7, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()