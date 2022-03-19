<h2><a href="https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/">1612. Check If Two Expression Trees are Equivalent</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/Binary_expression_tree" target="_blank" style="user-select: auto;">binary expression tree</a></strong> is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the <code style="user-select: auto;">'+'</code> operator (i.e. addition).</p>

<p style="user-select: auto;">You are given the roots of two binary expression trees, <code style="user-select: auto;">root1</code> and <code style="user-select: auto;">root2</code>. Return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if the two binary expression trees are equivalent</em>. Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">Two binary expression trees are equivalent if they <strong style="user-select: auto;">evaluate to the same value</strong> regardless of what the variables are set to.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root1 = [x], root2 = [x]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/tree1.png" style="width: 211px; height: 131px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,c]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explaination:</strong> <code style="user-select: auto;">a + (b + c) == (b + c) + a</code></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/tree2.png" style="width: 211px; height: 131px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,d]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explaination:</strong> <code style="user-select: auto;">a + (b + c) != (b + d) + a</code>
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in both trees are equal, odd and, in the range <code style="user-select: auto;">[1, 4999]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">Node.val</code> is <code style="user-select: auto;">'+'</code> or a lower-case English letter.</li>
	<li style="user-select: auto;">It's <strong style="user-select: auto;">guaranteed</strong> that the tree given is a valid binary expression tree.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> What will you change in your solution if the tree also supports the <code style="user-select: auto;">'-'</code> operator (i.e. subtraction)?</p>
</div>