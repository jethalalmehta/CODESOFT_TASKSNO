import tkinter as tk
from tkinter import messagebox
import json
import os

# File for saving contacts
DATA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "contacts.json"
)

contacts = []
visible_indices = []

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x700")
root.configure(bg="light blue")

# Main heading
heading = tk.Label(
    root,
    text="My Contact Book",
    font=("Arial", 24, "bold"),
    bg="light blue"
)
heading.pack(pady=15)

# Contact form
form = tk.Frame(root, bg="light blue")
form.pack(pady=10)

# Name
tk.Label(form, text="Name:", bg="light blue").grid(
    row=0, column=0, padx=10, pady=5, sticky="w"
)
name_entry = tk.Entry(form, width=35)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Phone
tk.Label(form, text="Phone:", bg="light blue").grid(
    row=1, column=0, padx=10, pady=5, sticky="w"
)
phone_entry = tk.Entry(form, width=35)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Email
tk.Label(form, text="Email:", bg="light blue").grid(
    row=2, column=0, padx=10, pady=5, sticky="w"
)
email_entry = tk.Entry(form, width=35)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Address
tk.Label(form, text="Address:", bg="light blue").grid(
    row=3, column=0, padx=10, pady=5, sticky="w"
)
address_entry = tk.Entry(form, width=35)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Search area
search_frame = tk.Frame(root, bg="light blue")
search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="Search:",
    bg="light blue"
).pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame, width=25)
search_entry.pack(side=tk.LEFT, padx=5)

# Contact list
contact_list = tk.Listbox(
    root,
    width=65,
    height=12,
    font=("Arial", 11)
)


# Save contacts to JSON
def save_contacts():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


# Display contacts in the list
def refresh_contact_list(query=""):
    contact_list.delete(0, tk.END)
    visible_indices.clear()

    query = query.lower().strip()

    for index, contact in enumerate(contacts):
        name = contact["name"]
        phone = contact["phone"]

        if query == "" or query in name.lower() or query in phone.lower():
            visible_indices.append(index)
            contact_list.insert(tk.END, name + " - " + phone)


# Clear the input fields
def clear_form():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_list.selection_clear(0, tk.END)
    name_entry.focus_set()


# Add a new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter the name and phone number."
        )
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts()
    search_entry.delete(0, tk.END)
    refresh_contact_list()
    clear_form()

    messagebox.showinfo(
        "Success",
        "Contact added successfully!"
    )


# Select a contact to view or edit its details
def select_contact(event=None):
    selected = contact_list.curselection()

    if not selected:
        return

    index = visible_indices[selected[0]]
    contact = contacts[index]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact["name"])

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["phone"])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["email"])

    address_entry.delete(0, tk.END)
    address_entry.insert(0, contact["address"])


# Search by name or phone number
def search_contact():
    query = search_entry.get().strip()

    if query == "":
        messagebox.showwarning(
            "Search",
            "Please enter a name or phone number."
        )
        return

    refresh_contact_list(query)

    if not visible_indices:
        messagebox.showinfo(
            "Search",
            "No matching contact found."
        )


# Show the complete contact list
def show_all_contacts():
    search_entry.delete(0, tk.END)
    refresh_contact_list()


# Update a selected contact
def update_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Select Contact",
            "Please select a contact from the list first."
        )
        return

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Missing Information",
            "Name and phone number are required."
        )
        return

    index = visible_indices[selected[0]]

    contacts[index] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    save_contacts()
    search_entry.delete(0, tk.END)
    refresh_contact_list()
    clear_form()

    messagebox.showinfo(
        "Success",
        "Contact updated successfully!"
    )


# Delete a selected contact
def delete_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Select Contact",
            "Please select a contact to delete."
        )
        return

    index = visible_indices[selected[0]]
    name = contacts[index]["name"]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete " + name + "?"
    )

    if confirm:
        del contacts[index]
        save_contacts()
        search_entry.delete(0, tk.END)
        refresh_contact_list()
        clear_form()

        messagebox.showinfo(
            "Deleted",
            "Contact deleted successfully!"
        )


# Load previously saved contacts
def load_contacts():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            saved_contacts = json.load(file)

        if isinstance(saved_contacts, list):
            for contact in saved_contacts:
                if isinstance(contact, dict):
                    contacts.append({
                        "name": str(contact.get("name", "")),
                        "phone": str(contact.get("phone", "")),
                        "email": str(contact.get("email", "")),
                        "address": str(contact.get("address", ""))
                    })

    except FileNotFoundError:
        pass

    except (json.JSONDecodeError, OSError) as error:
        messagebox.showwarning(
            "Load Warning",
            "Could not load contacts:\n" + str(error)
        )

    refresh_contact_list()


# Buttons
button_frame = tk.Frame(root, bg="light blue")
button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="Add Contact",
    width=13,
    command=add_contact
).pack(side=tk.LEFT, padx=4)

tk.Button(
    button_frame,
    text="Update Contact",
    width=13,
    command=update_contact
).pack(side=tk.LEFT, padx=4)

tk.Button(
    button_frame,
    text="Delete Contact",
    width=13,
    command=delete_contact
).pack(side=tk.LEFT, padx=4)

tk.Button(
    button_frame,
    text="Clear Fields",
    width=13,
    command=clear_form
).pack(side=tk.LEFT, padx=4)

tk.Button(
    search_frame,
    text="Search",
    command=search_contact
).pack(side=tk.LEFT, padx=4)

tk.Button(
    search_frame,
    text="Show All",
    command=show_all_contacts
).pack(side=tk.LEFT, padx=4)

# Make clicking a contact fill in its details
contact_list.bind("<<ListboxSelect>>", select_contact)
contact_list.pack(pady=15)

# Load contacts and start the application
load_contacts()
name_entry.focus_set()
root.mainloop()