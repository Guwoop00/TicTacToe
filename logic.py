from views import cell_taken_view, invalid_input_view, player_input_view


def init_board():
    return [[" "] * 3 for _ in range(3)]


def get_player_input(board, player):
    while True:
        player_input_view(player)
        try:
            choice = int(input()) - 1
            row, col = divmod(choice, 3)

            if board[row][col] == " ":
                board[row][col] = player
                break

            else:
                cell_taken_view()

        except (ValueError, IndexError):
            invalid_input_view()


def check_winner(board, player):
    return (
        any(all(cell == player for cell in row) for row in board) or
        any(all(row[i] == player for row in board) for i in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2 - i] == player for i in range(3))
    )

    # for row in board:
    #     if all(col == player for col in row):
    #         return True
    # for i in range(3):
    #     if all(board[row][i] == player for row in range(3)):
    #         return True
    # if all(board[i][i] == player for i in range(3)):
    #     return True
    # if all(board[i][2 - i] == player for i in range(3)):
    #     return True
    # return False


def draw_game(board):
    return all(cell != " " for row in board for cell in row)


def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"
