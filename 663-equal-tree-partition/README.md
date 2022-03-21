<h2><a href="https://leetcode.com/problems/equal-tree-partition/">663. Equal Tree Partition</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">root</code> of a binary tree, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if you can partition the tree into two trees with equal sums of values after removing exactly one edge on the original tree</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/split1-tree.jpg" style="width: 500px; height: 204px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [5,10,10,null,null,2,3]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/split2-tree.jpg" style="width: 277px; height: 302px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,2,10,null,null,2,20]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> You cannot split the tree into two trees with equal sums after removing exactly one edge on the tree.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[1, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= Node.val &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>