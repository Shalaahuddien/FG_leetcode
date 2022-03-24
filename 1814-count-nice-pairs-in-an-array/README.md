<h2><a href="https://leetcode.com/problems/count-nice-pairs-in-an-array/">1814. Count Nice Pairs in an Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an array <code style="user-select: auto;">nums</code> that consists of non-negative integers. Let us define <code style="user-select: auto;">rev(x)</code> as the reverse of the non-negative integer <code style="user-select: auto;">x</code>. For example, <code style="user-select: auto;">rev(123) = 321</code>, and <code style="user-select: auto;">rev(120) = 21</code>. A pair of indices <code style="user-select: auto;">(i, j)</code> is <strong style="user-select: auto;">nice</strong> if it satisfies all of the following conditions:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= i &lt; j &lt; nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])</code></li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of nice pairs of indices</em>. Since that number can be too large, return it <strong style="user-select: auto;">modulo</strong> <code style="user-select: auto;">10<sup style="user-select: auto;">9</sup> + 7</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [42,11,1,97]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [13,10,35,24,76]
<strong style="user-select: auto;">Output:</strong> 4
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>