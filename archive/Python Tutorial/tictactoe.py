class TicTacToe:
    """Represents a Tic Tac Toe game"""

    def __init__(self):
        """Initializes a new instance of a Tic Tac Toe Game"""
        self.board = []
        self.game_started = False

        self.start_game()

    def start_game(self):
        """Starts a Tic Tac Toe game (Resets the board)"""
        self.board = [x for x in range(1, 10)]
        self.game_started = True

    def move(self, position: int) -> str:
        """Place a marker on an empty spot

        Returns:
            str -- "X" for x win,
                   "O" for o win,
                   "T" for tie,
                   "" for no win
        """
        if not self.game_started:
            raise Exception("Game has ended!")

        if (self.board[position] != "X" and self.board[position] != "O"):
            self.board[position] = self.next_to_move()
        else:
            pass

        win_result = self.check_for_win()
        if win_result != "":
            self.game_started = False
        return win_result

    def next_to_move(self) -> str:
        return "O" if self.board.count("X") > self.board.count("O") else "X"

    def check_for_win(self) -> str:
        """Check if the game is won yet

        Returns:
            str -- "X" for x win,
                   "O" for o win,
                   "T" for tie,
                   "" for no win
        """
        for i in range(3):
            # Check rows
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2]:
                return self.board[i*3]
            # Check columns
            if self.board[i] == self.board[3+i] == self.board[6+i]:
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] or \
                self.board[2] == self.board[4] == self.board[6]:
            return self.board[4]
        if self.board.count("X") + self.board.count("O") == 9:
            return "T"
        return ""

    def print_board(self):
        """Prints the current state of the board"""
        for i in range(9):
            print(" {} ".format(self.board[i]), end="")
            if i == 8:
                print()
            elif i % 3 == 2:
                print("\n-----------")
            else:
                print("|", end="")

    @staticmethod
    def play_a_game(ai_level: int):
        """Starts and plays a new game of TicTacToe.
        Returns when a player wins. Quick and dirty!

        Arguments:
            ai_level {int} -- level of ai playing, from 1-3. 0 means no AI
        """
        t = TicTacToe()
        t.start_game()
        while True:
            t.print_board()
            result = ""
            while True:
                try:
                    input_text = t.next_to_move() + " to move\n> "
                    result = t.move(int(input(input_text))-1)
                    break
                except ValueError:
                    continue
            if result != "":
                t.print_board()
                d = {"X": "X wins!", "O": "O wins!", "T": "It's a tie!"}
                print("The game has ended\n{}".format(d[result]))
                break

    @staticmethod
    def ai_move(t, ai_level: int) -> int:
        """Make a move as an AI

        Arguments:
            t {TicTacToe} -- the TicTacToe game
            ai_level {int} -- level of ai playing
        Returns:
            int -- Which square the AI wishes to move to
        """


if __name__ == "__main__":
    TicTacToe.play_a_game(0)
