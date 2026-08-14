import tkinter as tk


WINDOW_BG = "#081229"


class ResultScreen:

    def __init__(
        self,
        root,
        result,
        analytics,
        play_again_callback,
        home_callback
    ):

        self.root = root

        self.result = result

        self.analytics = analytics

        self.play_again_callback = (
            play_again_callback
        )

        self.home_callback = (
            home_callback
        )

        self.create_ui()

    # -----------------------------------

    def create_ui(self):

        self.clear_window()

        self.root.configure(
            bg=WINDOW_BG
        )

        # Determine styling

        if "SUCCESS" in self.result:

            icon = "🏆"
            color = "#FFD700"

        elif "WINS" in self.result:

            icon = "👽"
            color = "#FF4D4D"

        else:

            icon = "🤝"
            color = "#00FFFF"

        # Title

        title = tk.Label(

            self.root,

            text=f"{icon} {self.result}",

            font=(
                "Arial",
                28,
                "bold"
            ),

            fg=color,

            bg=WINDOW_BG

        )

        title.pack(
            pady=40
        )

        # Mission Report Frame

        report_frame = tk.LabelFrame(

            self.root,

            text="Mission Report",

            font=(
                "Arial",
                12,
                "bold"
            ),

            fg="cyan",

            bg=WINDOW_BG,

            padx=20,

            pady=20

        )

        report_frame.pack(
            pady=20
        )

        report_label = tk.Label(

            report_frame,

            text=self.analytics,

            justify="left",

            font=(
                "Consolas",
                12
            ),

            fg="white",

            bg=WINDOW_BG

        )

        report_label.pack()

        # Action Buttons

        button_frame = tk.Frame(
            self.root,
            bg=WINDOW_BG
        )

        button_frame.pack(
            pady=30
        )

        play_again_btn = tk.Button(

            button_frame,

            text="🔄 Play Again",

            width=20,

            height=2,

            font=(
                "Arial",
                12,
                "bold"
            ),

            command=self.play_again_callback

        )

        play_again_btn.grid(
            row=0,
            column=0,
            padx=10
        )

        home_btn = tk.Button(

            button_frame,

            text="🏠 Home",

            width=20,

            height=2,

            font=(
                "Arial",
                12,
                "bold"
            ),

            command=self.home_callback

        )

        home_btn.grid(
            row=0,
            column=1,
            padx=10
        )

        # Footer

        footer = tk.Label(

            self.root,

            text="Cosmic Tic-Tac-Toe AI | Internship Project",

            fg="gray",

            bg=WINDOW_BG,

            font=(
                "Arial",
                10
            )

        )

        footer.pack(
            side="bottom",
            pady=20
        )

    # -----------------------------------

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()