<h2><a href="https://leetcode.com/problems/find-the-most-competitive-subsequence/">1673. Find the Most Competitive Subsequence</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code> and a positive integer <code style="user-select: auto;">k</code>, return <em style="user-select: auto;">the most<strong style="user-select: auto;"> competitive</strong> subsequence of </em><code style="user-select: auto;">nums</code> <em style="user-select: auto;">of size </em><code style="user-select: auto;">k</code>.</p>

<p style="user-select: auto;">An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.</p>

<p style="user-select: auto;">We define that a subsequence <code style="user-select: auto;">a</code> is more <strong style="user-select: auto;">competitive</strong> than a subsequence <code style="user-select: auto;">b</code> (of the same length) if in the first position where <code style="user-select: auto;">a</code> and <code style="user-select: auto;">b</code> differ, subsequence <code style="user-select: auto;">a</code> has a number <strong style="user-select: auto;">less</strong> than the corresponding number in <code style="user-select: auto;">b</code>. For example, <code style="user-select: auto;">[1,3,4]</code> is more competitive than <code style="user-select: auto;">[1,3,5]</code> because the first position they differ is at the final number, and <code style="user-select: auto;">4</code> is less than <code style="user-select: auto;">5</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,5,2,6], k = 2
<strong style="user-select: auto;">Output:</strong> [2,6]
<strong style="user-select: auto;">Explanation:</strong> Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,4,3,3,5,4,9,6], k = 4
<strong style="user-select: auto;">Output:</strong> [2,3,3,4]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= nums.length</code></li>
</ul>
</div>