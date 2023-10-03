import GameBoard

game = GameBoard()
player = 1

while game.activeGame:
    game.playerTurn(player)
    if (player == 1):
        player = 2
    else:
        player = 1

print(f"Player {game.board[8]} won!")