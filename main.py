from logic import init_board, check_winner, draw_game, switch_player, get_player_input
from views import welcome_message, display_board, player_wins_input, draw_input


def lunch_game():
    welcome_message()
    board = init_board()
    current_player = "X"

    while True:
        display_board(board)
        get_player_input(board, current_player)

        if check_winner(board, current_player):
            display_board(board)
            player_wins_input(current_player)
            break

        elif draw_game(board):
            display_board(board)
            draw_input()
            break

        current_player = switch_player(current_player)


lunch_game()
