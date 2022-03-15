<h2><a href="https://leetcode.com/problems/trapping-rain-water-ii/">407. Trapping Rain Water II</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an <code style="user-select: auto;">m x n</code> integer matrix <code style="user-select: auto;">heightMap</code> representing the height of each unit cell in a 2D elevation map, return <em style="user-select: auto;">the volume of water it can trap after raining</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg" style="width: 361px; height: 321px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg" style="width: 401px; height: 321px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
<strong style="user-select: auto;">Output:</strong> 10
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == heightMap.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == heightMap[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= heightMap[i][j] &lt;= 2 * 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>