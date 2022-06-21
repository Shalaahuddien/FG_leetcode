<h2><a href="https://leetcode.com/problems/furthest-building-you-can-reach/">1642. Furthest Building You Can Reach</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">heights</code> representing the heights of buildings, some <code style="user-select: auto;">bricks</code>, and some <code style="user-select: auto;">ladders</code>.</p>

<p style="user-select: auto;">You start your journey from building <code style="user-select: auto;">0</code> and move to the next building by possibly using bricks or ladders.</p>

<p style="user-select: auto;">While moving from building <code style="user-select: auto;">i</code> to building <code style="user-select: auto;">i+1</code> (<strong style="user-select: auto;">0-indexed</strong>),</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If the current building's height is <strong style="user-select: auto;">greater than or equal</strong> to the next building's height, you do <strong style="user-select: auto;">not</strong> need a ladder or bricks.</li>
	<li style="user-select: auto;">If the current building's height is <b style="user-select: auto;">less than</b> the next building's height, you can either use <strong style="user-select: auto;">one ladder</strong> or <code style="user-select: auto;">(h[i+1] - h[i])</code> <strong style="user-select: auto;">bricks</strong>.</li>
</ul>

<p style="user-select: auto;"><em style="user-select: auto;">Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/27/q4.gif" style="width: 562px; height: 561px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 &gt;= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 &lt; 7.
- Go to building 3 without using ladders nor bricks since 7 &gt;= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 &lt; 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
<strong style="user-select: auto;">Output:</strong> 7
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [14,3,19,3], bricks = 17, ladders = 0
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= heights.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= heights[i] &lt;= 10<sup style="user-select: auto;">6</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= bricks &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= ladders &lt;= heights.length</code></li>
</ul>
</div>