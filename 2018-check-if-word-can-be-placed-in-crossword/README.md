<h2><a href="https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/">2018. Check if Word Can Be Placed In Crossword</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an <code style="user-select: auto;">m x n</code> matrix <code style="user-select: auto;">board</code>, representing the<strong style="user-select: auto;"> current </strong>state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), <code style="user-select: auto;">' '</code> to represent any <strong style="user-select: auto;">empty </strong>cells, and <code style="user-select: auto;">'#'</code> to represent any <strong style="user-select: auto;">blocked</strong> cells.</p>

<p style="user-select: auto;">A word can be placed<strong style="user-select: auto;"> horizontally</strong> (left to right <strong style="user-select: auto;">or</strong> right to left) or <strong style="user-select: auto;">vertically</strong> (top to bottom <strong style="user-select: auto;">or</strong> bottom to top) in the board if:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">It does not occupy a cell containing the character <code style="user-select: auto;">'#'</code>.</li>
	<li style="user-select: auto;">The cell each letter is placed in must either be <code style="user-select: auto;">' '</code> (empty) or <strong style="user-select: auto;">match</strong> the letter already on the <code style="user-select: auto;">board</code>.</li>
	<li style="user-select: auto;">There must not be any empty cells <code style="user-select: auto;">' '</code> or other lowercase letters <strong style="user-select: auto;">directly left or right</strong><strong style="user-select: auto;"> </strong>of the word if the word was placed <strong style="user-select: auto;">horizontally</strong>.</li>
	<li style="user-select: auto;">There must not be any empty cells <code style="user-select: auto;">' '</code> or other lowercase letters <strong style="user-select: auto;">directly above or below</strong> the word if the word was placed <strong style="user-select: auto;">vertically</strong>.</li>
</ul>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">word</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if </em><code style="user-select: auto;">word</code><em style="user-select: auto;"> can be placed in </em><code style="user-select: auto;">board</code><em style="user-select: auto;">, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> <strong style="user-select: auto;">otherwise</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/04/crossword-ex1-1.png" style="width: 478px; height: 180px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The word "abc" can be placed as shown above (top to bottom).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/04/crossword-ex2-1.png" style="width: 180px; height: 180px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> It is impossible to place the word because there will always be a space/letter above or below it.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/04/crossword-ex3-1.png" style="width: 478px; height: 180px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The word "ca" can be placed as shown above (right to left). 
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == board.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == board[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m * n &lt;= 2 * 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">board[i][j]</code> will be <code style="user-select: auto;">' '</code>, <code style="user-select: auto;">'#'</code>, or a lowercase English letter.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word.length &lt;= max(m, n)</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">word</code> will contain only lowercase English letters.</li>
</ul>
</div>