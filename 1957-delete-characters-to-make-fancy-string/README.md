<h2><a href="https://leetcode.com/problems/delete-characters-to-make-fancy-string/">1957. Delete Characters to Make Fancy String</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;">fancy string</strong> is a string where no <strong style="user-select: auto;">three</strong> <strong style="user-select: auto;">consecutive</strong> characters are equal.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, delete the <strong style="user-select: auto;">minimum</strong> possible number of characters from <code style="user-select: auto;">s</code> to make it <strong style="user-select: auto;">fancy</strong>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the final string after the deletion</em>. It can be shown that the answer will always be <strong style="user-select: auto;">unique</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "le<u style="user-select: auto;">e</u>etcode"
<strong style="user-select: auto;">Output:</strong> "leetcode"
<strong style="user-select: auto;">Explanation:</strong>
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "<u style="user-select: auto;">a</u>aab<u style="user-select: auto;">aa</u>aa"
<strong style="user-select: auto;">Output:</strong> "aabaa"
<strong style="user-select: auto;">Explanation:</strong>
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aab"
<strong style="user-select: auto;">Output:</strong> "aab"
<strong style="user-select: auto;">Explanation:</strong> No three consecutive characters are equal, so return "aab".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists only of lowercase English letters.</li>
</ul>
</div>