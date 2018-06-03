import numpy as np


def insert_coor(board,player):
    print("Now is the turn of Player {0}".format(player))
    while True:
        point = list(input("Please select coordinates: "))
        coors = []
        for i in point:
            if i.isdigit():
                coors.append(i)
        if len(coors) >= 2:
            y = int(coors[0]) - 1
            x = int(coors[1]) - 1
        else:
            print("Not enough coordinates given. Please retry.")
            continue

        if x >= 0 and x < 3 and y >= 0 and y < 3:
            if board[x,y] == 0:
                board[x,y] = player
                print(board)
                break
            else:
                print("Point already used, please choose another one")
                continue
        else:
            print("Coordinates out of bound. Please retry.")
            continue

def row_win(board,player):

    for i in board:
        a = np.asarray(i)[0]

        if any(a != player):
            continue
        else:
            return True

    return False

def col_win(board,player):

    for i in range(3):
        col = board[:,i]
        col = np.asarray(col)[:,0]

        if any(col != player):
            continue
        else:
            return True
    return False

def diag_win(board,player):
    diag1 = []
    diag2 = []

    for i,j in zip(range(3),reversed(range(3))):
        diag1.append(board[i,i])
        diag2.append(board[i,j])

    diags = [diag1,diag2]

    for diag in diags:
        diag = np.asarray(diag)
        if any(diag != player):
            continue
        else:
            return True

    return False

def check_win(board,player):
    if row_win(board,player):
        return True
    elif col_win(board,player):
        return True
    elif diag_win(board,player):
        return True
    else:
        return False

def tic_tac_toe():
    board = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
    print("The game can begun! \n{0}".format(board))
    while True:
        insert_coor(board,1)
        if check_win(board,1):
            print("Player 1 won!")
            break
        elif np.all(board != 0):
            print("No moves remained")
            break

        insert_coor(board,2)
        if check_win(board,2):
            print("Player 2 won!")
            break
        elif np.all(board != 0):
            print("No moves remained")
            break

tic_tac_toe()
