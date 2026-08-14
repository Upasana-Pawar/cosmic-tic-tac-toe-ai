import tkinter as tk
from PIL import Image, ImageTk
import random

from game import Game
from ai import AI
from screens.result_screen import ResultScreen



WINDOW_BG = "#081229"
BOARD_BG = "#142850"


class GameScreen:

    def __init__(self, root):

        self.root = root

        self.game = Game()
        self.ai = AI()

        self.buttons = []

        self.player_moves = 0
        self.ai_moves = 0

        self.difficulty = tk.StringVar(
            value="Impossible"
        )

        self.load_assets()

        self.create_ui()

    # -------------------------------------------------

    def load_assets(self):

        # Astronaut

        try:

            img = Image.open(
                "assets/astronaut_avatar.png"
            )

            img = img.resize((120, 120))

            self.astronaut_photo = (
                ImageTk.PhotoImage(img)
            )

        except:

            self.astronaut_photo = None

        # Alien

        try:

            img = Image.open(
                "assets/alien_avatar.png"
            )

            img = img.resize((120, 120))

            self.alien_photo = (
                ImageTk.PhotoImage(img)
            )

        except:

            self.alien_photo = None

        # X Icon

        try:

            img = Image.open(
                "assets/x_icon.png"
            )

            img = img.resize((60, 60))

            self.x_photo = (
                ImageTk.PhotoImage(img)
            )

        except:

            self.x_photo = None

        # O Icon

        try:

            img = Image.open(
                "assets/o_icon.png"
            )

            img = img.resize((60, 60))

            self.o_photo = (
                ImageTk.PhotoImage(img)
            )

        except:

            self.o_photo = None

    # -------------------------------------------------

    def create_ui(self):

        self.root.configure(
            bg=WINDOW_BG
        )

        self.clear_window()

        title = tk.Label(

            self.root,

            text="🚀 COSMIC TIC-TAC-TOE AI",

            font=("Arial", 22, "bold"),

            fg="cyan",

            bg=WINDOW_BG
        )

        title.pack(
            pady=10
        )

        # Difficulty

        difficulty_frame = tk.Frame(
            self.root,
            bg=WINDOW_BG
        )

        difficulty_frame.pack()

        tk.Label(

            difficulty_frame,

            text="Difficulty:",

            fg="white",

            bg=WINDOW_BG

        ).pack(
            side=tk.LEFT
        )

        tk.OptionMenu(

            difficulty_frame,

            self.difficulty,

            "Easy",

            "Medium",

            "Impossible"

        ).pack(
            side=tk.LEFT
        )

        # Avatar Section

        top_frame = tk.Frame(
            self.root,
            bg=WINDOW_BG
        )

        top_frame.pack(
            pady=20
        )

        # Commander

        commander = tk.Frame(
            top_frame,
            bg=WINDOW_BG
        )

        commander.pack(
            side=tk.LEFT,
            padx=50
        )

        if self.astronaut_photo:

            tk.Label(

                commander,

                image=self.astronaut_photo,

                bg=WINDOW_BG

            ).pack()

        tk.Label(

            commander,

            text="👩‍🚀 Commander",

            fg="cyan",

            bg=WINDOW_BG,

            font=("Arial", 14, "bold")

        ).pack()

        # Alien

        alien = tk.Frame(
            top_frame,
            bg=WINDOW_BG
        )

        alien.pack(
            side=tk.RIGHT,
            padx=50
        )

        if self.alien_photo:

            tk.Label(

                alien,

                image=self.alien_photo,

                bg=WINDOW_BG

            ).pack()

        tk.Label(

            alien,

            text="👽 Alien AI",

            fg="magenta",

            bg=WINDOW_BG,

            font=("Arial", 14, "bold")

        ).pack()

        # Status

        self.status_label = tk.Label(

            self.root,

            text="Mission Started 🚀",

            fg="white",

            bg=WINDOW_BG,

            font=("Arial", 14)

        )

        self.status_label.pack(
            pady=10
        )

        # Analytics

        self.analytics_label = tk.Label(

            self.root,

            text="Player Moves: 0 | AI Moves: 0",

            fg="gold",

            bg=WINDOW_BG,

            font=("Arial", 12)

        )

        self.analytics_label.pack(
            pady=5
        )

        # Board

        board_container = tk.Frame(
            self.root,
            bg=WINDOW_BG
        )
        board_container.pack(pady=20)

        board_frame = tk.Frame(
            board_container,
            bg=WINDOW_BG
        )
        board_frame.pack()

        for i in range(9):

            btn = tk.Button(
                board_frame,
                width=4,
                height=2,
                font=("Arial", 24, "bold"),
                bg=BOARD_BG,
                fg="white",
                relief="raised",
                bd=3,
                activebackground="#1f4068",
                command=lambda i=i: self.player_move(i)
            )

            btn.grid(
                row=i // 3,
                column=i % 3,
                padx=8,
                pady=8
            )

            self.buttons.append(btn)

        # Controls

        tk.Button(
            self.root,
            text="🔄 New Game",
            width=20,
            command=self.restart_game
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="🏠 Home",
            width=20,
            command=self.go_home
        ).pack(pady=5)

        # Controls

        tk.Button(

            self.root,

            text="🔄 New Game",

            width=20,

            command=self.restart_game

        ).pack(
            pady=5
        )

        tk.Button(

            self.root,

            text="🏠 Home",

            width=20,

            command=self.go_home

        ).pack(
            pady=5
        )

    # -------------------------------------------------

    def player_move(self, position):

        if not self.game.make_move(
            position,
            "X"
        ):
            return

        self.player_moves += 1

        self.update_board()

        if self.game.winner():

            self.show_result(
                "🏆 MISSION SUCCESS"
            )

            return

        if self.game.is_draw():

            self.show_result(
                "🤝 STALEMATE"
            )

            return

        self.status_label.config(
            text="🤖 AI Thinking..."
        )

        self.root.after(
            800,
            self.ai_move
        )

    # -------------------------------------------------
    
    def ai_move(self):

        difficulty = self.difficulty.get()

        if difficulty == "Easy":
            move = random.choice(self.game.available_moves())

        elif difficulty == "Medium":
            if random.random() < 0.5:
                move = random.choice(self.game.available_moves())
            else:
                move = self.ai.get_best_move(self.game.board)

        else:
            move = self.ai.get_best_move(self.game.board)

        self.game.make_move(move, "O")

        self.ai_moves += 1

        self.update_board()

    # -------------------------------------------------

    def update_board(self):

        print("BOARD:", self.game.board)

        for i in range(9):

            symbol = self.game.board[i]

            if symbol == "X":

                self.buttons[i].config(
                    text="X",
                    fg="cyan"
                )

            elif symbol == "O":

                self.buttons[i].config(
                    text="O",
                    fg="magenta"
                )

            else:

                self.buttons[i].config(
                    text=""
                )

        self.analytics_label.config(
            text=f"Player Moves: {self.player_moves} | AI Moves: {self.ai_moves}"
        )
    # -------------------------------------------------
    # -------------------------------------------------

    # -------------------------------------------------

    def show_result(self, result):

        analytics = f"""
            Commander Report

            Player Moves: {self.player_moves}
            AI Moves: {self.ai_moves}

        Difficulty:
        {self.difficulty.get()}
    """

        ResultScreen(
        self.root,
        result,
        analytics,
        self.restart_game,
        self.go_home
    )

    def restart_game(self):

        self.clear_window()

        GameScreen(
            self.root
        )

    # -------------------------------------------------

    def go_home(self):

        from screens.home_screen import HomeScreen

        self.clear_window()

        HomeScreen(
            self.root
        )

    # -------------------------------------------------

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()