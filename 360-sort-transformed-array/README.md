<h2><a href="https://leetcode.com/problems/sort-transformed-array/">360. Sort Transformed Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <strong style="user-select: auto;">sorted</strong> integer array <code style="user-select: auto;">nums</code> and three integers <code style="user-select: auto;">a</code>, <code style="user-select: auto;">b</code> and <code style="user-select: auto;">c</code>, apply a quadratic function of the form <code style="user-select: auto;">f(x) = ax<sup style="user-select: auto;">2</sup> + bx + c</code> to each element <code style="user-select: auto;">nums[i]</code> in the array, and return <em style="user-select: auto;">the array in a sorted order</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [-4,-2,2,4], a = 1, b = 3, c = 5
<strong style="user-select: auto;">Output:</strong> [3,9,15,33]
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [-4,-2,2,4], a = -1, b = 3, c = 5
<strong style="user-select: auto;">Output:</strong> [-23,-5,1,7]
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= nums[i], a, b, c &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums</code> is sorted in <strong style="user-select: auto;">ascending</strong> order.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Could you solve it in <code style="user-select: auto;">O(n)</code> time?</p>
</div>