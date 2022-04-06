<h2><a href="https://leetcode.com/problems/count-of-range-sum/">327. Count of Range Sum</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code> and two integers <code style="user-select: auto;">lower</code> and <code style="user-select: auto;">upper</code>, return <em style="user-select: auto;">the number of range sums that lie in</em> <code style="user-select: auto;">[lower, upper]</code> <em style="user-select: auto;">inclusive</em>.</p>

<p style="user-select: auto;">Range sum <code style="user-select: auto;">S(i, j)</code> is defined as the sum of the elements in <code style="user-select: auto;">nums</code> between indices <code style="user-select: auto;">i</code> and <code style="user-select: auto;">j</code> inclusive, where <code style="user-select: auto;">i &lt;= j</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [-2,5,-1], lower = -2, upper = 2
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0], lower = 0, upper = 0
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-2<sup style="user-select: auto;">31</sup> &lt;= nums[i] &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= lower &lt;= upper &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;">The answer is <strong style="user-select: auto;">guaranteed</strong> to fit in a <strong style="user-select: auto;">32-bit</strong> integer.</li>
</ul>
</div>