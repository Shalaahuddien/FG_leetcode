<h2><a href="https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/">1628. Design an Expression Tree With Evaluate Function</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">postfix</code> tokens of an arithmetic expression, build and return <em style="user-select: auto;">the binary expression tree that represents this expression.</em></p>

<p style="user-select: auto;"><b style="user-select: auto;">Postfix</b> notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression <code style="user-select: auto;">4*(5-(7+2))</code> are represented in the array <code style="user-select: auto;">postfix = ["4","5","7","2","+","-","*"]</code>.</p>

<p style="user-select: auto;">The class <code style="user-select: auto;">Node</code> is an interface you should use to implement the binary expression tree. The returned tree will be tested using the <code style="user-select: auto;">evaluate</code> function, which is supposed to evaluate the tree's value. You should not remove the <code style="user-select: auto;">Node</code> class; however, you can modify it as you wish, and you can define other classes to implement it if needed.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/Binary_expression_tree" target="_blank" style="user-select: auto;">binary expression tree</a></strong> is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators <code style="user-select: auto;">'+'</code> (addition), <code style="user-select: auto;">'-'</code> (subtraction), <code style="user-select: auto;">'*'</code> (multiplication), and <code style="user-select: auto;">'/'</code> (division).</p>

<p style="user-select: auto;">It's guaranteed that no subtree will yield a value that exceeds <code style="user-select: auto;">10<sup style="user-select: auto;">9</sup></code> in absolute value, and all the operations are valid (i.e., no division by zero).</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing <code style="user-select: auto;">evaluate</code> implementation?</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/untitled-diagram.png" style="width: 242px; height: 241px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = ["3","4","+","2","*","7","/"]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> this expression evaluates to the above binary tree with expression (<code style="user-select: auto;">(3+4)*2)/7) = 14/7 = 2.</code>
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/untitled-diagram2.png" style="width: 222px; height: 232px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = ["4","5","2","7","+","-","*"]
<strong style="user-select: auto;">Output:</strong> -16
<strong style="user-select: auto;">Explanation:</strong> this expression evaluates to the above binary tree with expression 4*(5-<code style="user-select: auto;">(2+7)) = 4*(-4) = -16.</code>
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt; 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s.length</code> is odd.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of numbers and the characters <code style="user-select: auto;">'+'</code>, <code style="user-select: auto;">'-'</code>, <code style="user-select: auto;">'*'</code>, and <code style="user-select: auto;">'/'</code>.</li>
	<li style="user-select: auto;">If <code style="user-select: auto;">s[i]</code> is a number, its integer representation is no more than <code style="user-select: auto;">10<sup style="user-select: auto;">5</sup></code>.</li>
	<li style="user-select: auto;">It is guaranteed that <code style="user-select: auto;">s</code> is a valid expression.</li>
	<li style="user-select: auto;">The absolute value of the result and intermediate values will not exceed <code style="user-select: auto;">10<sup style="user-select: auto;">9</sup></code>.</li>
	<li style="user-select: auto;">It is guaranteed that no expression will include division by zero.</li>
</ul>
</div>