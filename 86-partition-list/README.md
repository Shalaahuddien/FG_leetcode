<h2><a href="https://leetcode.com/problems/partition-list/">86. Partition List</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">head</code> of a linked list and a value <code style="user-select: auto;">x</code>, partition it such that all nodes <strong style="user-select: auto;">less than</strong> <code style="user-select: auto;">x</code> come before nodes <strong style="user-select: auto;">greater than or equal</strong> to <code style="user-select: auto;">x</code>.</p>

<p style="user-select: auto;">You should <strong style="user-select: auto;">preserve</strong> the original relative order of the nodes in each of the two partitions.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,4,3,2,5,2], x = 3
<strong style="user-select: auto;">Output:</strong> [1,2,2,4,3,5]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [2,1], x = 2
<strong style="user-select: auto;">Output:</strong> [1,2]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the list is in the range <code style="user-select: auto;">[0, 200]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= Node.val &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-200 &lt;= x &lt;= 200</code></li>
</ul>
</div>