import functions as f

f.start_game()

while f.game:

    if f.iturn:
        f.player_i()
        f.win_check()

    else:
        f.player_u()
        f.win_check()

f.print_winner()