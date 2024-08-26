import random
import difflib
import os
import json
from tkinter import Tk, StringVar, Label, Entry, Button
from tkinter import messagebox
from tkinter import ttk

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
HIGH_SCORE_FILE = os.path.join(current_dir, "high_score.json")

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Tkinter Quiz Game")
        self.root.configure(bg='#1E1E1E')  # Dark background color
        self.score = 0
        self.tries = 0
        self.players = [
            ["Lionel Messi", "Argentinian footballer", "Plays for Inter Miami", "7-time Ballon d'Or winner", 36],
            ["Cristiano Ronaldo", "Portuguese footballer", "Plays for Al Nassr", "5-time Ballon d'Or winner", 39],
            ["Kylian Mbappe", "French footballer", "Plays for PSG", "2018 World Cup winner", 25],
            ["Erling Haaland", "Norwegian footballer", "Plays for Manchester City", "Top scorer of the Premier League 2023-2024", 24],
            ["Kevin De Bruyne", "Belgian footballer", "Plays for Manchester City", "Considered one of the best midfielders", 32],
            ["Karim Benzema", "French footballer", "Plays for Al-Ittihad", "2022 Ballon d'Or winner", 36],
            ["Robert Lewandowski", "Polish footballer", "Plays for FC Barcelona", "Best FIFA Men's Player 2020", 36],
            ["Neymar Jr", "Brazilian footballer", "Plays for Al Hilal", "Skillful winger and playmaker", 32]
        ]
        self.current_player = None
        self.hints_used = []
        self.hints = []
        self.help_used = False

        self.player_name_var = StringVar()
        self.hint_var = StringVar()
        self.tries_var = StringVar()
        self.score_var = StringVar()
        self.high_score_var = StringVar()
        self.age_var = StringVar()

        self.load_high_score()
        self.setup_ui()
        self.new_game()

    def setup_ui(self):
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', background='#333333', foreground='black', padding=6, font=('Arial', 12))
        style.configure('TLabel', background='#1E1E1E', foreground='white', font=('Arial', 12))
        style.configure('TEntry', background='#333333', foreground='white', padding=5)

        # Labels for high score, score, and tries
        Label(self.root, text="High Score:", bg='#1E1E1E', fg='white').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.high_score_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=0, column=1, padx=10, pady=10)

        Label(self.root, text="Score:", bg='#1E1E1E', fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.score_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=1, column=1, padx=10, pady=10)

        Label(self.root, text="Tries:", bg='#1E1E1E', fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.tries_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=2, column=1, padx=10, pady=10)

        Label(self.root, text="Age:", bg='#1E1E1E', fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.age_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=3, column=1, padx=10, pady=10)

        # Labels for hints
        Label(self.root, text="Hint:", bg='#1E1E1E', fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.hint_label = Label(self.root, text="", bg='#1E1E1E', fg='white', font=('Arial', 12))
        self.hint_label.grid(row=4, column=1, padx=10, pady=10)

        Label(self.root, text="Player Guess:", bg='#1E1E1E', fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.player_guess_entry = Entry(self.root, textvariable=self.player_name_var, bg='#333333', fg='white')
        self.player_guess_entry.grid(row=5, column=1, padx=10, pady=10)
        self.player_guess_entry.bind("<Return>", self.submit_answer_event)

        # Buttons
        ttk.Button(self.root, text="Submit Answer", command=self.submit_answer).grid(row=6, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Hint", command=self.provide_hint).grid(row=6, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Help", command=self.provide_help).grid(row=7, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="New Game", command=self.new_game).grid(row=7, column=1, padx=10, pady=10)

        # Message label for game status
        self.status_label = Label(self.root, text="", bg='#1E1E1E', fg='white', font=('Arial', 14))
        self.status_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def submit_answer_event(self, event):
        self.submit_answer()

    def similarity_score(self, a, b):
        return difflib.SequenceMatcher(None, a, b).ratio()

    def get_random_hints(self, player):
        hint1 = player[1]
        hint2 = random.choice(player[2:])
        while hint1 == hint2:
            hint2 = random.choice(player[2:])
        return [hint1, hint2]

    def get_third_hint(self, player):
        remaining_hints = [hint for hint in player[2:] if hint not in self.hints_used]
        return random.choice(remaining_hints) if remaining_hints else None

    def new_game(self):
        self.current_player = random.choice(self.players)
        self.hints_used = []
        self.hints = self.get_random_hints(self.current_player)
        self.help_used = False

        self.age_var.set(f"Age: {self.current_player[4]}")
        self.hint_label.config(text="")  # Clear hint label
        self.player_name_var.set("")
        self.update_ui()

    def submit_answer(self):
        player_name = self.current_player[0]
        user_answer = self.player_name_var.get().strip()

        if self.similarity_score(user_answer, player_name) >= 0.7:
            if self.help_used:
                self.score += 2  # Increase score by 2 points if help was used
            else:
                points = 5 if self.tries == 0 else (4 if not self.hint_label.cget("text") else 3)
                self.score += points
            self.status_label.config(text=f"Correct! It's {player_name}!\nYou earned {self.score} points.")
        else:
            self.score -= 1
            self.status_label.config(text=f"Incorrect. The correct answer is: {player_name}")

        self.tries += 1
        self.update_ui()
        self.new_game()

    def provide_hint(self):
        if self.hints:
            next_hint = self.hints.pop(0)
            self.hint_label.config(text=next_hint)
            self.hints_used.append(next_hint)
        else:
            messagebox.showinfo("Hint", "No more hints available!")

    def provide_help(self):
        self.help_used = True
        self.player_name_var.set(f"{self.current_player[0].split()[0]} ")

    def update_ui(self):
        self.score_var.set(f"Score: {self.score}")
        self.tries_var.set(f"Tries: {self.tries}")
        self.high_score_var.set(f"High Score: {self.high_score}")

    def load_high_score(self):
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as file:
                data = json.load(file)
                self.high_score = data.get("score", 0)
                self.high_score_tries = data.get("tries", 0)
        else:
            self.high_score = 0
            self.high_score_tries = 0

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_tries = self.tries
            with open(HIGH_SCORE_FILE, "w") as file:
                json.dump({"score": self.high_score, "tries": self.high_score_tries}, file)

if __name__ == "__main__":
    root = Tk()
    game = QuizGame(root)
    root.mainloop()
