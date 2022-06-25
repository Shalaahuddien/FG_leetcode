<h2><a href="https://leetcode.com/problems/non-decreasing-array/">665. Non-decreasing Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array <code style="user-select: auto;">nums</code> with <code style="user-select: auto;">n</code> integers, your task is to check if it could become non-decreasing by modifying <strong style="user-select: auto;">at most one element</strong>.</p>

<p style="user-select: auto;">We define an array is non-decreasing if <code style="user-select: auto;">nums[i] &lt;= nums[i + 1]</code> holds for every <code style="user-select: auto;">i</code> (<strong style="user-select: auto;">0-based</strong>) such that (<code style="user-select: auto;">0 &lt;= i &lt;= n - 2</code>).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [4,2,3]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> You could modify the first <code style="user-select: auto;">4</code> to <code style="user-select: auto;">1</code> to get a non-decreasing array.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [4,2,1]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> You can't get a non-decreasing array by modify at most one element.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>