import tkinter as tk
from tkinter import ttk

contacts = []

window = tk.Tk()
window.title("Contact Book")
window.geometry("850x520")
window.config(bg="#eaffea")  

# === Header ===
tk.Label(window, text="📒 Contact Book", font=("Verdana", 22, "bold"),
         bg="#5cb85c", fg="white", pady=10).pack(fill="x")

# === Form Frame ===
form_frame = tk.Frame(window, bg="white", bd=2, relief="groove")
form_frame.place(x=30, y=70, width=380, height=250)

# === Input Fields ===
tk.Label(form_frame, text="Name", bg="white", font=("Arial", 11)).place(x=20, y=20)
name_entry = tk.Entry(form_frame, width=28, font=("Arial", 10), bd=2, relief="ridge")
name_entry.place(x=130, y=20)

tk.Label(form_frame, text="Email", bg="white", font=("Arial", 11)).place(x=20, y=60)
email_entry = tk.Entry(form_frame, width=28, font=("Arial", 10), bd=2, relief="ridge")
email_entry.place(x=130, y=60)

tk.Label(form_frame, text="Mobile", bg="white", font=("Arial", 11)).place(x=20, y=100)
mobile_entry = tk.Entry(form_frame, width=28, font=("Arial", 10), bd=2, relief="ridge")
mobile_entry.place(x=130, y=100)

tk.Label(form_frame, text="Gender", bg="white", font=("Arial", 11)).place(x=20, y=140)
gender_box = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], state="readonly", width=25)
gender_box.place(x=130, y=140)

# === Functions ===
def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    gender_box.set("")

def save_contact(update=False):
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    gender = gender_box.get()

    if name and email and mobile and gender:
        info = [name, email, mobile, gender]
        if update and contact_table.selection():
            index = contact_table.index(contact_table.selection()[0])
            contacts[index] = info
        else:
            contacts.append(info)
        display_all()
        clear_fields()

def delete_contact():
    selected = contact_table.selection()
    if selected:
        index = contact_table.index(selected[0])
        del contacts[index]
        display_all()
        clear_fields()

def display_all():
    contact_table.delete(*contact_table.get_children())
    for contact in contacts:
        contact_table.insert('', 'end', values=contact)

def fill_row(event):
    selected = contact_table.selection()
    if selected:
        data = contact_table.item(selected[0], 'values')
        name_entry.delete(0, tk.END)
        name_entry.insert(0, data[0])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, data[1])
        mobile_entry.delete(0, tk.END)
        mobile_entry.insert(0, data[2])
        gender_box.set(data[3])

# === Buttons ===
btn_style = {"width": 10, "font": ("Arial", 10, "bold"), "bd": 1}

tk.Button(form_frame, text="Save", bg="#5bc0de", fg="white",
          command=lambda: save_contact(True), **btn_style).place(x=30, y=190)
tk.Button(form_frame, text="Delete", bg="#f0ad4e", fg="white",
          command=delete_contact, **btn_style).place(x=140, y=190)
tk.Button(form_frame, text="Clear", bg="#d9534f", fg="white",
          command=clear_fields, **btn_style).place(x=250, y=190)

# === Search Section ===
tk.Label(window, text="🔍 Search by Name", bg="#eaffea", font=("Arial", 11)).place(x=450, y=80)
search_entry = tk.Entry(window, width=20, font=("Arial", 10), bd=2, relief="ridge")
search_entry.place(x=600, y=80)

def search_contact():
    name = search_entry.get().lower()
    contact_table.delete(*contact_table.get_children())
    for contact in contacts:
        if name in contact[0].lower():
            contact_table.insert('', 'end', values=contact)

tk.Button(window, text="Search", bg="#0275d8", fg="white", width=10,
          command=search_contact).place(x=600, y=110)
tk.Button(window, text="Show All", bg="#5cb85c", fg="white", width=10,
          command=display_all).place(x=700, y=110)

# === Table ===
cols = ["Name", "Email", "Mobile", "Gender"]
contact_table = ttk.Treeview(window, columns=cols, show='headings')
for col in cols:
    contact_table.heading(col, text=col)
    contact_table.column(col, width=180, anchor="center")

contact_table.place(x=30, y=340, width=790, height=150)
contact_table.bind("<ButtonRelease-1>", fill_row)

# === Footer ===
tk.Label(window, text="💡 Made with ❤️ by Payal for CodeSoft Internship",
         bg="#5cb85c", fg="white", font=("Arial", 10)).pack(side="bottom", fill="x")

window.mainloop()
