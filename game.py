from datetime import datetime

class Player:
    """ADD DOCSTRING"""

    def __init__(self, name, char):
        """ADD DOCSTRING"""
        
        self.name = name
        self.char = char


class Move:
    """ADD DOCSTRING"""
    
    def __init__(self, player, position):
        """ADD DOCSTRING"""
        
        self.player = player
        self.position = position


class Board:
    """ADD DOCSTRING"""
    
    def __init__(self):
        """ADD DOCSTRING"""

        self.current_board = [["-","-","-"],
                              ["-","-","-"],
                              ["-","-","-"]]
        self.last_move = None

    def display(self):
        """ADD DOCSTRING"""
        
        for line in self.current_board:
            print(" ".join(line))

    def add_move(self, move):
        """ADD DOCSTRING"""
   
        self.current_board[move.position[0]][move.position[1]] = move.player.char

    def is_full(self):
        """ADD DOCSTRING"""

        current_board = self.current_board
        remaining_rows = 0

        for row in current_board:
            if "-"  in row:
                remaining_rows += 1

        if remaining_rows == 0:
            return True
        else:
            return False

    def is_winning(self):
        """ADD DOCSTRING"""

        current_board = self.current_board

        # check rows
        for row in current_board:
            if ("X" not in row and "-" not in row) or ("O" not in row and "-" not in row):
                return True

        # check columns
        for i in range(len(current_board)):
            column_to_check = set()
            
            for j in range(len(current_board)):
                column_to_check.add(current_board[j][i])

            if ("X" not in column_to_check and "-" not in column_to_check) or ("O" not in column_to_check and "-" not in column_to_check):
                return True
        
        # check diagonals
        forward_diagonal_check = set()
        backward_diagonal_check = set()
        
        for i in range(len(current_board)):
            forward_diagonal_check.add(current_board[i][i])
            backward_diagonal_check.add(current_board[i][len(current_board)-1-i])

        if forward_diagonal_check == {"X"} or forward_diagonal_check == {"O"}:
            return True

        if backward_diagonal_check == {"X"} or backward_diagonal_check == {"O"}:
            return True


class Game:
    """ADD DOCSTRING"""
    
    def __init__(self, board, player_1, player_2):
        """ADD DOCSTRING"""

        self.board = board
        self.player1 = player_1
        self.player2 = player_2
        self.started_at = datetime.now().time()
        self.finished_at = None
    

def create_players():
    """ADD DOCSTRING"""

    char_pairings = {"X":"O","O":"X"}

    # Create player1
    name_1 = input("Player 1, what is your name? > ")
    char_1 = ""
    
    # Force player to choose valid input
    while char_1 not in char_pairings:
        char_1 = input("Would you like to be X or O? > ").upper()
    player_1 = Player(name_1, char_1)

    # Create player2
    name_2 = input("Player 2, what is your name? > ")

    print("{}, you are {}.".format(name_2, char_pairings[char_1]))
    char_2 = char_pairings[char_1]

    player_2 = Player(name_2, char_2)

    return (player_1, player_2)

def next_move(board, player):
    """Next player picks a move"""
    
    move_row = "move"
    move_column = "move"

    while not move_row.isnumeric():
        move_row = input("{}, pick row to place your {}. > ".format(player.name, player.char))
    while not move_column.isnumeric():   
        move_column = input("Pick column in row {} to place your {}. > ".format(move_row, player.char))

    move_row = int(move_row)
    move_column = int(move_column)

    move = Move(player, (move_row, move_column))
    
    # Check if move is out of bounds
    if (move_row >= len(board.current_board) or
        move_column >= len(board.current_board)):
        print("Move out of bounds. Choose a valid move.")
        return board

    # Check if space is already used
    if board.current_board[move_row][move_column] != "-":
        print("Spot already played. Pick an unused space.")
        return board

    board.last_move = player.name
    board.add_move(move)

    return board


if __name__ == "__main__":
    """ADD DOCSTRING"""

    # Create players
    (player_1, player_2) = create_players()

    # Initialize new board
    board = Board()

    # Start game
    game = Game(board, player_1, player_2)

    # Play game
    while not board.is_winning() and not board.is_full():

        if board.last_move == player_2.name or board.last_move is None:
            board = next_move(board, player_1)
        else:
            board = next_move(board, player_2)

        board.display()

    # Display winner
    if board.is_winning == True:
        print("{} wins!".format(board.last_move.player.name))
    else:
        print("Game over - it's a tie!")

