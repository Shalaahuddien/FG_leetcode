<h2><a href="https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/">1373. Maximum Sum BST in Binary Tree</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <strong style="user-select: auto;">binary tree</strong> <code style="user-select: auto;">root</code>, return <em style="user-select: auto;">the maximum sum of all keys of <strong style="user-select: auto;">any</strong> sub-tree which is also a Binary Search Tree (BST)</em>.</p>

<p style="user-select: auto;">Assume a BST is defined as follows:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The left subtree of a node contains only nodes with keys <strong style="user-select: auto;">less than</strong> the node's key.</li>
	<li style="user-select: auto;">The right subtree of a node contains only nodes with keys <strong style="user-select: auto;">greater than</strong> the node's key.</li>
	<li style="user-select: auto;">Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/01/30/sample_1_1709.png" style="width: 320px; height: 250px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
<strong style="user-select: auto;">Output:</strong> 20
<strong style="user-select: auto;">Explanation:</strong> Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/01/30/sample_2_1709.png" style="width: 134px; height: 180px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [4,3,null,1,2]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [-4,-2,-5]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> All values are negatives. Return an empty BST.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[1, 4 * 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-4 * 10<sup style="user-select: auto;">4</sup> &lt;= Node.val &lt;= 4 * 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>