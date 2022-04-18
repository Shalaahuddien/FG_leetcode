<h2><a href="https://leetcode.com/problems/binary-search-tree-iterator-ii/">1586. Binary Search Tree Iterator II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Implement the <code style="user-select: auto;">BSTIterator</code> class that represents an iterator over the <strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)" style="user-select: auto;">in-order traversal</a></strong> of a binary search tree (BST):</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">BSTIterator(TreeNode root)</code> Initializes an object of the <code style="user-select: auto;">BSTIterator</code> class. The <code style="user-select: auto;">root</code> of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean hasNext()</code> Returns <code style="user-select: auto;">true</code> if there exists a number in the traversal to the right of the pointer, otherwise returns <code style="user-select: auto;">false</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int next()</code> Moves the pointer to the right, then returns the number at the pointer.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean hasPrev()</code> Returns <code style="user-select: auto;">true</code> if there exists a number in the traversal to the left of the pointer, otherwise returns <code style="user-select: auto;">false</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int prev()</code> Moves the pointer to the left, then returns the number at the pointer.</li>
</ul>

<p style="user-select: auto;">Notice that by initializing the pointer to a non-existent smallest number, the first call to <code style="user-select: auto;">next()</code> will return the smallest element in the BST.</p>

<p style="user-select: auto;">You may assume that <code style="user-select: auto;">next()</code> and <code style="user-select: auto;">prev()</code> calls will always be valid. That is, there will be at least a next/previous number in the in-order traversal when <code style="user-select: auto;">next()</code>/<code style="user-select: auto;">prev()</code> is called.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/untitled-diagram-1.png" style="width: 201px; height: 201px; user-select: auto;"></strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["BSTIterator", "next", "next", "prev", "next", "hasNext", "next", "next", "next", "hasNext", "hasPrev", "prev", "prev"]
[[[7, 3, 15, null, null, 9, 20]], [null], [null], [null], [null], [null], [null], [null], [null], [null], [null], [null], [null]]
<strong style="user-select: auto;">Output</strong>
[null, 3, 7, 3, 7, true, 9, 15, 20, false, true, 15, 9]

<strong style="user-select: auto;">Explanation</strong>
// The underlined element is where the pointer currently is.
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]); // state is <u style="user-select: auto;"> </u> [3, 7, 9, 15, 20]
bSTIterator.next(); // state becomes [<u style="user-select: auto;">3</u>, 7, 9, 15, 20], return 3
bSTIterator.next(); // state becomes [3, <u style="user-select: auto;">7</u>, 9, 15, 20], return 7
bSTIterator.prev(); // state becomes [<u style="user-select: auto;">3</u>, 7, 9, 15, 20], return 3
bSTIterator.next(); // state becomes [3, <u style="user-select: auto;">7</u>, 9, 15, 20], return 7
bSTIterator.hasNext(); // return true
bSTIterator.next(); // state becomes [3, 7, <u style="user-select: auto;">9</u>, 15, 20], return 9
bSTIterator.next(); // state becomes [3, 7, 9, <u style="user-select: auto;">15</u>, 20], return 15
bSTIterator.next(); // state becomes [3, 7, 9, 15, <u style="user-select: auto;">20</u>], return 20
bSTIterator.hasNext(); // return false
bSTIterator.hasPrev(); // return true
bSTIterator.prev(); // state becomes [3, 7, 9, <u style="user-select: auto;">15</u>, 20], return 15
bSTIterator.prev(); // state becomes [3, 7, <u style="user-select: auto;">9</u>, 15, 20], return 9
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[1, 10<sup style="user-select: auto;">5</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt;= 10<sup style="user-select: auto;">6</sup></code></li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">10<sup style="user-select: auto;">5</sup></code> calls will be made to <code style="user-select: auto;">hasNext</code>, <code style="user-select: auto;">next</code>, <code style="user-select: auto;">hasPrev</code>, and <code style="user-select: auto;">prev</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Could you solve the problem without precalculating the values of the tree?</div>