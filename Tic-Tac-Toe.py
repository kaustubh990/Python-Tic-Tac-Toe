#   global varialbles

#board
board = ["-" , "-" , "-", 
         "-" , "-" , "-",
         "-" , "-" , "-",] 

#game still goin
game_still_goin = True

# winner or tie
winner = None

#whos turn
current_player = "X"

def disp_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
    
    
    #display initial board
    disp_board()

    while game_still_goin:
        print()
        print(current_player + "Turns")
        print()
        #handle the turn
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    #winner 
    if winner=="X" or winner=="O":
        print(winner + "WON!!!")

    elif winner==None:
        print("TIE!!!!")


def handle_turn(current_player):

    position =(input("Choose a position to from 1-9: "))
    
    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position =(input("Invalid input!.   Choose a position to from 1-9: "))
    
        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there")

    board[position] = current_player

    disp_board()


def check_if_game_over():

    check_if_win()

    check_if_tie()



def check_if_win():

    global winner


    #check rows
    row_winner = check_row()
    #check column
    column_winner = check_column()
    #check diagonnals
    diagonal_winner = check_diagonal()
    
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner= column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner = None

    
    return


def check_row():

    global game_still_goin
    row1 = board[0] == board[1] == board[2] !="-"
    row2 = board[3] == board[4] == board[5] !="-"
    row3 = board[6] == board[7] == board[8] !="-"
    
    if row1 or row2 or row3:
        game_still_goin = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_column():

    global game_still_goin
    column1 = board[0] == board[3] == board[6] !="-"
    column2 = board[1] == board[4] == board[7] !="-"
    column3 = board[2] == board[5] == board[8] !="-"
    
    if column1 or column2 or column3:
        game_still_goin = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return


def check_diagonal():

    global game_still_goin
    diagonal1 = board[0] == board[4] == board[8] !="-"
    diagonal2 = board[2] == board[4] == board[6] !="-"
    
    if diagonal1 or diagonal2 :
        game_still_goin = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return




def check_if_tie():

    global game_still_goin

    if "-" not in board:
        game_still_goin= False
    return


def flip_player():
    
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()