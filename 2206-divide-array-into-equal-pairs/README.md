<h2><a href="https://leetcode.com/problems/divide-array-into-equal-pairs/">2206. Divide Array Into Equal Pairs</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">nums</code> consisting of <code style="user-select: auto;">2 * n</code> integers.</p>

<p style="user-select: auto;">You need to divide <code style="user-select: auto;">nums</code> into <code style="user-select: auto;">n</code> pairs such that:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Each element belongs to <strong style="user-select: auto;">exactly one</strong> pair.</li>
	<li style="user-select: auto;">The elements present in a pair are <strong style="user-select: auto;">equal</strong>.</li>
</ul>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if nums can be divided into</em> <code style="user-select: auto;">n</code> <em style="user-select: auto;">pairs, otherwise return</em> <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,2,3,2,2,2]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,4]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">nums.length == 2 * n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums[i] &lt;= 500</code></li>
</ul>
</div>