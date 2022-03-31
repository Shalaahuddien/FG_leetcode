<h2><a href="https://leetcode.com/problems/lucky-numbers-in-a-matrix/">1380. Lucky Numbers in a Matrix</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an <code style="user-select: auto;">m x n</code> matrix of <strong style="user-select: auto;">distinct </strong>numbers, return <em style="user-select: auto;">all <strong style="user-select: auto;">lucky numbers</strong> in the matrix in <strong style="user-select: auto;">any </strong>order</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">lucky number</strong> is an element of the matrix such that it is the minimum element in its row and maximum in its column.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[3,7,8],[9,11,13],[15,16,17]]
<strong style="user-select: auto;">Output:</strong> [15]
<strong style="user-select: auto;">Explanation:</strong> 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
<strong style="user-select: auto;">Output:</strong> [12]
<strong style="user-select: auto;">Explanation:</strong> 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[7,8],[1,2]]
<strong style="user-select: auto;">Output:</strong> [7]
<strong style="user-select: auto;">Explanation:</strong> 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == mat.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == mat[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n, m &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= matrix[i][j] &lt;= 10<sup style="user-select: auto;">5</sup></code>.</li>
	<li style="user-select: auto;">All elements in the matrix are distinct.</li>
</ul>
</div>