<h1 align="center">Tic-Tac-Toe Game</h1>
<h3 align="center"> Simple Tic-Tac-Toe Game with GUI</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Tkinter-Built--in-blue.svg" alt="Tkinter">
</p>
<p align="center">This project is a simple implementation of the classic Tic-Tac-Toe game using Python's Tkinter library. The game features a graphical user interface (GUI) where two players can play against each other. It keeps track of the players' turns, checks for winning conditions, and displays the game result. Additionally, it includes a timer to show the duration of the game.</p>
🚀 Features
<p align="center">
  <ul>
    <li><strong>Player Turns:</strong> The game alternates between two players, X and O.</li>
    <li><strong>Winning Detection:</strong> The game checks for winning conditions after each move.</li>
    <li><strong>Draw Detection:</strong> The game can detect if there is a draw (no more possible moves).</li>
    <li><strong>Score Keeping:</strong> The game keeps track of the scores for both players.</li>
    <li><strong>Timer:</strong> A timer displays the elapsed time since the game started.</li>
    <li><strong>Reset:</strong> The board is reset after a win or a draw, allowing players to start a new game.</li>
  </ul>
</p>
📋 Requirements
<p align="center">
  <ul>
    <li>Python 3.x (tested with Python 3.12.4)</li>
    <li>Tkinter (built-in with Python)</li>
  </ul>
</p>
📦 Installation
<p align="center">
  <ol>
    <li><strong>Clone the repository:</strong>
      <pre><code>git clone  https://github.com/EGuseinov/TicTacToe-Game-with-GUI.git 
cd tictactoe</code></pre>
    </li>
    <li><strong>Run the game:</strong>
      <pre><code>python tictactoe.py</code></pre>
    </li>
  </ol>
</p>
🛠 Usage
<p align="center">
  <ol>
    <li>Launch the game by running <code>tictactoe.py</code>.</li>
    <li>The game window will open with a 3x3 grid.</li>
    <li>Player X starts the game. Click on any empty cell to place your mark.</li>
    <li>The game will alternate turns between Player X and Player O.</li>
    <li>When a player wins, a message box will display the winner and the game will reset.</li>
    <li>If all cells are filled and there is no winner, a message box will display "The game is a draw!" and the game will reset.</li>
    <li>The scores and the timer will be updated accordingly.</li>
  </ol>
</p>
🌐 Example
<p align="center">
  Here's an example of how to play the game:
  <ol>
    <li><strong>Start the game:</strong>
      <pre><code>python tictactoe.py</code></pre>
    </li>
    <li><strong>Gameplay:</strong>
      <ul>
        <li>Player X clicks on an empty cell to place their mark.</li>
        <li>The game alternates turns between Player X and Player O.</li>
        <li>A message box will display the result when the game ends.</li>
        <li>The game board resets for a new game.</li>
      </ul>
    </li>
  </ol>
</p>
🗂 Code Structure
<p align="center">
  <ul>
    <li><strong>TicTacToe Class:</strong> This class contains all the game logic and UI components.
      <ul>
        <li><code>__init__</code>: Initializes the game, sets up the UI, and starts the timer.</li>
        <li><code>create_widgets</code>: Creates the top frame widgets for displaying player info, timer, and score.</li>
        <li><code>create_board</code>: Creates the 3x3 grid of buttons for the game board.</li>
        <li><code>click</code>: Handles a player's move and checks for win/draw conditions.</li>
        <li><code>on_enter</code> and <code>on_leave</code>: Handle button hover effects.</li>
        <li><code>check_win</code>: Checks if the current player has won.</li>
        <li><code>is_full</code>: Checks if the board is full (for a draw).</li>
        <li><code>reset_board</code>: Resets the board for a new game.</li>
        <li><code>update_timer</code>: Updates the game timer every second.</li>
      </ul>
    </li>
  </ul>
</p>
📝 Rules
<p align="center">
  <ul>
    <li><strong>Player Turns:</strong> Players alternate turns, starting with Player X.</li>
    <li><strong>Winning Conditions:</strong> A player wins if they place three of their marks in a row, column, or diagonal.</li>
    <li><strong>Draw:</strong> The game is a draw if all cells are filled and no player has won.</li>
    <li><strong>Score Keeping:</strong> The scores for both players are updated and displayed at the top of the game window.</li>
    <li><strong>Timer:</strong> The timer starts at the beginning of the game and stops when a player wins or the game is a draw.</li>
  </ul>
</p>
🤝 Contributing
<p align="center">If you want to contribute to this project, feel free to submit pull requests or open issues.</p>
