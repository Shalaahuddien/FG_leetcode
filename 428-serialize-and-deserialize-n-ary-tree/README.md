<h2><a href="https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/">428. Serialize and Deserialize N-ary Tree</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p style="user-select: auto;">Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p style="user-select: auto;">For example, you may serialize the following <code style="user-select: auto;">3-ary</code> tree</p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 500px; max-width: 300px; height: 321px; user-select: auto;">
<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;">as <code style="user-select: auto;">[1 [3[5 6] 2 4]]</code>. Note that this is just an example, you do not necessarily need to follow this format.</p>

<p style="user-select: auto;">Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 500px; height: 454px; user-select: auto;">
<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;">For example, the above tree may be serialized as <code style="user-select: auto;">[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]</code>.</p>

<p style="user-select: auto;">You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong style="user-select: auto;">Output:</strong> [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong style="user-select: auto;">Output:</strong> [1,null,3,2,4,null,5,6]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

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