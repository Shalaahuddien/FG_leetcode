<h2><a href="https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/">1509. Minimum Difference Between Largest and Smallest Value in Three Moves</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">nums</code>. In one move, you can choose one element of <code style="user-select: auto;">nums</code> and change it by <strong style="user-select: auto;">any value</strong>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the minimum difference between the largest and smallest value of <code style="user-select: auto;">nums</code> after performing <strong style="user-select: auto;">at most three moves</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [5,3,2,4]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> Change the array [5,3,2,4] to [<strong style="user-select: auto;">2</strong>,<strong style="user-select: auto;">2</strong>,2,<strong style="user-select: auto;">2</strong>].
The difference between the maximum and minimum is 2-2 = 0.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,5,0,10,14]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> Change the array [1,5,0,10,14] to [1,<strong style="user-select: auto;">1</strong>,0,<strong style="user-select: auto;">1</strong>,<strong style="user-select: auto;">1</strong>]. 
The difference between the maximum and minimum is 1-0 = 1.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>