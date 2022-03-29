<h2><a href="https://leetcode.com/problems/special-positions-in-a-binary-matrix/">1582. Special Positions in a Binary Matrix</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an <code style="user-select: auto;">m x n</code> binary matrix <code style="user-select: auto;">mat</code>, return <em style="user-select: auto;">the number of special positions in </em><code style="user-select: auto;">mat</code><em style="user-select: auto;">.</em></p>

<p style="user-select: auto;">A position <code style="user-select: auto;">(i, j)</code> is called <strong style="user-select: auto;">special</strong> if <code style="user-select: auto;">mat[i][j] == 1</code> and all other elements in row <code style="user-select: auto;">i</code> and column <code style="user-select: auto;">j</code> are <code style="user-select: auto;">0</code> (rows and columns are <strong style="user-select: auto;">0-indexed</strong>).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> (0, 0), (1, 1) and (2, 2) are special positions.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == mat.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == mat[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">mat[i][j]</code> is either <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
</ul>
</div>