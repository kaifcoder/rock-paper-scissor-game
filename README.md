# Rock Paper Scissor Game

A tiny command‑line implementation of the classic **Rock‑Paper‑Scissors** game written in Python. The program lets a user play against the computer for a fixed number of rounds and displays the final scores.

## Features

- Random computer choice using `random.randint`.
- Supports 5 rounds (can be changed easily).
- Shows round‑by‑round result and final tally.
- Simple text‑based interface.

## Prerequisites

- Python 3.x installed.

## Installation

```bash
git clone https://github.com/kaifcoder/rock-paper-scissor-game.git
cd rock-paper-scissor-game
```

No external dependencies are required.

## Usage

Run the script:

```bash
python rock_paper_scissor.py
```

You will be prompted to enter your name (at least 4 alphabetic characters) and then to choose **rock**, **paper**, or **scissor** for each round. After each round the program prints who won that round and updates the scores. After the configured number of rounds the final scores are displayed.

## Code Overview

- `choices` – list of possible moves.
- `username()` – asks the player for a name and validates it.
- `comp_choice()` – returns a random choice for the computer.
- Main loop – runs the game for a set number of rounds, compares choices, updates scores, and prints results.

## Improvements & Known Issues

- The current implementation calls `comp_choice()` multiple times per round, which may give different computer moves for the same comparison. Storing the result in a variable fixes this.
- Input validation for the player's choice is minimal; entering an invalid option will be treated as a loss.
- The number of rounds is hard‑coded to 5; you can change the `range(5)` value to adjust it.

Feel free to fork the repo and submit pull requests with enhancements such as better input handling, configurable round count, or a graphical UI.

## License

This project is released under the MIT License.
