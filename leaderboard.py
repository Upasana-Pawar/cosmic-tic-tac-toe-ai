import tkinter as tk
import json
import os

LEADERBOARD_FILE = "data/leaderboard.json"


class LeaderboardScreen:

    def __init__(self, root):

        self.root = root

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, "w") as f:
                json.dump({"players": {}}, f, indent=4)

        self.window = tk.Toplevel(root)
        self.window.title("Galactic Leaderboard")
        self.window.geometry("400x400")

        tk.Label(
            self.window,
            text="🏆 Galactic Leaderboard",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        top_players = self.get_top_players()

        if not top_players:
            tk.Label(
                self.window,
                text="No players recorded yet."
            ).pack(pady=20)
        else:
            for i, (name, wins) in enumerate(top_players[:10], start=1):
                tk.Label(
                    self.window,
                    text=f"{i}. {name} - {wins} wins",
                    font=("Arial", 12)
                ).pack(anchor="w", padx=20)

    def load(self):

        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def register_player(self, player_name):

        data = self.load()

        if player_name not in data["players"]:
            data["players"][player_name] = {
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "games": 0
            }

            self.save(data)

    def record_result(self, player_name, result):

        data = self.load()

        if player_name not in data["players"]:
            self.register_player(player_name)
            data = self.load()

        player = data["players"][player_name]

        player["games"] += 1

        if result == "win":
            player["wins"] += 1

        elif result == "loss":
            player["losses"] += 1

        elif result == "draw":
            player["draws"] += 1

        self.save(data)

    def get_stats(self, player_name):

        data = self.load()

        return data["players"].get(player_name)

    def get_top_players(self):

        data = self.load()

        players = []

        for name, stats in data["players"].items():
            players.append(
                (name, stats["wins"])
            )

        return sorted(
            players,
            key=lambda x: x[1],
            reverse=True
        )