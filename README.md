
# Maze Solver Project

This project is a Python-based graphical application that uses the Tkinter library to create, visualize, and solve mazes. The application allows users to explore maze generation and solving algorithms such as Depth-First Search (DFS) and Breadth-First Search (BFS).

## Project Structure

```
maze_solver_project/
│
├── src/
│   ├── __init__.py
│   ├── main.py               # Entry point for the application
│   ├── maze_generator.py      # Handles the maze generation algorithms
│   ├── maze_solver.py         # Contains algorithms like DFS, BFS for solving the maze
│   ├── gui.py                 # Handles the Tkinter GUI components
│   └── utils.py               # Utility functions (e.g., for drawing, randomization)
│
├── tests/
│   ├── __init__.py
│   ├── test_maze_generator.py # Unit tests for maze generation
│   ├── test_maze_solver.py    # Unit tests for solving algorithms
│   └── test_gui.py            # Tests related to the GUI (optional or mock-based)
│
├── assets/
│   └── images/                # Any assets for your GUI (e.g., icons, graphics)
│
├── docs/
│   └── README.md              # Documentation on how to run the project and any notes
│
├── venv/                      # Your Python virtual environment (usually excluded from version control)
│
├── .vscode/                   # VSCode-specific settings (e.g., launch.json, settings.json)
│
├── requirements.txt           # List of project dependencies
│
└── setup.py                   # If packaging the project for distribution (optional)
```

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

To install Tkinter on WSL or other minimal environments, you can run:

```
sudo apt-get install python3-tk
```

## How to Run

1. Clone this repository or download the source code.
2. Navigate to the `src/` folder and run the following command:

```
python3 main.py
```

This will open a graphical window with an 800x600 canvas, where the maze-solving algorithms will be implemented.

## Features

- **Tkinter GUI**: A graphical window where mazes can be drawn and solved.
- **Maze Generation Algorithms**: Will include DFS-based random maze generation.
- **Maze Solving Algorithms**: Includes classical maze-solving algorithms like DFS and BFS.

## License

This project is open-source and free to use under the MIT License.
