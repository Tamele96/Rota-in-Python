
#Create board
##################
boardField = ['i', 'i', 'i', 'e', 'u', 'u', 'u', 'e', 'e']
##################


#Create active game loop
##################
game = True
iturn = True
uturn = False
win = False


while game == True:

    #Player 1's turn
    ####################################
    if iturn == True:
        while iturn == True:

            print("\nPlayer 1's turn:\n")
            oldField = int(input("From: "))
            while boardField[oldField] != 'i':
                oldField = int(input("That's not a valid field. Please select again: "))

         
            newField = int(input("To: "))
            while (boardField[newField] != 'e') and ((newField == (oldField + 1) % 8) or (newField == (oldField - 1) % 8)):
                newField = int(input("That's not an empty field. Please select again: "))

            boardField[newField]='i'
            boardField[oldField]='e'

            #check if someone won
            ###############################
            if boardField[8] == 'i':
                for i in range (0,3):
                    if boardField[i]=='i' and boardField[i+4]=='i':
                        win = True
                        game = False 
                        break
            ##############################

            iturn = False
            uturn = True
        
        

        
        
    ####################################
    
    
    #Player 2's turn
    ####################################
    if uturn == True:
        while uturn == True:
            print("\nPlayer 2's turn:\n")

            oldField = int(input("From: "))
            while boardField[oldField] != 'u':
                oldField = int(input("That's not a valid field. Please select again: "))

         
            newField = int(input("To: "))
            while (boardField[newField] != 'e') and ((newField == (oldField + 1) % 8) or (newField == (oldField - 1) % 8)):
                newField = int(input("That's not an empty field. Please select again: "))

            boardField[newField]='u'
            boardField[oldField]='e'

            #check if someone won
            ###############################
            if boardField[8] == 'i':
                for i in range (0,3):
                    if boardField[i]=='i' and boardField[i+4]=='i':
                        win = True
                        game = False 
                        break
            ###############################
            uturn = False
            iturn = True

print(boardField[8], "won!")
