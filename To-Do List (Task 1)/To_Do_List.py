import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x400")
        self.master.configure(bg="#F0F0F0")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.pack(pady=10)

        self.add_icon = ImageTk.PhotoImage(Image.open("E:/Suyash/Internship/CodSoft/To-Do List (Task 1)/add_icon.png").resize((20, 20)))
        self.add_button = ttk.Button(master, text="Add Task", image=self.add_icon, compound="left", command=self.add_task, style="Add.TButton")
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.edit_icon = ImageTk.PhotoImage(Image.open("E:/Suyash/Internship/CodSoft/To-Do List (Task 1)/edit_icon.png").resize((20, 20)))
        self.edit_button = ttk.Button(master, text="Edit Task", image=self.edit_icon, compound="left", command=self.edit_task, style="Edit.TButton")
        self.edit_button.pack(pady=5)

        self.delete_icon = ImageTk.PhotoImage(Image.open("E:/Suyash/Internship/CodSoft/To-Do List (Task 1)/delete_icon.png").resize((20, 20)))
        self.delete_button = ttk.Button(master, text="Delete Task", image=self.delete_icon, compound="left", command=self.delete_task, style="Delete.TButton")
        self.delete_button.pack(pady=5)

        self.style = ttk.Style()
        self.style.configure("Add.TButton", foreground="#4CAF50", background="#4CAF50", padding=5, borderwidth=0, bordercolor="#4CAF50", focusthickness=3)
        self.style.configure("Edit.TButton", foreground="#2196F3", background="#2196F3", padding=5, borderwidth=0, bordercolor="#2196F3", focusthickness=3)
        self.style.configure("Delete.TButton", foreground="#F44336", background="#F44336", padding=5, borderwidth=0, bordercolor="#F44336", focusthickness=3)

        self.refresh_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_to_edit = self.tasks[selected_index[0]]
            edited_task = simpledialog.askstring("Edit Task", f"Edit task: {task_to_edit}", parent=self.master)
            if edited_task:
                self.tasks[selected_index[0]] = edited_task
                self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            confirmation = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?", parent=self.master)
            if confirmation:
                del self.tasks[selected_index[0]]
                self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
