from rich.console import Console
console = Console()


def welcome_message():

    message = """
    Welcome to Tic Tac Toe!

    Player X and Player O will take turns. Choose a number between 1 and 9 to place your mark.

    The board positions are as follows:
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    ---------
    Press Enter to start the game...
    """

    console.print(message, style="light_steel_blue1")
    input()


def position_reminder():

    message = """
    The board positions are as follows:
    ---------
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    ---------
    """
    console.print(message, style="light_steel_blue1 italic")


def display_board(board):

    console.clear()
    console.print("\n" + "-" * 9, style="light_steel_blue1")
    for row in board:
        row_str = " | ".join(row)
        console.print(row_str, style="grey85")
        console.print("-" * 9, style="light_steel_blue1")
    print("\n")


def player_input_view(player):
    position_reminder()
    console.print(f"Player {player}, enter your choice (1-9): ", style="light_steel_blue1")


def cell_taken_view():
    console.print("Cell already taken. Choose another move.", style="red1")


def invalid_input_view():
    console.print("Invalid input. Please enter a number between 1 and 9.", style="red1")


def player_wins_input(player):
    console.print(f"Player {player} wins! ", style="light_green")


def draw_input():
    console.print("It's a draw! ", style="sky_blue1")
