<h2><a href="https://leetcode.com/problems/hexspeak/">1271. Hexspeak</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A decimal number can be converted to its <strong style="user-select: auto;">Hexspeak representation</strong> by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit <code style="user-select: auto;">'0'</code> with the letter <code style="user-select: auto;">'O'</code>, and the digit <code style="user-select: auto;">'1'</code> with the letter <code style="user-select: auto;">'I'</code>. Such a representation is valid if and only if it consists only of the letters in the set <code style="user-select: auto;">{'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}</code>.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">num</code> representing a decimal integer <code style="user-select: auto;">n</code>, <em style="user-select: auto;">return the <strong style="user-select: auto;">Hexspeak representation</strong> of </em><code style="user-select: auto;">n</code><em style="user-select: auto;"> if it is valid, otherwise return </em><code style="user-select: auto;">"ERROR"</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> num = "257"
<strong style="user-select: auto;">Output:</strong> "IOI"
<strong style="user-select: auto;">Explanation:</strong> 257 is 101 in hexadecimal.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> num = "3"
<strong style="user-select: auto;">Output:</strong> "ERROR"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= num.length &lt;= 12</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">num</code> does not contain leading zeros.</li>
	<li style="user-select: auto;">num represents an integer in the range <code style="user-select: auto;">[1, 10<sup style="user-select: auto;">12</sup>]</code>.</li>
</ul>
</div>