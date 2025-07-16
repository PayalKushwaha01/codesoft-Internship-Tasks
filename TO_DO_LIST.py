import tkinter as tk
from tkinter import messagebox, simpledialog

# Window setup
app = tk.Tk()
app.title("🎯 Payal's To-do List")
app.geometry("800x480")
app.config(bg="#e3306c")

tasks = []

# ===== Functions =====
def add_task():
    t = entry.get()
    if t:
        listbox.insert(tk.END, t)
        tasks.append(t)
        entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Oops", "Type something first!")

def delete_task():
    try:
        i = listbox.curselection()[0]
        listbox.delete(i)
        del tasks[i]
    except:
        messagebox.showinfo("Error", "Select a task to delete!")

def mark_done():
    try:
        i = listbox.curselection()[0]
        text = listbox.get(i)
        if "✔" not in text:
            listbox.delete(i)
            listbox.insert(i, "✔ " + text)
    except:
        messagebox.showinfo("Error", "Select a task!")

def edit_task():
    try:
        i = listbox.curselection()[0]
        current = listbox.get(i).replace("✔ ", "")
        new = simpledialog.askstring("Edit", "Update your task:", initialvalue=current)
        if new:
            listbox.delete(i)
            listbox.insert(i, new)
            tasks[i] = new
    except:
        messagebox.showinfo("Error", "Select a task to edit!")

def show_stats():
    total = listbox.size()
    done = sum(1 for i in listbox.get(0, tk.END) if "✔" in i)
    messagebox.showinfo("📊 Stats", f"Total: {total}\nDone: {done}")

# ===== UI =====
tk.Label(app, text="🌸 Payal's Daily Tasks" , font=("Arial", 18, "bold"), bg="#fff0f5", fg="#6a1b9a").pack(pady=10)

entry = tk.Entry(app, font=("Arial", 14), width=28)
entry.pack(pady=5)

tk.Button(app, text="➕ Add", command=add_task, bg="#ce93d8", fg="white", width=10).pack(pady=5)

listbox = tk.Listbox(app, font=("Arial", 14), width=32, height=10, bg="#fce4ec", selectbackground="#ba68c8")
listbox.pack(pady=10)

btns = tk.Frame(app, bg="#fff0f5")
btns.pack(pady=5)

tk.Button(btns, text="✔ Done", command=mark_done, bg="#0bf11a", width=10).grid(row=0, column=0, padx=5)
tk.Button(btns, text="✏ Edit", command=edit_task, bg="#d6e409", width=10).grid(row=0, column=1, padx=5)
tk.Button(btns, text="📊 Stats", command=show_stats, bg="#4dd0e1", width=10).grid(row=0, column=2, padx=5)

tk.Button(app, text="🗑 Delete", command=delete_task, bg="#c4413f", fg="white", width=20).pack(pady=10)

# Run app
app.mainloop()
