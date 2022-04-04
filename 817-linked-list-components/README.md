<h2><a href="https://leetcode.com/problems/linked-list-components/">817. Linked List Components</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given the <code style="user-select: auto;">head</code> of a linked list containing unique integer values and an integer array <code style="user-select: auto;">nums</code> that is a subset of the linked list values.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of connected components in </em><code style="user-select: auto;">nums</code><em style="user-select: auto;"> where two values are connected if they appear <strong style="user-select: auto;">consecutively</strong> in the linked list</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg" style="width: 424px; height: 65px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [0,1,2,3], nums = [0,1,3]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg" style="width: 544px; height: 65px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [0,1,2,3,4], nums = [0,3,1,4]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the linked list is <code style="user-select: auto;">n</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt; n</code></li>
	<li style="user-select: auto;">All the values <code style="user-select: auto;">Node.val</code> are <strong style="user-select: auto;">unique</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums[i] &lt; n</code></li>
	<li style="user-select: auto;">All the values of <code style="user-select: auto;">nums</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>