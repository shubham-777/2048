# 2048 Game

Welcome to the 2048 game repository! This repository contains a Python implementation of the popular 2048 game using NumPy and tabulate libraries.

## Introduction

2048 is a single-player puzzle game where the objective is to combine tiles with the same value to reach the tile with the number 2048. This implementation allows you to play the game from the command line.

## Features

- Playable game with a command-line interface.
- Support for movement in all four directions (up, down, left, right).
- Automatic insertion of new tiles after each move.
- Win detection when reaching the 2048 tile.

## Installation

To run this game, you'll need Python and the following libraries:

- `numpy`
- `tabulate`

You can install these libraries using pip:

```bash
pip install numpy tabulate
```


## Usage

1. Clone the Repository
First, you need to clone the repository to your local machine. Open your terminal and run: 
``` bash 
git clone https://github.com/shubham-777/2048.git
cd 2048
```

3. Run the game

```bash
python main.py
```

4. Follow the on-screen instructions to play the game

    -   Use `w` to move up.
    -   Use `s` to move down.
    -   Use `a` to move left.
    -   Use `d` to move right.
    -   Use `x` to exit the game.

5.  The game board size can be set when you start the game. Enter the size as an integer for an `n x n` board.

## Code Explanation
Here's a brief overview of the main components of the code:

-   **`print_board(board)`**: Prints the current game board using the tabulate library for a neat display.
-   **`availabel_index(board)`**: Returns the indices of all empty cells in the board.
-   **`check_win(board)`**: Checks if the board contains the winning tile (2048).
-   **`choose_idx(board)`**: Randomly selects an empty cell where the next tile will be inserted.
-   **`choose_number()`**: Randomly selects the value (2 or 4) for the new tile.
-   **`insert_next(board)`**: Inserts a new tile in a randomly chosen empty cell.
-   **`move_board(board, dir)`**: Moves the tiles on the board in the specified direction and combines them if needed.
-   **`take_cmd_input()`**: Prompts the user for movement commands.

## Contributing
If you would like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Commit your changes and push them to your forked repository.
4.  Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
