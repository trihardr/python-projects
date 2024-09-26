import tkinter as tk
from tkinter import messagebox
import os

# Function to add a task with category and deadline
def add_task():
    task = task_entry.get()
    category = category_entry.get()
    deadline = deadline_entry.get()
    if task != "":
        task_info = f"{task} - {category} - {deadline}"
        task_listbox.insert(tk.END, task_info)
        task_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        task_listbox.delete(tk.ANCHOR)
    except:
        messagebox.showwarning("Remove Error", "Please select a task to remove.")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)  # Get all tasks from the listbox
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    messagebox.showinfo("Save Success", "Tasks saved successfully!")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())  # Add tasks back into listbox

# Function to edit a selected task
def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get index of the selected task
        new_task = task_entry.get()
        new_category = category_entry.get()
        new_deadline = deadline_entry.get()
        if new_task != "":
            task_info = f"{new_task} - {new_category} - {new_deadline}"
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, task_info)
            task_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            deadline_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task.")
    except IndexError:
        messagebox.showwarning("Edit Error", "Please select a task to edit.")

# Function to sort tasks alphabetically
def sort_tasks():
    tasks = list(task_listbox.get(0, tk.END))  # Get all tasks from the listbox
    tasks.sort()  # Sort tasks alphabetically
    task_listbox.delete(0, tk.END)  # Clear listbox
    for task in tasks:
        task_listbox.insert(tk.END, task)  # Insert sorted tasks

# Function to enable dark mode
def enable_dark_mode():
    root.config(bg="black")
    task_entry.config(bg="gray", fg="white")
    category_entry.config(bg="gray", fg="white")
    deadline_entry.config(bg="gray", fg="white")
    task_listbox.config(bg="gray", fg="white")
    add_button.config(bg="black", fg="white")
    remove_button.config(bg="black", fg="white")
    save_button.config(bg="black", fg="white")
    load_button.config(bg="black", fg="white")
    edit_button.config(bg="black", fg="white")
    sort_button.config(bg="black", fg="white")
    dark_mode_button.config(bg="black", fg="white")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget for the task
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=5)
task_entry.insert(0, "Enter Task")

# Create an entry widget for the category
category_entry = tk.Entry(root, width=35)
category_entry.pack(pady=5)
category_entry.insert(0, "Enter Category (e.g., Work, Personal)")

# Create an entry widget for the deadline
deadline_entry = tk.Entry(root, width=35)
deadline_entry.pack(pady=5)
deadline_entry.insert(0, "Enter Deadline (e.g., 2024-09-30)")

# Create an 'Add Task' button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Create a 'Remove Task' button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Create 'Save Tasks' and 'Load Tasks' buttons
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack(pady=5)

# Create an 'Edit Task' button
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

# Create a 'Sort Tasks' button
sort_button = tk.Button(root, text="Sort Tasks", command=sort_tasks)
sort_button.pack(pady=5)

# Create a 'Dark Mode' button
dark_mode_button = tk.Button(root, text="Enable Dark Mode", command=enable_dark_mode)
dark_mode_button.pack(pady=5)

# Load tasks when the program starts
load_tasks()

# Run the application
root.mainloop()
