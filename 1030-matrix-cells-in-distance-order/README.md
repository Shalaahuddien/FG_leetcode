<h2><a href="https://leetcode.com/problems/matrix-cells-in-distance-order/">1030. Matrix Cells in Distance Order</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given four integers <code style="user-select: auto;">row</code>, <code style="user-select: auto;">cols</code>, <code style="user-select: auto;">rCenter</code>, and <code style="user-select: auto;">cCenter</code>. There is a <code style="user-select: auto;">rows x cols</code> matrix and you are on the cell with the coordinates <code style="user-select: auto;">(rCenter, cCenter)</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the coordinates of all cells in the matrix, sorted by their <strong style="user-select: auto;">distance</strong> from </em><code style="user-select: auto;">(rCenter, cCenter)</code><em style="user-select: auto;"> from the smallest distance to the largest distance</em>. You may return the answer in <strong style="user-select: auto;">any order</strong> that satisfies this condition.</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">distance</strong> between two cells <code style="user-select: auto;">(r<sub style="user-select: auto;">1</sub>, c<sub style="user-select: auto;">1</sub>)</code> and <code style="user-select: auto;">(r<sub style="user-select: auto;">2</sub>, c<sub style="user-select: auto;">2</sub>)</code> is <code style="user-select: auto;">|r<sub style="user-select: auto;">1</sub> - r<sub style="user-select: auto;">2</sub>| + |c<sub style="user-select: auto;">1</sub> - c<sub style="user-select: auto;">2</sub>|</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> rows = 1, cols = 2, rCenter = 0, cCenter = 0
<strong style="user-select: auto;">Output:</strong> [[0,0],[0,1]]
<strong style="user-select: auto;">Explanation:</strong> The distances from (0, 0) to other cells are: [0,1]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> rows = 2, cols = 2, rCenter = 0, cCenter = 1
<strong style="user-select: auto;">Output:</strong> [[0,1],[0,0],[1,1],[1,0]]
<strong style="user-select: auto;">Explanation:</strong> The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> rows = 2, cols = 3, rCenter = 1, cCenter = 2
<strong style="user-select: auto;">Output:</strong> [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
<strong style="user-select: auto;">Explanation:</strong> The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= rows, cols &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= rCenter &lt; rows</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= cCenter &lt; cols</code></li>
</ul>
</div>