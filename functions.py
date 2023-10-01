#define board
boardField = ['i', 'i', 'i', 'e', 'u', 'u', 'u', 'e', 'e']

game = True
iturn = True
win = False


#Create board
def createBoard():
    boardField = ['i', 'i', 'i', 'e', 'u', 'u', 'u', 'e', 'e']


#restart the game
def start_game():
    createBoard()
    game = True
    iturn = True
    win = False


#Player 1's turn
def player_i():
    print("\nPlayer 1's turn:\n")
    oldField = int(input("From: "))
    
    while boardField[oldField] != 'i':
            oldField = int(input("That's not a valid field. Please select again: "))

    while boardField[newField] != 'e':    
            newField = int(input("To: "))
            while (boardField[newField] != 'e') and (((newField == (oldField + 1) % 8) or (newField == (oldField - 1) % 8) or (oldField == 8) or (newField == 8))):
                newField = int(input("That's not an empty field. Please select again: "))

            boardField[newField]='i'
            boardField[oldField]='e'
    iturn = False


#Player 2's turn
def player_u():
    print("\nPlayer 2's turn:\n")
    oldField = int(input("From: "))
    while boardField[oldField] != 'u':
            oldField = int(input("That's not a valid field. Please select again: "))

         
            newField = int(input("To: "))
            while (boardField[newField] != 'e') and (((newField == (oldField + 1) % 8) or (newField == (oldField - 1) % 8) or (oldField == 8)  or (newField == 8))):
                newField = int(input("That's not an empty field. Please select again: "))

            boardField[newField]='u'
            boardField[oldField]='e'
    iturn = True

#check if someone won
def win_check():
     if boardField[8] == 'i':
        for i in range (0,4):
             if boardField[i]=='i' and boardField[i+4]=='i':
                 win = True
                 game = False 
                 break
     elif boardField[8] == 'u':
        for i in range (0,4):
             if boardField[i]=='u' and boardField[i+4]=='u':
                 win = True
                 game = False 
                 break
             
#print out the winner
def print_winner():
     print(boardField[8], "won!")



    