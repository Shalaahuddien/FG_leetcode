<h2><a href="https://leetcode.com/problems/diameter-of-n-ary-tree/">1522. Diameter of N-Ary Tree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <code style="user-select: auto;">root</code> of an <a href="https://leetcode.com/articles/introduction-to-n-ary-trees/" target="_blank" style="user-select: auto;">N-ary tree</a>, you need to compute the length of the diameter of the tree.</p>

<p style="user-select: auto;">The diameter of an N-ary tree is the length of the <strong style="user-select: auto;">longest</strong> path between any two nodes in the tree. This path may or may not pass through the root.</p>

<p style="user-select: auto;">(<em style="user-select: auto;">Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/07/19/sample_2_1897.png" style="width: 324px; height: 173px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation: </strong>Diameter is shown in red color.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/07/19/sample_1_1897.png" style="width: 253px; height: 246px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,2,null,3,4,null,5,null,6]
<strong style="user-select: auto;">Output:</strong> 4
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/07/19/sample_3_1897.png" style="width: 369px; height: 326px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong style="user-select: auto;">Output:</strong> 7
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The depth of the n-ary tree is less than or equal to <code style="user-select: auto;">1000</code>.</li>
	<li style="user-select: auto;">The total number of nodes is between <code style="user-select: auto;">[1, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
</ul>
</div>