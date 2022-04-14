<h2><a href="https://leetcode.com/problems/leaf-similar-trees/">872. Leaf-Similar Trees</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Consider all the leaves of a binary tree, from&nbsp;left to right order, the values of those&nbsp;leaves form a <strong style="user-select: auto;">leaf value sequence</strong><em style="user-select: auto;">.</em></p>

<p style="user-select: auto;"><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 400px; height: 336px; user-select: auto;" title=""></p>

<p style="user-select: auto;">For example, in the given tree above, the leaf value sequence is <code style="user-select: auto;">(6, 7, 4, 9, 8)</code>.</p>

<p style="user-select: auto;">Two binary trees are considered <em style="user-select: auto;">leaf-similar</em>&nbsp;if their leaf value sequence is the same.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> if and only if the two given trees with head nodes <code style="user-select: auto;">root1</code> and <code style="user-select: auto;">root2</code> are leaf-similar.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg" style="width: 600px; height: 237px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg" style="width: 300px; height: 110px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root1 = [1,2,3], root2 = [1,3,2]
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in each tree will be in the range <code style="user-select: auto;">[1, 200]</code>.</li>
	<li style="user-select: auto;">Both of the given trees will have values in the range <code style="user-select: auto;">[0, 200]</code>.</li>
</ul>
</div>