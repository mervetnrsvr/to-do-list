import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.configure(bg="lightblue")

        self.todo_list = []

        self.frame = tk.Frame(self.root, bg="lightblue")
        self.frame.pack(pady=25)

        self.todo_entry = tk.Entry(self.frame, width=50)
        self.todo_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.frame, text="Add", command=self.add_task, bg="orange", fg="black")
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

       
        self.tasks_frame = tk.Frame(self.root, bg="lightblue", width=400, height=300, bd=1, relief="solid")
        self.tasks_frame.pack(pady=20)
        self.tasks_frame.pack_propagate(False)  

        self.remove_button = tk.Button(self.root, text="Delete", command=self.remove_task, bg="orange", fg="black")
        self.remove_button.pack(pady=5)

        

    def add_task(self):
        task_text = self.todo_entry.get()
        if task_text:
            var = tk.BooleanVar()
            task_frame = tk.Frame(self.tasks_frame, bg="lightblue")
            check_button = tk.Checkbutton(task_frame, variable=var, bg="lightblue")
            check_button.pack(side=tk.LEFT)
            task_label = tk.Label(task_frame, text=task_text, bg="lightblue")
            task_label.pack(side=tk.LEFT)
            task_frame.pack(anchor='w', pady=2)
            
            self.todo_list.append((task_frame, var))
            self.todo_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            for task_frame, var in self.todo_list:
                if var.get():
                    task_frame.destroy()
            self.todo_list = [(task_frame, var) for task_frame, var in self.todo_list if not var.get()]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
