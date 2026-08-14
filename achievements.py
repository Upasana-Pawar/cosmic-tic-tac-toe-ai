import tkinter as tk
import json
import os

ACHIEVEMENT_FILE = "data/achievements.json"


class AchievementsScreen:

    def __init__(self, root):

        self.root = root

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(ACHIEVEMENT_FILE):
            with open(ACHIEVEMENT_FILE, "w") as f:
                json.dump({"players": {}}, f, indent=4)

        self.window = tk.Toplevel(root)
        self.window.title("Achievements")
        self.window.geometry("400x400")

        tk.Label(
            self.window,
            text="🏅 Achievements",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Label(
            self.window,
            text="Achievement system ready."
        ).pack()

    def load(self):
        with open(ACHIEVEMENT_FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(ACHIEVEMENT_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def register_player(self, player_name):
        data = self.load()

        if player_name not in data["players"]:
            data["players"][player_name] = []
            self.save(data)

    def unlock(self, player_name, achievement):
        data = self.load()

        if achievement not in data["players"][player_name]:
            data["players"][player_name].append(achievement)
            self.save(data)

    def get_player_achievements(self, player_name):
        data = self.load()
        return data["players"].get(player_name, [])