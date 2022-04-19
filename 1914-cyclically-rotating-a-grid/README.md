<h2><a href="https://leetcode.com/problems/cyclically-rotating-a-grid/">1914. Cyclically Rotating a Grid</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an <code style="user-select: auto;">m x n</code> integer matrix <code style="user-select: auto;">grid</code>​​​, where <code style="user-select: auto;">m</code> and <code style="user-select: auto;">n</code> are both <strong style="user-select: auto;">even</strong> integers, and an integer <code style="user-select: auto;">k</code>.</p>

<p style="user-select: auto;">The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:</p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png" style="width: 231px; height: 258px; user-select: auto;"></p>

<p style="user-select: auto;">A cyclic rotation of the matrix is done by cyclically rotating <strong style="user-select: auto;">each layer</strong> in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the <strong style="user-select: auto;">counter-clockwise</strong> direction. An example rotation is shown below:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg" style="width: 500px; height: 268px; user-select: auto;">
<p style="user-select: auto;">Return <em style="user-select: auto;">the matrix after applying </em><code style="user-select: auto;">k</code> <em style="user-select: auto;">cyclic rotations to it</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/rod2.png" style="width: 421px; height: 191px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[40,10],[30,20]], k = 1
<strong style="user-select: auto;">Output:</strong> [[10,20],[40,30]]
<strong style="user-select: auto;">Explanation:</strong> The figures above represent the grid at every state.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png" style="width: 231px; height: 262px; user-select: auto;"></strong> <strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png" style="width: 231px; height: 262px; user-select: auto;"></strong> <strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png" style="width: 231px; height: 262px; user-select: auto;"></strong>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
<strong style="user-select: auto;">Output:</strong> [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
<strong style="user-select: auto;">Explanation:</strong> The figures above represent the grid at every state.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == grid.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == grid[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= m, n &lt;= 50</code></li>
	<li style="user-select: auto;">Both <code style="user-select: auto;">m</code> and <code style="user-select: auto;">n</code> are <strong style="user-select: auto;">even</strong> integers.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= grid[i][j] &lt;=<sup style="user-select: auto;"> </sup>5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul></div>