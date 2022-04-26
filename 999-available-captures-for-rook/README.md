<h2><a href="https://leetcode.com/problems/available-captures-for-rook/">999. Available Captures for Rook</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">On an <code style="user-select: auto;">8 x 8</code> chessboard, there is <strong style="user-select: auto;">exactly one</strong> white rook <code style="user-select: auto;">'R'</code> and some number of white bishops <code style="user-select: auto;">'B'</code>, black pawns <code style="user-select: auto;">'p'</code>, and empty squares <code style="user-select: auto;">'.'</code>.</p>

<p style="user-select: auto;">When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered <strong style="user-select: auto;">attacking</strong> a pawn if the rook can capture the pawn on the rook's turn. The <strong style="user-select: auto;">number of available captures</strong> for the white rook is the number of pawns that the rook is <strong style="user-select: auto;">attacking</strong>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">number of available captures</strong> for the white rook</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG" style="width: 300px; height: 305px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> In this example, the rook is attacking all the pawns.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG" style="width: 300px; height: 306px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The bishops are blocking the rook from attacking any of the pawns.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG" style="width: 300px; height: 305px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> The rook is attacking the pawns at positions b5, d6, and f5.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">board.length == 8</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[i].length == 8</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[i][j]</code> is either <code style="user-select: auto;">'R'</code>, <code style="user-select: auto;">'.'</code>, <code style="user-select: auto;">'B'</code>, or <code style="user-select: auto;">'p'</code></li>
	<li style="user-select: auto;">There is exactly one cell with <code style="user-select: auto;">board[i][j] == 'R'</code></li>
</ul>
</div>