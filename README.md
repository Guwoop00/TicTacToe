# Tic-Tac-Toe with Rich

A terminal-based Tic-Tac-Toe game built with Python, featuring colorful output using the `rich` library for enhanced user experience.

## Overview

This project is structured into three modules:
- **logic.py**: Handles game logic.
- **views.py**: Manages display and text styling.
- **main.py**: The entry point to launch the game.

## Installation

### Requirements

- Python 3.x
- `rich` library

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Guwoop00/TicTacToe
   cd tic-tac-toe

2. Create a virtual environment (optional):
   ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. Install dependencies:
    ```bash
    pip install rich

## Usage

1. Start the game:
    ```bash
    python main.py

2. Follow the instructions in the terminal to place your marks.

## Game Rules

- Two players, **X** and **O**, take turns placing marks on a 3x3 grid.
- The first player to align three marks horizontally, vertically, or diagonally wins.
- If all cells are filled without a winning alignment, the game ends in a draw.
