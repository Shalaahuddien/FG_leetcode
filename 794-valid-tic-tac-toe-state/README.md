<h2><a href="https://leetcode.com/problems/valid-tic-tac-toe-state/">794. Valid Tic-Tac-Toe State</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a Tic-Tac-Toe board as a string array <code style="user-select: auto;">board</code>, return <code style="user-select: auto;">true</code> if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.</p>

<p style="user-select: auto;">The board is a <code style="user-select: auto;">3 x 3</code> array that consists of characters <code style="user-select: auto;">' '</code>, <code style="user-select: auto;">'X'</code>, and <code style="user-select: auto;">'O'</code>. The <code style="user-select: auto;">' '</code> character represents an empty square.</p>

<p style="user-select: auto;">Here are the rules of Tic-Tac-Toe:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Players take turns placing characters into empty squares <code style="user-select: auto;">' '</code>.</li>
	<li style="user-select: auto;">The first player always places <code style="user-select: auto;">'X'</code> characters, while the second player always places <code style="user-select: auto;">'O'</code> characters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">'X'</code> and <code style="user-select: auto;">'O'</code> characters are always placed into empty squares, never filled ones.</li>
	<li style="user-select: auto;">The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.</li>
	<li style="user-select: auto;">The game also ends if all squares are non-empty.</li>
	<li style="user-select: auto;">No more moves can be played if the game is over.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg" style="width: 253px; height: 253px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = ["O  ","   ","   "]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> The first player always plays "X".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg" style="width: 253px; height: 253px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = ["XOX"," X ","   "]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> Players take turns making moves.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg" style="width: 253px; height: 253px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = ["XOX","O O","XOX"]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">board.length == 3</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[i].length == 3</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[i][j]</code> is either <code style="user-select: auto;">'X'</code>, <code style="user-select: auto;">'O'</code>, or <code style="user-select: auto;">' '</code>.</li>
</ul>
</div>