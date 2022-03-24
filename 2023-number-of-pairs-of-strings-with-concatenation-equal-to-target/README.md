<h2><a href="https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/">2023. Number of Pairs of Strings With Concatenation Equal to Target</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of <strong style="user-select: auto;">digit</strong> strings <code style="user-select: auto;">nums</code> and a <strong style="user-select: auto;">digit</strong> string <code style="user-select: auto;">target</code>, return <em style="user-select: auto;">the number of pairs of indices </em><code style="user-select: auto;">(i, j)</code><em style="user-select: auto;"> (where </em><code style="user-select: auto;">i != j</code><em style="user-select: auto;">) such that the <strong style="user-select: auto;">concatenation</strong> of </em><code style="user-select: auto;">nums[i] + nums[j]</code><em style="user-select: auto;"> equals </em><code style="user-select: auto;">target</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = ["777","7","77","77"], target = "7777"
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = ["123","4","12","34"], target = "1234"
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = ["1","1","1"], target = "11"
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation:</strong> Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= nums.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums[i].length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= target.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i]</code> and <code style="user-select: auto;">target</code> consist of digits.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i]</code> and <code style="user-select: auto;">target</code> do not have leading zeros.</li>
</ul>
</div>