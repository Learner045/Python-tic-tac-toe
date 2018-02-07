board=["  "for i in range(9)]

def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
        
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    

def is_victory(icon):
    row_wins=[[0,1,2],[3,4,5],[6,7,8]]
    col_wins=[[0,3,6],[1,4,7],[2,5,8]]
    diag_wins=[[0,4,8],[2,4,6]]

    for i in range(2):
        if (board[row_wins[i][0]]==icon and board[row_wins[i][1]]==icon and board[row_wins[i][2]]==icon):
            return True         

    for j in range(2):
        if (board[col_wins[j][0]]==icon and board[col_wins[j][1]]==icon and board[col_wins[j][2]]==icon):
             return True
            
    for k in range(2):
         if (board[diag_wins[k][0]]==icon and board[diag_wins[k][1]]==icon and board[diag_wins[k][2]]==icon):
             return True
    return False
    
         
def is_draw():
    if "  " not in board:
        return True
    else:
        return False
     

print(is_victory("X"))
def player_move(icon):

    if icon=="X":
        number=1
    elif icon=="O":
        number=2

    print("Player {} plays".format(number))

    choice=int(input("Enter your choice(1-9): ").strip())
    if board[choice-1]=="  ":
        board[choice-1]=icon
    else:
        print()
        print("space already taken!")
    

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins!Yay")
        break
    player_move("O")
    if is_victory("O"):
        print("O Wins!Yay")
        break
    if is_draw():
        print("Draw")
        break





    
    

        
        
    
    
   

