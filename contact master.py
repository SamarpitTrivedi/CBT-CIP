import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactMaster:
    def __init__(self, root):
        self.root = root
        self.contacts = self.load_contacts()
        self.name_var = tk.StringVar()
        self.phone_number_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x")
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill="x")
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x")
        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(fill="x")

        # Create labels and entries
        tk.Label(self.frame1, text="Name:").pack(side="left")
        tk.Entry(self.frame1, textvariable=self.name_var).pack(side="left")
        tk.Label(self.frame2, text="Phone Number:").pack(side="left")
        tk.Entry(self.frame2, textvariable=self.phone_number_var).pack(side="left")
        tk.Label(self.frame3, text="Email:").pack(side="left")
        tk.Entry(self.frame3, textvariable=self.email_var).pack(side="left")

        # Create buttons
        tk.Button(self.frame4, text="Add Contact", command=self.add_contact).pack(side="left")
        tk.Button(self.frame4, text="Delete Contact", command=self.delete_contact).pack(side="left")
        tk.Button(self.frame4, text="Search Contact", command=self.search_contact).pack(side="left")
        tk.Button(self.frame4, text="Display Contacts", command=self.display_contacts).pack(side="left")

        # Create search entry
        tk.Label(self.frame1, text="Search:").pack(side="left")
        tk.Entry(self.frame1, textvariable=self.search_var).pack(side="left")

        # Create text box
        self.text_box = tk.Text(self.root)
        self.text_box.pack(fill="both", expand=True)

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                contacts = []
                for line in file:
                    name, phone_number, email = line.strip().split(",")
                    contacts.append(Contact(name, phone_number, email))
                return contacts
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number},{contact.email}\n")

    def add_contact(self):
        name = self.name_var.get()
        phone_number = self.phone_number_var.get()
        email = self.email_var.get()
        if name and phone_number and email:
            new_contact = Contact(name, phone_number, email)
            self.contacts.append(new_contact)
            self.save_contacts()
            self.name_var.set("")
            self.phone_number_var.set("")
            self.email_var.set("")
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def delete_contact(self):
        name = self.search_var.get()
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_contacts()
                self.search_var.set("")
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return
        messagebox.showerror("Error", "Contact not found!")

    def search_contact(self):
        name = self.search_var.get()
        for contact in self.contacts:
            if contact.name == name:
                self.text_box.delete(1.0, "end")
                self.text_box.insert("end", f"Name: {contact.name}\n")
                self.text_box.insert("end", f"Phone Number: {contact.phone_number}\n")
                self.text_box.insert("end", f"Email: {contact.email}\n")
                return
        messagebox.showerror("Error", "Contact not found!")

    def display_contacts(self):
        self.text_box.delete(1.0, "end")
        for i, contact in enumerate(self.contacts, start=1):
            self.text_box.insert("end", f"Contact {i}:\n")
            self.text_box.insert("end", f"Name: {contact.name}\n")
            self.text_box.insert("end", f"Phone Number: {contact.phone_number}\n")
            self.text_box.insert("end", f"Email: {contact.email}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Manager")
    contact_manager = ContactMaster(root)
    root.mainloop()