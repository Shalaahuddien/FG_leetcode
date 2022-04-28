<h2><a href="https://leetcode.com/problems/maximum-repeating-substring/">1668. Maximum Repeating Substring</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">For a string <code style="user-select: auto;">sequence</code>, a string <code style="user-select: auto;">word</code> is <strong style="user-select: auto;"><code style="user-select: auto;">k</code>-repeating</strong> if <code style="user-select: auto;">word</code> concatenated <code style="user-select: auto;">k</code> times is a substring of <code style="user-select: auto;">sequence</code>. The <code style="user-select: auto;">word</code>'s <strong style="user-select: auto;">maximum <code style="user-select: auto;">k</code>-repeating value</strong> is the highest value <code style="user-select: auto;">k</code> where <code style="user-select: auto;">word</code> is <code style="user-select: auto;">k</code>-repeating in <code style="user-select: auto;">sequence</code>. If <code style="user-select: auto;">word</code> is not a substring of <code style="user-select: auto;">sequence</code>, <code style="user-select: auto;">word</code>'s maximum <code style="user-select: auto;">k</code>-repeating value is <code style="user-select: auto;">0</code>.</p>

<p style="user-select: auto;">Given strings <code style="user-select: auto;">sequence</code> and <code style="user-select: auto;">word</code>, return <em style="user-select: auto;">the <strong style="user-select: auto;">maximum <code style="user-select: auto;">k</code>-repeating value</strong> of <code style="user-select: auto;">word</code> in <code style="user-select: auto;">sequence</code></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> sequence = "ababc", word = "ab"
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation: </strong>"abab" is a substring in "<u style="user-select: auto;">abab</u>c".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> sequence = "ababc", word = "ba"
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation: </strong>"ba" is a substring in "a<u style="user-select: auto;">ba</u>bc". "baba" is not a substring in "ababc".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> sequence = "ababc", word = "ac"
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation: </strong>"ac" is not a substring in "ababc". 
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= sequence.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">sequence</code> and <code style="user-select: auto;">word</code>&nbsp;contains only lowercase English letters.</li>
</ul>
</div>