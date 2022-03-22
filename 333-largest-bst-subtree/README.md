<h2><a href="https://leetcode.com/problems/largest-bst-subtree/">333. Largest BST Subtree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">Binary Search Tree (BST)</strong> is a tree in which all the nodes follow the below-mentioned properties:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The left subtree values are less than the value of their parent (root) node's value.</li>
	<li style="user-select: auto;">The right subtree values are greater than the value of their parent (root) node's value.</li>
</ul>

<p style="user-select: auto;"><strong style="user-select: auto;">Note:</strong> A subtree must include all of its descendants.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/10/17/tmp.jpg" style="width: 571px; height: 302px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [10,5,15,1,8,null,7]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation: </strong>The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[0, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">4</sup> &lt;= Node.val &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Can you figure out ways to solve it with <code style="user-select: auto;">O(n)</code> time complexity?</p>
</div>