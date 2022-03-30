<h2><a href="https://leetcode.com/problems/longest-harmonious-subsequence/">594. Longest Harmonious Subsequence</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">We define a harmonious array as an array where the difference between its maximum value and its minimum value is <b style="user-select: auto;">exactly</b> <code style="user-select: auto;">1</code>.</p>

<p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code>, return <em style="user-select: auto;">the length of its longest harmonious subsequence among all its possible subsequences</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">subsequence</strong> of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,3,2,2,5,2,3,7]
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong> The longest harmonious subsequence is [3,2,2,2,3].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,4]
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,1,1,1]
<strong style="user-select: auto;">Output:</strong> 0
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 2 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul></div>