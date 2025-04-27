import random

board = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]

def printtable(board):
    for i in range(len(board)):
        print("|".join(board[i]))
        if (i!=len(board)-1):
            print("-"*11)


def win(board,player):
    winning_combinations = [
    # Rows
    [[0,0], [0,1], [0,2]],
    [[1,0], [1,1], [1,2]],
    [[2,0], [2,1], [2,2]],

    # Columns
    [[0,0], [1,0], [2,0]],
    [[0,1], [1,1], [2,1]],
    [[0,2], [1,2], [2,2]],

    # Diagonals
    [[0,0], [1,1], [2,2]],
    [[0,2], [1,1], [2,0]]
                           ]
    mark=f" {player} "
    for k in winning_combinations:
        if all(board[rol][col]==mark for rol,col in k):
           return True
    return False
    

def modify(XO):
     while True:
        rol=int(input("Enter which row  like matrix(3x3)"))
        col=int(input("Enter which colum like matrix(3x3)"))
        if 0<= rol <= 2 and 0 <= col <= 2:
            if board[rol][col]=="   ":
                board[rol][col]=f" {XO} " 
                break
            else:                    
                print("Position is already taken")
        else:
            print("Enter a position where it is free")

def comp():
    list=[0,1,2]
    while True:
        rol=random.choice(list)
        col=random.choice(list)
        if board[rol][col]=="   ":
            board[rol][col]=" O "
            break

def all3():
    score1=0
    score2=0
    scorec=0
    for l in range(100):
        f=int(input(("How do you want to play 1.2/Player 2.Single player 3.Exit")))
        if f==2:
            for j in range(5):
                print("\n\n")
                printtable(board)
                print("Player 1's turn")
                modify("X")
                printtable(board)
                a=win(board,"X")
                if a==True:
                    print("Player 1 Wins")
                    score1=score1+1
                    print(f" Score is Player {score1} \nScore of Computer {scorec}\n")
                    break

                if j==4:
                    print("It's a draw")
                    break


                print("\n\n")
                comp()
                printtable(board)
                b=win(board,"O")
                if b==True:
                    print("Computer wins")
                    scorec=scorec+1
                    print(f" Score is Player {score1} \nScore of Computer {scorec}\n")

                    break
        elif f==1:
             for j in range(5):
                print("\n\n")
                printtable(board)
                print("Player 1's turn")
                modify("X")
                printtable(board)
                a=win(board,"X")
                if a==True:
                    print("Player 1 Wins")
                    score1=score1+1
                    print(f" Score is Player {score1} \nScore of Player 2 {score2}\n")
                    break

                if j==4:
                    print("It's a draw")
                    break


                print("\n\n")
                print("Player 2's turn")
                modify("O")
                printtable(board)
                b=win(board,"O")
                if b==True:
                    print("Player 2  wins")
                    score2=score2+1
                    print(f" Score is Player {score1} \nScore of Player 2 {score2}\n")
                    break
                
        elif f==3:
            break
        else:
            print("Enter a valid number:")
        for i in range(3):
            for j in range(3):
                board[i][j] = "   "
all3()