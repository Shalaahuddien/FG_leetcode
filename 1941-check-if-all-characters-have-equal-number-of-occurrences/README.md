<h2><a href="https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/">1941. Check if All Characters Have Equal Number of Occurrences</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if </em><code style="user-select: auto;">s</code><em style="user-select: auto;"> is a <strong style="user-select: auto;">good</strong> string, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise</em>.</p>

<p style="user-select: auto;">A string <code style="user-select: auto;">s</code> is <strong style="user-select: auto;">good</strong> if <strong style="user-select: auto;">all</strong> the characters that appear in <code style="user-select: auto;">s</code> have the <strong style="user-select: auto;">same</strong> number of occurrences (i.e., the same frequency).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abacbc"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aaabb"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of lowercase English letters.</li>
</ul>
</div>