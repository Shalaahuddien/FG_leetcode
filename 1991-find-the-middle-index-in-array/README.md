<h2><a href="https://leetcode.com/problems/find-the-middle-index-in-array/">1991. Find the Middle Index in Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <strong style="user-select: auto;">0-indexed</strong> integer array <code style="user-select: auto;">nums</code>, find the <strong style="user-select: auto;">leftmost</strong> <code style="user-select: auto;">middleIndex</code> (i.e., the smallest amongst all the possible ones).</p>

<p style="user-select: auto;">A <code style="user-select: auto;">middleIndex</code> is an index where <code style="user-select: auto;">nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]</code>.</p>

<p style="user-select: auto;">If <code style="user-select: auto;">middleIndex == 0</code>, the left side sum is considered to be <code style="user-select: auto;">0</code>. Similarly, if <code style="user-select: auto;">middleIndex == nums.length - 1</code>, the right side sum is considered to be <code style="user-select: auto;">0</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">leftmost</strong> </em><code style="user-select: auto;">middleIndex</code><em style="user-select: auto;"> that satisfies the condition, or </em><code style="user-select: auto;">-1</code><em style="user-select: auto;"> if there is no such index</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,3,-1,<u style="user-select: auto;">8</u>,4]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,-1,<u style="user-select: auto;">4</u>]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,5]
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> There is no valid middleIndex.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Note:</strong> This question is the same as&nbsp;724:&nbsp;<a href="https://leetcode.com/problems/find-pivot-index/" target="_blank" style="user-select: auto;">https://leetcode.com/problems/find-pivot-index/</a></p>
</div>