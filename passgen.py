#THIS PYTHON APPLICATION ALLOWS YOU TO CREATE A RANDOM PASSWORD  WITH SPECIFIC 
# LENGTH .


# Call the libraries
import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")

# widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()


root.mainloop()