<h2><a href="https://leetcode.com/problems/projection-area-of-3d-shapes/">883. Projection Area of 3D Shapes</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an <code style="user-select: auto;">n x n</code> <code style="user-select: auto;">grid</code> where we place some <code style="user-select: auto;">1 x 1 x 1</code> cubes that are axis-aligned with the <code style="user-select: auto;">x</code>, <code style="user-select: auto;">y</code>, and <code style="user-select: auto;">z</code> axes.</p>

<p style="user-select: auto;">Each value <code style="user-select: auto;">v = grid[i][j]</code> represents a tower of <code style="user-select: auto;">v</code> cubes placed on top of the cell <code style="user-select: auto;">(i, j)</code>.</p>

<p style="user-select: auto;">We view the projection of these cubes onto the <code style="user-select: auto;">xy</code>, <code style="user-select: auto;">yz</code>, and <code style="user-select: auto;">zx</code> planes.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">projection</strong> is like a shadow, that maps our <strong style="user-select: auto;">3-dimensional</strong> figure to a <strong style="user-select: auto;">2-dimensional</strong> plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the total area of all three projections</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png" style="width: 800px; height: 214px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,2],[3,4]]
<strong style="user-select: auto;">Output:</strong> 17
<strong style="user-select: auto;">Explanation:</strong> Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[2]]
<strong style="user-select: auto;">Output:</strong> 5
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,0],[0,2]]
<strong style="user-select: auto;">Output:</strong> 8
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == grid.length == grid[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>
</div>