#A TIC TAC TOE GAME
#
# made by Louis Sheid

def start(): # FIRST PLAYER CHOOSES TO BE X OR O - SENDS THAT CHOICE TO game()
    print(""" _______________________
|------TIC-TAC-TOE------|
|                       |
|        -------        |
|       | 1|2|3 |       |
|       | 4|5|6 |       |
|       | 7|8|9 |       |
|        -------        |
|_______________________|""")
    while True:
        xo = input("(start) X or O?: ").capitalize() #just makes sure x or o typed in is capitalized for the game board
        if xo != "O" and xo != "X": print("Type in either X or O")
        else: game(xo)

def game(xo): #PLACES X OR O ON A BOARD, STORED AS A STRING ARRAY, THEN SENDS THAT CURRENT BOARD TO checkgamestate()
    grid = """_|_|_
_|_|_
_|_|_"""
    boards = []
    boards.append(grid) #just adds the original game board as the first value in the array
    i = 0
    while True:
        try: loc_d = int(input(xo + " -> Type a number [1-9]: ")) #loc_d = location_desired
        except ValueError: print("That is not an integer") #makes sure the person playing doesn't input anything but an integer value (it would break the game)
        if loc_d > 9: print("Must be a number in between 1 and 9")
        else:
            loc_c = (2 * loc_d) - 1 #IMPORTANT - because the string value has characters already in it, typing in '3' would not be the 3rd position - have to take the underscores and '|' <- these things into account
            if boards[i][loc_c - 1:loc_c] != '_': print('Choose another position') #if the player types in a number that already has a character in it by checking if that place is empty or not - '_' is a blank space
            else:
                board_move = boards[i][:loc_c - 1] + boards[i][loc_c - 1:loc_c].replace('_', xo) + boards[i][loc_c:] # this makes a new board with the new move. -> board_move = [board until desired place] + [the desired place] + [the rest of the board]
                boards.append(board_move) #adds this updated board to the array
                print(boards[i+1]) #the board you see while playing
                currentBoard = boards[i+1] #literally only used to send to checkgamestate()
                i += 1
                if xo == "X": xo = "O" #switching the X's to O's for the next turn (or vice versa)
                else: xo = "X"
                checkgamestate(currentBoard)

def checkgamestate(currentBoard): #ITERATES THROUGH ALL ROWS, COLUMNS AND CROSS SECTIONS TO CHECK IF THERE IS A 'WIN' OR THREE CONSECUTIVE X'S OR O'S
    while True:
        i = 0
        n = 0
        for k in range(3): #There are 3 rows and 3 columns and this loop checks both simultaneously
            rows = currentBoard[i:i+6].replace("_", "").replace("|", "").replace("\n", "") #IMPORTANT - takes the row/column and turns it into a string ABSENT of "_","|" and \n (which denotes a line break)
            cols = (currentBoard[n:n+2] + currentBoard[n+5:n+7] + currentBoard[n+11:n+13]).replace("_","").replace("|", "").replace("\n", "") #So these numerical values are just the exact places on the grid string where the row/column spaces are.
            if "OOO" in rows: #pretty self explanatory
                print("ROW O wins")
                start() #Restarts the game
            if "XXX" in rows:
                print("ROW X wins")
                start()
            if "OOO" in cols:
                print("COL O wins")
                start()
            if "XXX" in cols:
                print("COL X wins")
                start()
            u = 0
            for p in range(2): #there are only 2 possible across combos - I know that having a nested for-loop like this may be a bit redundant but that's why I'm sending the code over!
                across = (currentBoard[u:u+1] + currentBoard[7:9] + currentBoard[15 - u:17 - u]).replace("_","").replace("|","").replace( "\n" ,"") #Similar to the rows/columns, just going from the left cross to the right one by adding and subtracting a 4 respectively to the starting positions (it goes from the top left down then from the top right down)
                u += 4
                if "XXX" in across:
                    print("DIAG X wins")
                    start()
                if "OOO" in across:
                    print("DIAG O wins")
                    start()
            i+=6
        break
start() #the command that starts it all...

#So my main problem lies in the checkgamestate() function primarily with the repetitive if statements and nested for-loop. gang.