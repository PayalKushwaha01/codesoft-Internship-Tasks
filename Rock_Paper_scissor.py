import tkinter as tk
import random

# Game Choices
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}

# Scores
user_score = 0
comp_score = 0
history = []

def get_winner(user, comp):
    if user == comp:
        return "Tie"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "Payal"
    else:
        return "Computer"

def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)
    winner = get_winner(user_choice, comp_choice)

    if winner == "Payal":
        result_label.config(text="🎉 Payal Wins!", fg="#28a745")
        user_score += 1
    elif winner == "Computer":
        result_label.config(text="💻 Computer Wins!", fg="#dc3545")
        comp_score += 1
    else:
        result_label.config(text="😐 It's a Tie!", fg="#6c757d")

    user_choice_label.config(text=f"Payal: {emojis[user_choice]}")
    comp_choice_label.config(text=f"Computer: {emojis[comp_choice]}")
    score_label.config(text=f"Score - Payal: {user_score} | Computer: {comp_score}")

    history.append((user_choice, comp_choice, winner))
    update_history()

def update_history():
    for widget in history_frame.winfo_children():
        widget.destroy()

    # Table Headers
    headers = ["Payal's Move", "Computer's Move", "Winner"]
    for col, title in enumerate(headers):
        tk.Label(history_frame, text=title, width=15, font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=0, column=col)

    # Last 10 moves
    for i, (u, c, w) in enumerate(reversed(history[-10:]), start=1):
        tk.Label(history_frame, text=u, width=15, bg="white").grid(row=i, column=0)
        tk.Label(history_frame, text=c, width=15, bg="white").grid(row=i, column=1)
        tk.Label(history_frame, text=w, width=15, bg="white").grid(row=i, column=2)

# GUI
win = tk.Tk()
win.title("Payal's Rock Paper Scissors 🎮")
win.geometry("520x680")
win.config(bg="#fce4ec")  # Light pink

# Title
tk.Label(win, text="✊✋✌️ Rock Paper Scissors ✌️✋✊", font=("Helvetica", 18, "bold"), bg="#ba68c8", fg="white").pack(fill=tk.X, pady=10)

# Score & result
score_label = tk.Label(win, text="Score - Payal: 0 | Computer: 0", font=("Arial", 14), bg="#fce4ec")
score_label.pack(pady=5)

result_label = tk.Label(win, text="", font=("Arial", 16, "italic"), bg="#fce4ec")
result_label.pack(pady=5)

user_choice_label = tk.Label(win, text="Payal: ", font=("Arial", 20), bg="#fce4ec")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(win, text="Computer: ", font=("Arial", 20), bg="#fce4ec")
comp_choice_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(win, bg="#fce4ec")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Rock", font=("Arial", 12), width=12, bg="#ce93d8", command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper", font=("Arial", 12), width=12, bg="#ce93d8", command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissors", font=("Arial", 12), width=12, bg="#ce93d8", command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# History
tk.Label(win, text="📝 Match History (Last 10)", font=("Arial", 14, "bold"), bg="#fce4ec").pack(pady=10)
history_frame = tk.Frame(win, bg="#fce4ec")
history_frame.pack()

win.mainloop()
