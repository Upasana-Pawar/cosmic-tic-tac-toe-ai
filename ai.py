class AI:

    def __init__(self):
        self.ai_player = "O"
        self.human_player = "X"

    def get_best_move(self, board):

        best_score = float("-inf")
        best_move = None

        for move in self.available_moves(board):

            board[move] = self.ai_player

            score = self.minimax(
                board,
                False
            )

            board[move] = ""

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, is_maximizing):

        winner = self.check_winner(board)

        if winner == self.ai_player:
            return 1

        if winner == self.human_player:
            return -1

        if self.is_draw(board):
            return 0

        if is_maximizing:

            best_score = float("-inf")

            for move in self.available_moves(board):

                board[move] = self.ai_player

                score = self.minimax(
                    board,
                    False
                )

                board[move] = ""

                best_score = max(
                    best_score,
                    score
                )

            return best_score

        else:

            best_score = float("inf")

            for move in self.available_moves(board):

                board[move] = self.human_player

                score = self.minimax(
                    board,
                    True
                )

                board[move] = ""

                best_score = min(
                    best_score,
                    score
                )

            return best_score

    def available_moves(self, board):

        return [
            i
            for i in range(9)
            if board[i] == ""
        ]

    def is_draw(self, board):

        return (
            "" not in board
            and self.check_winner(board) is None
        )

    def check_winner(self, board):

        wins = [

            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),

            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),

            (0, 4, 8),
            (2, 4, 6)

        ]

        for a, b, c in wins:

            if (
                board[a] != ""
                and board[a] == board[b] == board[c]
            ):
                return board[a]

        return None