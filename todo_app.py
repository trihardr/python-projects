import tkinter as tk

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a selected task
def remove_task():
    task_listbox.delete(tk.ANCHOR)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget where the user can type tasks
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# Create an 'Add Task' button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Create a 'Remove Task' button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Run the application
root.mainloop()
