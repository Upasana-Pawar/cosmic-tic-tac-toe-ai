import random


class Game:

    def __init__(self):

        self.board = [""] * 9

    def reset(self):

        self.board = [""] * 9

    def available_moves(self):

        return [

            i

            for i in range(9)

            if self.board[i] == ""
        ]

    def make_move(
        self,
        position,
        symbol
    ):

        if self.board[position] == "":

            self.board[position] = symbol

            return True

        return False

    def winner(self):

        patterns = [

            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            [0, 4, 8],
            [2, 4, 6]
        ]

        for pattern in patterns:

            a, b, c = pattern

            if (
                self.board[a] != ""
                and self.board[a]
                == self.board[b]
                == self.board[c]
            ):
                return self.board[a]

        return None

    def is_draw(self):

        return (
            "" not in self.board
            and self.winner() is None
        )

    def random_move(self):

        return random.choice(
            self.available_moves()
        )
    