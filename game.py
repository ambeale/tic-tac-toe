from datetime import datetime

class Player:

	def __init__(self, name, char):
		self.name = name
		self.char = char


class Move:
	
	def __init__(self, player, position):
		self.player = player
		self.position = position


class Board:
	
	def __init__(self):
		self.current_board = [["-","-","-"],
					  ["-","-","-"],
					  ["-","-","-"]]

	def display(self):
		for line in self.current_board:
			print(" ".join(line))

	def add_move(self, move):
		self.current_board[move.position[0]][move.position[1]] = move.player.char

class Game:
	
	def __init__(self, board, player_1, player_2):
		self.board = board
		self.player1 = player_1
		self.player2 = player_2
		self.started_at = datetime.now().time()
		self.finished_at = None
	

def create_players():

	# Create player1
	name_1 = input("Player 1, what is your name? > ")
	char_1 = input("Would you like to be X or O? > ").upper()
	player_1 = Player(name_1, char_1)

	# Create player2
	name_2 = input("Player 2, what is your name? > ")

	if char_1.lower() == "x":
		print("{}, you are O.".format(name_2))
		char_2 = "O"
	else:
		print("{}, you are X.".format(name_2))
		char_2 = "X"

	player_2 = Player(name_2, char_2)

	return (player_1, player_2)

def next_move(board, player):
	"""Next player picks a move"""
	
	move_row = int(input("{}, pick row to place your {}. > ".format(player.name, player.char)))
	move_column = int(input("Pick column in row {} to place your {}. > ".format(move_row, player.char)))

	move = Move(player, (move_row, move_column))
	
	# TO DO: add condition if space is already picked

	board.add_move(move)

	return board



(player_1, player_2) = create_players()

# Initialize new board
board = Board()

# Start game
game = Game(board, player_1, player_2)

board.display()

board = next_move(board, player_1)

board.display()



### END CONDITIONS ###

# 1. The board is full
# 		"-" not in board.current_board
#
# 2. A player wins