<h2><a href="https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/">1437. Check If All 1's Are at Least Length K Places Away</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an binary array <code style="user-select: auto;">nums</code> and an integer <code style="user-select: auto;">k</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if all </em><code style="user-select: auto;">1</code><em style="user-select: auto;">'s are at least </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> places away from each other, otherwise return </em><code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 428px; height: 181px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,0,0,0,1,0,0,1], k = 2
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Each of the 1s are at least 2 places away from each other.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 320px; height: 173px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> The second 1 and third 1 are only one apart from each other.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= k &lt;= nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i]</code> is <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code></li>
</ul>
</div>