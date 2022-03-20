<h2><a href="https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/">1886. Determine Whether Matrix Can Be Obtained By Rotation</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two <code style="user-select: auto;">n x n</code> binary matrices <code style="user-select: auto;">mat</code> and <code style="user-select: auto;">target</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if it is possible to make </em><code style="user-select: auto;">mat</code><em style="user-select: auto;"> equal to </em><code style="user-select: auto;">target</code><em style="user-select: auto;"> by <strong style="user-select: auto;">rotating</strong> </em><code style="user-select: auto;">mat</code><em style="user-select: auto;"> in <strong style="user-select: auto;">90-degree increments</strong>, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation: </strong>We can rotate mat 90 degrees clockwise to make mat equal target.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> It is impossible to make mat equal to target by rotating mat.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation: </strong>We can rotate mat 90 degrees clockwise two times to make mat equal target.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == mat.length == target.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == mat[i].length == target[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">mat[i][j]</code> and <code style="user-select: auto;">target[i][j]</code> are either <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
</ul>
</div>