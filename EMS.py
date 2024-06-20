import tkinter as tk
from tkinter import messagebox

class EventManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("500x400")
        
        self.events = []
        
        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for event information
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Date:").grid(row=2, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Event Type:").grid(row=3, column=0, padx=10, pady=5)
        self.event_entry = tk.Entry(self.root)
        self.event_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for Create, Update, Delete, Clear
        self.create_button = tk.Button(self.root, text="Create", command=self.create_event)
        self.create_button.grid(row=4, column=0, padx=10, pady=5)

        self.update_button = tk.Button(self.root, text="Update", command=self.update_event)
        self.update_button.grid(row=4, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_event)
        self.delete_button.grid(row=4, column=2, padx=10, pady=5)
        
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=4, column=3, padx=10, pady=5)

        # Listbox to display events
        self.event_listbox = tk.Listbox(self.root)
        self.event_listbox.grid(row=5, column=0, columnspan=4, padx=10, pady=5)
        self.event_listbox.bind('<<ListboxSelect>>', self.on_select)

    def create_event(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        date = self.date_entry.get()
        event = self.event_entry.get()

        if not all([name, phone, date, event]):
            messagebox.showwarning("Input Error", "All fields are required")
            return

        event_info = f"{name} - {phone} - {date} - {event}"
        self.events.append(event_info)
        self.update_listbox()
        self.clear_entries()

    def update_event(self):
        selected_index = self.event_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No event selected for update")
            return

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        date = self.date_entry.get()
        event = self.event_entry.get()

        if not all([name, phone, date, event]):
            messagebox.showwarning("Input Error", "All fields are required")
            return

        event_info = f"{name} - {phone} - {date} - {event}"
        self.events[selected_index[0]] = event_info
        self.update_listbox()
        self.clear_entries()

    def delete_event(self):
        selected_index = self.event_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No event selected for deletion")
            return

        del self.events[selected_index[0]]
        self.update_listbox()
        self.clear_entries()

    def update_listbox(self):
        self.event_listbox.delete(0, tk.END)
        for event in self.events:
            self.event_listbox.insert(tk.END, event)

    def on_select(self, event):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.events[selected_index[0]]
            name, phone, date, event_type = selected_event.split(" - ")

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)

            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, phone)

            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, date)

            self.event_entry.delete(0, tk.END)
            self.event_entry.insert(0, event_type)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.event_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementSystem(root)
    root.mainloop()
