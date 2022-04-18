<h2><a href="https://leetcode.com/problems/minesweeper/">529. Minesweeper</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Let's play the minesweeper game (<a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)" target="_blank" style="user-select: auto;">Wikipedia</a>, <a href="http://minesweeperonline.com" target="_blank" style="user-select: auto;">online game</a>)!</p>

<p style="user-select: auto;">You are given an <code style="user-select: auto;">m x n</code> char matrix <code style="user-select: auto;">board</code> representing the game board where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">'M'</code> represents an unrevealed mine,</li>
	<li style="user-select: auto;"><code style="user-select: auto;">'E'</code> represents an unrevealed empty square,</li>
	<li style="user-select: auto;"><code style="user-select: auto;">'B'</code> represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),</li>
	<li style="user-select: auto;">digit (<code style="user-select: auto;">'1'</code> to <code style="user-select: auto;">'8'</code>) represents how many mines are adjacent to this revealed square, and</li>
	<li style="user-select: auto;"><code style="user-select: auto;">'X'</code> represents a revealed mine.</li>
</ul>

<p style="user-select: auto;">You are also given an integer array <code style="user-select: auto;">click</code> where <code style="user-select: auto;">click = [click<sub style="user-select: auto;">r</sub>, click<sub style="user-select: auto;">c</sub>]</code> represents the next click position among all the unrevealed squares (<code style="user-select: auto;">'M'</code> or <code style="user-select: auto;">'E'</code>).</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the board after revealing this position according to the following rules</em>:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">If a mine <code style="user-select: auto;">'M'</code> is revealed, then the game is over. You should change it to <code style="user-select: auto;">'X'</code>.</li>
	<li style="user-select: auto;">If an empty square <code style="user-select: auto;">'E'</code> with no adjacent mines is revealed, then change it to a revealed blank <code style="user-select: auto;">'B'</code> and all of its adjacent unrevealed squares should be revealed recursively.</li>
	<li style="user-select: auto;">If an empty square <code style="user-select: auto;">'E'</code> with at least one adjacent mine is revealed, then change it to a digit (<code style="user-select: auto;">'1'</code> to <code style="user-select: auto;">'8'</code>) representing the number of adjacent mines.</li>
	<li style="user-select: auto;">Return the board when no more squares will be revealed.</li>
</ol>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png" style="width: 500px; max-width: 400px; height: 269px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
<strong style="user-select: auto;">Output:</strong> [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png" style="width: 500px; max-width: 400px; height: 275px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
<strong style="user-select: auto;">Output:</strong> [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == board.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == board[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[i][j]</code> is either <code style="user-select: auto;">'M'</code>, <code style="user-select: auto;">'E'</code>, <code style="user-select: auto;">'B'</code>, or a digit from <code style="user-select: auto;">'1'</code> to <code style="user-select: auto;">'8'</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">click.length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= click<sub style="user-select: auto;">r</sub> &lt; m</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= click<sub style="user-select: auto;">c</sub> &lt; n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[click<sub style="user-select: auto;">r</sub>][click<sub style="user-select: auto;">c</sub>]</code> is either <code style="user-select: auto;">'M'</code> or <code style="user-select: auto;">'E'</code>.</li>
</ul>
</div>