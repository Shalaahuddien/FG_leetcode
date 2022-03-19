<h2><a href="https://leetcode.com/problems/largest-substring-between-two-equal-characters/">1624. Largest Substring Between Two Equal Characters</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <em style="user-select: auto;">the length of the longest substring between two equal characters, excluding the two characters.</em> If there is no such substring return <code style="user-select: auto;">-1</code>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">substring</strong> is a contiguous sequence of characters within a string.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aa"
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The optimal substring here is an empty substring between the two <code style="user-select: auto;">'a's</code>.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abca"
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> The optimal substring here is "bc".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "cbzxy"
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> There are no characters that appear twice in s.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 300</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> contains only lowercase English letters.</li>
</ul>
</div>