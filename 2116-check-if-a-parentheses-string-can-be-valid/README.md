<h2><a href="https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/">2116. Check if a Parentheses String Can Be Valid</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A parentheses string is a <strong style="user-select: auto;">non-empty</strong> string consisting only of <code style="user-select: auto;">'('</code> and <code style="user-select: auto;">')'</code>. It is valid if <strong style="user-select: auto;">any</strong> of the following conditions is <strong style="user-select: auto;">true</strong>:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">It is <code style="user-select: auto;">()</code>.</li>
	<li style="user-select: auto;">It can be written as <code style="user-select: auto;">AB</code> (<code style="user-select: auto;">A</code> concatenated with <code style="user-select: auto;">B</code>), where <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code> are valid parentheses strings.</li>
	<li style="user-select: auto;">It can be written as <code style="user-select: auto;">(A)</code>, where <code style="user-select: auto;">A</code> is a valid parentheses string.</li>
</ul>

<p style="user-select: auto;">You are given a parentheses string <code style="user-select: auto;">s</code> and a string <code style="user-select: auto;">locked</code>, both of length <code style="user-select: auto;">n</code>. <code style="user-select: auto;">locked</code> is a binary string consisting only of <code style="user-select: auto;">'0'</code>s and <code style="user-select: auto;">'1'</code>s. For <strong style="user-select: auto;">each</strong> index <code style="user-select: auto;">i</code> of <code style="user-select: auto;">locked</code>,</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If <code style="user-select: auto;">locked[i]</code> is <code style="user-select: auto;">'1'</code>, you <strong style="user-select: auto;">cannot</strong> change <code style="user-select: auto;">s[i]</code>.</li>
	<li style="user-select: auto;">But if <code style="user-select: auto;">locked[i]</code> is <code style="user-select: auto;">'0'</code>, you <strong style="user-select: auto;">can</strong> change <code style="user-select: auto;">s[i]</code> to either <code style="user-select: auto;">'('</code> or <code style="user-select: auto;">')'</code>.</li>
</ul>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if you can make <code style="user-select: auto;">s</code> a valid parentheses string</em>. Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/eg1.png" style="width: 311px; height: 101px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "))()))", locked = "010100"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "()()", locked = "0000"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> We do not need to make any changes because s is already valid.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = ")", locked = "0"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == s.length == locked.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s[i]</code> is either <code style="user-select: auto;">'('</code> or <code style="user-select: auto;">')'</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">locked[i]</code> is either <code style="user-select: auto;">'0'</code> or <code style="user-select: auto;">'1'</code>.</li>
</ul>
</div>