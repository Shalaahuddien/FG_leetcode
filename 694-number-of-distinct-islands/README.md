<h2><a href="https://leetcode.com/problems/number-of-distinct-islands/">694. Number of Distinct Islands</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an <code style="user-select: auto;">m x n</code> binary matrix <code style="user-select: auto;">grid</code>. An island is a group of <code style="user-select: auto;">1</code>'s (representing land) connected <strong style="user-select: auto;">4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p style="user-select: auto;">An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of <b style="user-select: auto;">distinct</b> islands</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-1-grid.jpg" style="width: 413px; height: 334px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-2-grid.jpg" style="width: 413px; height: 334px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == grid.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == grid[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">grid[i][j]</code> is either <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
</ul>
</div>