import tkinter as tk
from screens.home_screen import HomeScreen


def main():

    root = tk.Tk()

    root.title("Cosmic Tic-Tac-Toe AI")

    root.geometry("1200x800")

    try:
        root.state("zoomed")
    except:
        pass

    HomeScreen(root)

    root.mainloop()


if __name__ == "__main__":
    main()


