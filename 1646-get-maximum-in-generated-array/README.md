<h2><a href="https://leetcode.com/problems/get-maximum-in-generated-array/">1646. Get Maximum in Generated Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer <code style="user-select: auto;">n</code>. A <strong style="user-select: auto;">0-indexed</strong> integer array <code style="user-select: auto;">nums</code> of length <code style="user-select: auto;">n + 1</code> is generated in the following way:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">nums[0] = 0</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[1] = 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[2 * i] = nums[i]</code> when <code style="user-select: auto;">2 &lt;= 2 * i &lt;= n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[2 * i + 1] = nums[i] + nums[i + 1]</code> when <code style="user-select: auto;">2 &lt;= 2 * i + 1 &lt;= n</code></li>
</ul>

<p style="user-select: auto;">Return<strong style="user-select: auto;"> </strong><em style="user-select: auto;">the <strong style="user-select: auto;">maximum</strong> integer in the array </em><code style="user-select: auto;">nums</code>​​​.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 7
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 2
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 3
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= n &lt;= 100</code></li>
</ul>
</div>