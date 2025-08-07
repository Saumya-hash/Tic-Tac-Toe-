🎮 Tic-Tac-Toe with AI (Minimax + Alpha-Beta Pruning)
A Python terminal-based implementation of the classic Tic-Tac-Toe game where you play against an unbeatable AI! The AI uses the Minimax algorithm enhanced with Alpha-Beta pruning to make optimal decisions.
📌 Features
Play as 'O', the human player, against the AI ('X')
AI makes optimal moves using Minimax and Alpha-Beta pruning
Handles win, draw, and invalid move conditions
Simple and clean command-line interface
🧠 How It Works
The game board is a 3x3 grid implemented using a Python list. The AI evaluates all possible future moves using recursion and selects the move that minimizes the potential loss, while pruning unnecessary branches for efficiency.
Minimax: Recursively simulates all possible outcomes
Alpha-Beta Pruning: Improves performance by cutting off branches that won't affect the result
