<h2><a href="https://leetcode.com/problems/linked-list-in-binary-tree/">1367. Linked List in Binary Tree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a binary tree <code style="user-select: auto;">root</code> and a&nbsp;linked list with&nbsp;<code style="user-select: auto;">head</code>&nbsp;as the first node.&nbsp;</p>

<p style="user-select: auto;">Return True if all the elements in the linked list starting from the <code style="user-select: auto;">head</code> correspond to some <em style="user-select: auto;">downward path</em> connected in the binary tree&nbsp;otherwise return False.</p>

<p style="user-select: auto;">In this context downward path means a path that starts at some node and goes downwards.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png" style="width: 220px; height: 280px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Nodes in blue form a subpath in the binary Tree.  
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/sample_2_1720.png" style="width: 220px; height: 280px; user-select: auto;" title=""></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> There is no path in the binary tree that contains all the elements of the linked list from <code style="user-select: auto;">head</code>.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree will be in the range <code style="user-select: auto;">[1, 2500]</code>.</li>
	<li style="user-select: auto;">The number of nodes in the list will be in the range <code style="user-select: auto;">[1, 100]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= Node.val&nbsp;&lt;= 100</code>&nbsp;for each node in the linked list and binary tree.</li>
</ul>
</div>