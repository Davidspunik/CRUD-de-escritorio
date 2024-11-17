import tkinter as tk
from tkinter import ttk, messagebox


class SimpleCRUDApp:
    def __init__(self):
        self.data = []  # Lista para almacenar los datos como (ID, Name, Email)
        self.counter = 1  # Contador para generar IDs únicos
        self.root = tk.Tk()
        self.root.title("CRUD Simple")
        self.build_gui()

    def build_gui(self):
        # Entry fields
        tk.Label(self.root, text="Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Email").grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.root, text="Insert", command=self.insert_record).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Update", command=self.update_record).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Delete", command=self.delete_record).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Clear", command=self.clear_inputs).grid(row=3, column=1, padx=5, pady=5)

        # Treeview
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def insert_record(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        if name and email:
            self.data.append((self.counter, name, email))
            self.counter += 1
            self.refresh_table()
            self.clear_inputs()
            messagebox.showinfo("Success", "Record added successfully!")
        else:
            messagebox.showwarning("Validation", "Please provide both name and email.")

    def update_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_index = self.tree.index(selected_item[0])
            name = self.name_entry.get()
            email = self.email_entry.get()
            if name and email:
                self.data[item_index] = (self.data[item_index][0], name, email)
                self.refresh_table()
                self.clear_inputs()
                messagebox.showinfo("Success", "Record updated successfully!")
            else:
                messagebox.showwarning("Validation", "Please provide both name and email.")
        else:
            messagebox.showwarning("Selection", "No record selected.")

    def delete_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_index = self.tree.index(selected_item[0])
            del self.data[item_index]
            self.refresh_table()
            self.clear_inputs()
            messagebox.showinfo("Success", "Record deleted successfully!")
        else:
            messagebox.showwarning("Selection", "No record selected.")

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for record in self.data:
            self.tree.insert("", "end", values=record)

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SimpleCRUDApp()
    app.run()
