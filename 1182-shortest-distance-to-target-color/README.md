<h2><a href="https://leetcode.com/problems/shortest-distance-to-target-color/">1182. Shortest Distance to Target Color</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an array <code style="user-select: auto;">colors</code>, in which there are three colors: <code style="user-select: auto;">1</code>, <code style="user-select: auto;">2</code> and&nbsp;<code style="user-select: auto;">3</code>.</p>

<p style="user-select: auto;">You are also given some queries. Each query consists of two integers <code style="user-select: auto;">i</code>&nbsp;and <code style="user-select: auto;">c</code>, return&nbsp;the shortest distance between the given index&nbsp;<code style="user-select: auto;">i</code> and the target color <code style="user-select: auto;">c</code>. If there is no solution return <code style="user-select: auto;">-1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
<strong style="user-select: auto;">Output:</strong> [3,0,3]
<strong style="user-select: auto;">Explanation: </strong>
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> colors = [1,2], queries = [[0,3]]
<strong style="user-select: auto;">Output:</strong> [-1]
<strong style="user-select: auto;">Explanation: </strong>There is no 3 in the array.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= colors.length &lt;= 5*10^4</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= colors[i] &lt;= 3</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1&nbsp;&lt;= queries.length &lt;= 5*10^4</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">queries[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= queries[i][0] &lt;&nbsp;colors.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= queries[i][1] &lt;= 3</code></li>
</ul>
</div>