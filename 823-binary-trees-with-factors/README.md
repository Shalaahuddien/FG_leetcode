<h2><a href="https://leetcode.com/problems/binary-trees-with-factors/">823. Binary Trees With Factors</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of unique integers, <code style="user-select: auto;">arr</code>, where each integer <code style="user-select: auto;">arr[i]</code> is strictly greater than <code style="user-select: auto;">1</code>.</p>

<p style="user-select: auto;">We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of binary trees we can make</em>. The answer may be too large so return the answer <strong style="user-select: auto;">modulo</strong> <code style="user-select: auto;">10<sup style="user-select: auto;">9</sup> + 7</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [2,4]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> We can make these trees: <code style="user-select: auto;">[2], [4], [4, 2, 2]</code></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [2,4,5,10]
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation:</strong> We can make these trees: <code style="user-select: auto;">[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= arr[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;">All the values of <code style="user-select: auto;">arr</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>