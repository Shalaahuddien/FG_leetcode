<h2><a href="https://leetcode.com/problems/longest-nice-substring/">1763. Longest Nice Substring</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A string <code style="user-select: auto;">s</code> is <strong style="user-select: auto;">nice</strong> if, for every letter of the alphabet that <code style="user-select: auto;">s</code> contains, it appears <strong style="user-select: auto;">both</strong> in uppercase and lowercase. For example, <code style="user-select: auto;">"abABB"</code> is nice because <code style="user-select: auto;">'A'</code> and <code style="user-select: auto;">'a'</code> appear, and <code style="user-select: auto;">'B'</code> and <code style="user-select: auto;">'b'</code> appear. However, <code style="user-select: auto;">"abA"</code> is not because <code style="user-select: auto;">'b'</code> appears, but <code style="user-select: auto;">'B'</code> does not.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <em style="user-select: auto;">the longest <strong style="user-select: auto;">substring</strong> of <code style="user-select: auto;">s</code> that is <strong style="user-select: auto;">nice</strong>. If there are multiple, return the substring of the <strong style="user-select: auto;">earliest</strong> occurrence. If there are none, return an empty string</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "YazaAay"
<strong style="user-select: auto;">Output:</strong> "aAa"
<strong style="user-select: auto;">Explanation: </strong>"aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "Bb"
<strong style="user-select: auto;">Output:</strong> "Bb"
<strong style="user-select: auto;">Explanation:</strong> "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "c"
<strong style="user-select: auto;">Output:</strong> ""
<strong style="user-select: auto;">Explanation:</strong> There are no nice substrings.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of uppercase and lowercase English letters.</li>
</ul>
</div>