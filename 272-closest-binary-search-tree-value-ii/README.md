<h2><a href="https://leetcode.com/problems/closest-binary-search-tree-value-ii/">272. Closest Binary Search Tree Value II</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">root</code> of a binary search tree, a <code style="user-select: auto;">target</code> value, and an integer <code style="user-select: auto;">k</code>, return <em style="user-select: auto;">the </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> values in the BST that are closest to the</em> <code style="user-select: auto;">target</code>. You may return the answer in <strong style="user-select: auto;">any order</strong>.</p>

<p style="user-select: auto;">You are <strong style="user-select: auto;">guaranteed</strong> to have only one unique set of <code style="user-select: auto;">k</code> values in the BST that are closest to the <code style="user-select: auto;">target</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg" style="width: 292px; height: 302px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [4,2,5,1,3], target = 3.714286, k = 2
<strong style="user-select: auto;">Output:</strong> [4,3]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1], target = 0.000000, k = 1
<strong style="user-select: auto;">Output:</strong> [1]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is <code style="user-select: auto;">n</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= n &lt;= 10<sup style="user-select: auto;">4</sup></code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= target &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Assume that the BST is balanced. Could you solve it in less than <code style="user-select: auto;">O(n)</code> runtime (where <code style="user-select: auto;">n = total nodes</code>)?</p>
</div>