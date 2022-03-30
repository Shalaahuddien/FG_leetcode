<h2><a href="https://leetcode.com/problems/path-with-maximum-minimum-value/">1102. Path With Maximum Minimum Value</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an <code style="user-select: auto;">m x n</code> integer matrix <code style="user-select: auto;">grid</code>, return <em style="user-select: auto;">the maximum <strong style="user-select: auto;">score</strong> of a path starting at </em><code style="user-select: auto;">(0, 0)</code><em style="user-select: auto;"> and ending at </em><code style="user-select: auto;">(m - 1, n - 1)</code> moving in the 4 cardinal directions.</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">score</strong> of a path is the minimum value in that path.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the score of the path <code style="user-select: auto;">8 → 4 → 5 → 9</code> is <code style="user-select: auto;">4</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/05/maxgrid1.jpg" style="width: 244px; height: 245px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[5,4,5],[1,2,6],[7,4,6]]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> The path with the maximum score is highlighted in yellow. 
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/05/maxgrid2.jpg" style="width: 484px; height: 165px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/05/maxgrid3.jpg" style="width: 404px; height: 485px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == grid.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == grid[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= grid[i][j] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>