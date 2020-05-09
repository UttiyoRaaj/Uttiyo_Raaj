
# Will hold our game main_board data
main_main_board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_not_done = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
curr_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def start_game():

  # Show the initial game main_board
  display_main_board()

  # Loop until the game stops (winner or tie)
  while game_not_done:

    # Handle a turn
    handle_turn(curr_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game main_board to the screen
def display_main_board():
  print("\n")
  print(main_board[0] + " | " + main_board[1] + " | " + main_board[2] + "     1 | 2 | 3")
  print(main_board[3] + " | " + main_board[4] + " | " + main_board[5] + "     4 | 5 | 6")
  print(main_board[6] + " | " + main_board[7] + " | " + main_board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get pos from player
  print(player + "'s turn.")
  pos = input("Choose a pos from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      pos = input("Choose a pos from 1-9: ")
 
    # Get correct index in our main_board list
    pos = int(pos) - 1

    # Then also make sure the spot is available on the main_board
    if main_board[pos] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the main_board
  main_board[pos] = player

  # Show the game main_board
  display_main_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diag_winner = check_diags()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diag_winner:
    winner = diag_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_not_done
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = main_board[0] == main_board[1] == main_board[2] != "-"
  row_2 = main_board[3] == main_board[4] == main_board[5] != "-"
  row_3 = main_board[6] == main_board[7] == main_board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_not_done = False
  # Return the winner
  if row_1:
    return main_board[0] 
  elif row_2:
    return main_board[3] 
  elif row_3:
    return main_board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_not_done
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = main_board[0] == main_board[3] == main_board[6] != "-"
  column_2 = main_board[1] == main_board[4] == main_board[7] != "-"
  column_3 = main_board[2] == main_board[5] == main_board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_not_done = False
  # Return the winner
  if column_1:
    return main_board[0] 
  elif column_2:
    return main_board[1] 
  elif column_3:
    return main_board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diags for a win
def check_diags():
  # Set global variables
  global game_not_done
  # Check if any of the columns have all the same value (and is not empty)
  diag_1 = main_board[0] == main_board[4] == main_board[8] != "-"
  diag_2 = main_board[2] == main_board[4] == main_board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diag_1 or diag_2:
    game_not_done = False
  # Return the winner
  if diag_1:
    return main_board[0] 
  elif diag_2:
    return main_board[2]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_not_done
  # If main_board is full
  if "-" not in main_board:
    game_not_done = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():
  # Global variables we need
  global curr_player
  # If the current player was X, make it O
  if curr_player == "X":
    curr_player = "O"
  # Or if the current player was O, make it X
  elif curr_player == "O":
    curr_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
start_game()