<h2><a href="https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/">1597. Build Binary Expression Tree From Infix Expression</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/Binary_expression_tree" target="_blank" style="user-select: auto;">binary expression tree</a></strong> is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators <code style="user-select: auto;">'+'</code> (addition), <code style="user-select: auto;">'-'</code> (subtraction), <code style="user-select: auto;">'*'</code> (multiplication), and <code style="user-select: auto;">'/'</code> (division).</p>

<p style="user-select: auto;">For each internal node with operator <code style="user-select: auto;">o</code>, the <a href="https://en.wikipedia.org/wiki/Infix_notation" target="_blank" style="user-select: auto;"><strong style="user-select: auto;">infix expression</strong></a> that it represents is <code style="user-select: auto;">(A o B)</code>, where <code style="user-select: auto;">A</code> is the expression the left subtree represents and <code style="user-select: auto;">B</code> is the expression the right subtree represents.</p>

<p style="user-select: auto;">You are given a string <code style="user-select: auto;">s</code>, an <strong style="user-select: auto;">infix expression</strong> containing operands, the operators described above, and parentheses <code style="user-select: auto;">'('</code> and <code style="user-select: auto;">')'</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">any valid&nbsp;<strong style="user-select: auto;">binary expression tree</strong>,&nbsp;which its <strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)" target="_blank" style="user-select: auto;">in-order traversal</a></strong>&nbsp;reproduces&nbsp;</em><code style="user-select: auto;">s</code>&nbsp;after omitting&nbsp;the parenthesis from it (see examples below)<em style="user-select: auto;">.</em></p>

<p style="user-select: auto;"><strong style="user-select: auto;">Please note that order of operations applies in </strong><code style="user-select: auto;">s</code><strong style="user-select: auto;">.</strong> That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.</p>

<p style="user-select: auto;">Operands must also appear in the <strong style="user-select: auto;">same order</strong> in both <code style="user-select: auto;">s</code>&nbsp;and the in-order traversal of the tree.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1-4.png" style="width: 250px; height: 161px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "3*4-2*5"
<strong style="user-select: auto;">Output:</strong> [-,*,*,3,4,2,5]
<strong style="user-select: auto;">Explanation:</strong> The tree above is the only valid tree whose inorder traversal produces s.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1-2.png" style="width: 150px; height: 210px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "2-3/(5*2)+1"
<strong style="user-select: auto;">Output:</strong> [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
<strong style="user-select: auto;">Explanation:</strong> The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid answer because it does not evaluate to the same value.
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1-1.png" style="width: 201px; height: 281px; user-select: auto;">
The third tree below is also not valid. Although it produces the same result and is equivalent to the above trees, its inorder traversal does not produce s and its operands are not in the same order as s.
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1-3.png" style="width: 281px; height: 281px; user-select: auto;">
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "1+2+3+4+5"
<strong style="user-select: auto;">Output:</strong> [+,+,5,+,4,null,null,+,3,null,null,1,2]
<strong style="user-select: auto;">Explanation:</strong> The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of digits and the characters <code style="user-select: auto;">'+'</code>, <code style="user-select: auto;">'-'</code>, <code style="user-select: auto;">'*'</code>, and <code style="user-select: auto;">'/'</code>.</li>
	<li style="user-select: auto;">Operands in <code style="user-select: auto;">s</code> are <strong style="user-select: auto;">exactly</strong> 1 digit.</li>
	<li style="user-select: auto;">It is guaranteed that <code style="user-select: auto;">s</code> is a valid expression.</li>
</ul>
</div>