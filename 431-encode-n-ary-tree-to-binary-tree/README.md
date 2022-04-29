<h2><a href="https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/">431. Encode N-ary Tree to Binary Tree</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.</p>

<p style="user-select: auto;"><em style="user-select: auto;">Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See following example).</em></p>

<p style="user-select: auto;">For example, you may encode the following <code style="user-select: auto;">3-ary</code> tree to a binary tree in this way:</p>

<p style="user-select: auto;"><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreebinarytreeexample.png" style="width: 100%; max-width: 640px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,3,2,4,null,5,6]
</pre>

<p style="user-select: auto;">Note that the above is just an example which <em style="user-select: auto;">might or might not</em> work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong style="user-select: auto;">Output:</strong> [1,null,3,2,4,null,5,6]
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong style="user-select: auto;">Output:</strong> [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = []
<strong style="user-select: auto;">Output:</strong> []
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[0, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;">The height of the n-ary tree is less than or equal to <code style="user-select: auto;">1000</code></li>
	<li style="user-select: auto;">Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.</li>
</ul>
</div>