<h2><a href="https://leetcode.com/problems/build-array-from-permutation/">1920. Build Array from Permutation</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <strong style="user-select: auto;">zero-based permutation</strong> <code style="user-select: auto;">nums</code> (<strong style="user-select: auto;">0-indexed</strong>), build an array <code style="user-select: auto;">ans</code> of the <strong style="user-select: auto;">same length</strong> where <code style="user-select: auto;">ans[i] = nums[nums[i]]</code> for each <code style="user-select: auto;">0 &lt;= i &lt; nums.length</code> and return it.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">zero-based permutation</strong> <code style="user-select: auto;">nums</code> is an array of <strong style="user-select: auto;">distinct</strong> integers from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">nums.length - 1</code> (<strong style="user-select: auto;">inclusive</strong>).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0,2,1,5,3,4]
<strong style="user-select: auto;">Output:</strong> [0,1,2,4,5,3]<strong style="user-select: auto;">
Explanation:</strong> The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [5,0,1,2,3,4]
<strong style="user-select: auto;">Output:</strong> [4,5,0,1,2,3]
<strong style="user-select: auto;">Explanation:</strong> The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums[i] &lt; nums.length</code></li>
	<li style="user-select: auto;">The elements in <code style="user-select: auto;">nums</code> are <strong style="user-select: auto;">distinct</strong>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow-up:</strong> Can you solve it without using an extra space (i.e., <code style="user-select: auto;">O(1)</code> memory)?</p>
</div>