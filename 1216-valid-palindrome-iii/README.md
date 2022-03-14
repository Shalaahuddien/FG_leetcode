<h2><a href="https://leetcode.com/problems/valid-palindrome-iii/">1216. Valid Palindrome III</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code> and an integer <code style="user-select: auto;">k</code>, return <code style="user-select: auto;">true</code> if <code style="user-select: auto;">s</code> is a <code style="user-select: auto;">k</code><strong style="user-select: auto;">-palindrome</strong>.</p>

<p style="user-select: auto;">A string is <code style="user-select: auto;">k</code><strong style="user-select: auto;">-palindrome</strong> if it can be transformed into a palindrome by removing at most <code style="user-select: auto;">k</code> characters from it.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abcdeca", k = 2
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Remove 'b' and 'e' characters.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abbababa", k = 1
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of only lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= s.length</code></li>
</ul>
</div>