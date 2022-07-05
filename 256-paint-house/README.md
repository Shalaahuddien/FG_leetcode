<h2><a href="https://leetcode.com/problems/paint-house/">256. Paint House</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is a row of <code style="user-select: auto;">n</code> houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.</p>

<p style="user-select: auto;">The cost of painting each house with a certain color is represented by an <code style="user-select: auto;">n x 3</code> cost matrix <code style="user-select: auto;">costs</code>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">costs[0][0]</code> is the cost of painting house <code style="user-select: auto;">0</code> with the color red; <code style="user-select: auto;">costs[1][2]</code> is the cost of painting house 1 with color green, and so on...</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the minimum cost to paint all houses</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> costs = [[17,2,17],[16,16,5],[14,3,19]]
<strong style="user-select: auto;">Output:</strong> 10
<strong style="user-select: auto;">Explanation:</strong> Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> costs = [[7,6,2]]
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">costs.length == n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">costs[i].length == 3</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= costs[i][j] &lt;= 20</code></li>
</ul>
</div>