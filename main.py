
# codsoft To-Do List application project


import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Codsoft")

        # Define colors
        self.bg_color = "#09112e" 
        self.font_color = "#FFFFFF"  

        self.tasks = []

        self.task_entry = tk.Entry(root, width=50, bg=self.bg_color, fg=self.font_color)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task, bg=self.bg_color, fg=self.font_color)
        add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=60, bg=self.bg_color, fg=self.font_color)
        self.task_listbox.pack(pady=10)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg=self.bg_color, fg=self.font_color)
        remove_button.pack(pady=5)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    task = task.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    
    # Set background color
    root.configure(bg=app.bg_color)
    
    root.mainloop()

if __name__ == "__main__":
    main()

