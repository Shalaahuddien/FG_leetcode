<h2><a href="https://leetcode.com/problems/determine-if-string-halves-are-alike/">1704. Determine if String Halves Are Alike</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">s</code> of even length. Split this string into two halves of equal lengths, and let <code style="user-select: auto;">a</code> be the first half and <code style="user-select: auto;">b</code> be the second half.</p>

<p style="user-select: auto;">Two strings are <strong style="user-select: auto;">alike</strong> if they have the same number of vowels (<code style="user-select: auto;">'a'</code>, <code style="user-select: auto;">'e'</code>, <code style="user-select: auto;">'i'</code>, <code style="user-select: auto;">'o'</code>, <code style="user-select: auto;">'u'</code>, <code style="user-select: auto;">'A'</code>, <code style="user-select: auto;">'E'</code>, <code style="user-select: auto;">'I'</code>, <code style="user-select: auto;">'O'</code>, <code style="user-select: auto;">'U'</code>). Notice that <code style="user-select: auto;">s</code> contains uppercase and lowercase letters.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if </em><code style="user-select: auto;">a</code><em style="user-select: auto;"> and </em><code style="user-select: auto;">b</code><em style="user-select: auto;"> are <strong style="user-select: auto;">alike</strong></em>. Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "book"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> a = "b<u style="user-select: auto;">o</u>" and b = "<u style="user-select: auto;">o</u>k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "textbook"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> a = "t<u style="user-select: auto;">e</u>xt" and b = "b<u style="user-select: auto;">oo</u>k". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= s.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s.length</code> is even.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of <strong style="user-select: auto;">uppercase and lowercase</strong> letters.</li>
</ul>
</div>