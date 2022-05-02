<h2><a href="https://leetcode.com/problems/reverse-only-letters/">917. Reverse Only Letters</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, reverse the string according to the following rules:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">All the characters that are not English letters remain in the same position.</li>
	<li style="user-select: auto;">All the English letters (lowercase or uppercase) should be reversed.</li>
</ul>

<p style="user-select: auto;">Return <code style="user-select: auto;">s</code><em style="user-select: auto;"> after reversing it</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "ab-cd"
<strong style="user-select: auto;">Output:</strong> "dc-ba"
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "a-bC-dEf-ghIj"
<strong style="user-select: auto;">Output:</strong> "j-Ih-gfE-dCba"
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "Test1ng-Leet=code-Q!"
<strong style="user-select: auto;">Output:</strong> "Qedo1ct-eeLg=ntse-T!"
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of characters with ASCII values in the range <code style="user-select: auto;">[33, 122]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> does not contain <code style="user-select: auto;">'\"'</code> or <code style="user-select: auto;">'\\'</code>.</li>
</ul>
</div>