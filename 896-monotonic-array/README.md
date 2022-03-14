<h2><a href="https://leetcode.com/problems/monotonic-array/">896. Monotonic Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">An array is <strong style="user-select: auto;">monotonic</strong> if it is either monotone increasing or monotone decreasing.</p>

<p style="user-select: auto;">An array <code style="user-select: auto;">nums</code> is monotone increasing if for all <code style="user-select: auto;">i &lt;= j</code>, <code style="user-select: auto;">nums[i] &lt;= nums[j]</code>. An array <code style="user-select: auto;">nums</code> is monotone decreasing if for all <code style="user-select: auto;">i &lt;= j</code>, <code style="user-select: auto;">nums[i] &gt;= nums[j]</code>.</p>

<p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if the given array is monotonic, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,2,3]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [6,5,4,4]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,3,2]
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>