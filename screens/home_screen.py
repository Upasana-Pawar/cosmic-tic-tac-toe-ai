import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class HomeScreen:

    def __init__(self, root):

        self.root = root

        self.root.configure(bg="#081229")

        self.load_assets()

        self.create_ui()

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()

    def load_assets(self):

        try:

            banner = Image.open(
                "assets/banner.png"
            )

            banner = banner.resize(
                (750, 250)
            )

            self.banner_image = (
                ImageTk.PhotoImage(banner)
            )

        except:

            self.banner_image = None

    def create_ui(self):

        self.clear_window()

        main_frame = tk.Frame(
            self.root,
            bg="#081229"
        )

        main_frame.pack(
            fill="both",
            expand=True
        )

        # Banner

        if self.banner_image:

            tk.Label(

                main_frame,

                image=self.banner_image,

                bg="#081229"

            ).pack(
                pady=20
            )

        else:

            tk.Label(

                main_frame,

                text="🚀 COSMIC TIC-TAC-TOE AI",

                font=(
                    "Arial",
                    30,
                    "bold"
                ),

                fg="cyan",

                bg="#081229"

            ).pack(
                pady=40
            )

        # Subtitle

        tk.Label(

            main_frame,

            text=(
                "Human Commander vs Alien Intelligence"
            ),

            font=(
                "Arial",
                16
            ),

            fg="white",

            bg="#081229"

        ).pack(
            pady=10
        )

        # Buttons

        tk.Button(

            main_frame,

            text="🚀 Start Mission",

            font=(
                "Arial",
                14,
                "bold"
            ),

            width=25,

            height=2,

            command=self.start_game

        ).pack(
            pady=10
        )

        tk.Button(

            main_frame,

            text="🏆 Leaderboard",

            font=(
                "Arial",
                14
            ),

            width=25,

            height=2,

            command=self.show_leaderboard

        ).pack(
            pady=10
        )

        tk.Button(

            main_frame,

            text="🎖 Achievements",

            font=(
                "Arial",
                14
            ),

            width=25,

            height=2,

            command=self.show_achievements

        ).pack(
            pady=10
        )

        tk.Button(

            main_frame,

            text="❌ Exit",

            font=(
                "Arial",
                14
            ),

            width=25,

            height=2,

            command=self.root.destroy

        ).pack(
            pady=10
        )

        # Footer

        tk.Label(

            main_frame,

            text=(
                "Powered by Minimax + Alpha-Beta Pruning"
            ),

            font=(
                "Arial",
                10
            ),

            fg="gray",

            bg="#081229"

        ).pack(
            side="bottom",
            pady=20
        )

    def start_game(self):
        from screens.game_screen import GameScreen

        self.clear_window()

        GameScreen(self.root)

    def show_leaderboard(self):

        from leaderboard import LeaderboardScreen 

        self.clear_window()

        LeaderboardScreen(self.root)

    def show_achievements(self):

        from achievements import AchievementsScreen

        self.clear_window()

        AchievementsScreen(self.root)
        