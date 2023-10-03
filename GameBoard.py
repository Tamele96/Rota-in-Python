class GameBoard:

    def __init__(self):
        board = [1, 1, 1, 0, 2, 2, 2, 0, 0]
        activeGame = True

    def playerTurn(self, player):
        print(f"Player {player}'s turn:")
        oldField = int(input("From: "))
        while self.board[oldField] != player:
            oldField = int(input("That's not a valid field. Please select again: "))  

        newField = int(input("To: "))
        while (self.board[newField] != 0) and (((newField == (oldField + 1) % 8) or (newField == (oldField - 1) % 8) or (oldField == 8) or (newField == 8))):
            newField = int(input("That's not an empty field. Please select again: "))
        
        self.board[oldField] = 0
        self.board[newField] = player
        
        if self.board[8] == player:
            for i in range (0,4):
                if self.board[i]== player and self.board[i+4]== player:
                    win = True
                    game = False
                    break



