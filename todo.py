import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        # Initialize tasks list
        self.tasks = []

        # Create entry field for adding tasks
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create button to add tasks
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        # Create listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Create button to delete selected task
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=10)

        # Create button to clear all tasks
        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=5, pady=10)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index[0])
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
