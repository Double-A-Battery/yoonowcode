import random

def printBoard(board):
    for j in range(len(board)):
        PrStore = ""
        for i in range(len(board[j])):
            PrStore = PrStore + board[j][i]
        print(PrStore)

def CheckWin(board):
    win = ""
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0]!= "☐":
        win = board[0][0]
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0]!= "☐":
        win = board[0][0]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0]!= "☐":
        win = board[0][0]
    if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1]!= "☐":
        win = board[0][1]
    if board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2]!= "☐":
        win = board[0][2]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2]!= "☐":
        win = board[0][2]
    if board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0]!= "☐":
        win = board[1][0]
    if board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0]!= "☐":
        win = board[2][0]
    full = False
    if win == "":
        full = True
        for i in range(len(board)):
            for j in range (len(board[i])):
                if board[i][j] == "☐":
                    full = False

    if full == True:
        win = "-"
    return win

def checkValid(board,choice):
    valid = False
    exampleboard = [["1","2","3"],["4","5","6"],["7","8","9"]]
    for i in range (len(board)):
        for j in range(len(board[i])):
            if choice == exampleboard[i][j]:
                if board[i][j] == "☐":
                    valid = True
    return valid

def playerTurn(board):
    printBoard(board)
    exampleboard = [["1","2","3"],["4","5","6"],["7","8","9"]]
    valid = False
    while valid == False:
        gridnum = input("enter a grid position here to place an X ")
        valid = checkValid(board,gridnum)
    for i in range (len(board)):
        for j in range(len(board[i])):
            if gridnum == exampleboard[i][j]:
                board[i][j] = "X"
    return board

def BotTurn(board):
    printBoard(board)
    exampleboard = [["1","2","3"],["4","5","6"],["7","8","9"]]
    valid = False
    while valid == False:
        gridnum = str(random.randint(1,9))
        valid = checkValid(board,gridnum)
    for i in range (len(board)):
        for j in range(len(board[i])):
            if gridnum == exampleboard[i][j]:
                board[i][j] = "O"
    return board

def Turn():
    board = [["☐","☐","☐"],["☐","☐","☐"],["☐","☐","☐"]]
    exampleBoard = [["1","2","3"],["4","5","6"],["7","8","9"]]
    printBoard(board)
    print("in this game of tic tac toe you will see the board as X's, O's. boxes represent empty spaces")
    pause = input("press enter to continue")
    printBoard(exampleBoard)
    print("each box on the grid has a corresponding number (shown above)")
    pause = input("press enter to continue")
    print("on your go, type the number of the box on the grid you wish to fill with your X")
    pause = input("press enter to continue")
    win = ""
    while win == "":
        print("----------player------------")
        board = playerTurn(board)
        win = CheckWin(board)
        if win == "":
            print("---------computer-----------")
            board = BotTurn(board)
            win = CheckWin(board)
    print("Final board \n___________________:")
    printBoard(board)
    if win == "O":
        print("computor wins")
    elif win == "X":
        print("player wins")
    else:
        print("its a tie")

Turn()
