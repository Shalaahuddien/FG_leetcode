<h2><a href="https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/">1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a binary tree where each path going from the root to any leaf form a <strong style="user-select: auto;">valid sequence</strong>, check if a given string&nbsp;is a <strong style="user-select: auto;">valid sequence</strong> in such binary tree.&nbsp;</p>

<p style="user-select: auto;">We get the given string from the concatenation of an array of integers <code style="user-select: auto;">arr</code> and the concatenation of all&nbsp;values of the nodes along a path results in a <strong style="user-select: auto;">sequence</strong> in the given binary tree.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/leetcode_testcase_1.png" style="width: 333px; height: 250px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation: 
</strong>The path 0 -&gt; 1 -&gt; 0 -&gt; 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -&gt; 1 -&gt; 1 -&gt; 0 
0 -&gt; 0 -&gt; 0
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/leetcode_testcase_2.png" style="width: 333px; height: 250px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
<strong style="user-select: auto;">Output:</strong> false 
<strong style="user-select: auto;">Explanation:</strong> The path 0 -&gt; 0 -&gt; 1 does not exist, therefore it is not even a sequence.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/leetcode_testcase_3.png" style="width: 333px; height: 250px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation: </strong>The path 0 -&gt; 1 -&gt; 1 is a sequence, but it is not a valid sequence.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr.length &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= arr[i] &lt;= 9</code></li>
	<li style="user-select: auto;">Each node's value is between [0 - 9].</li>
</ul>
</div>