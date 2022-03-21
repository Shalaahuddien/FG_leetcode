<h2><a href="https://leetcode.com/problems/reformat-the-string/">1417. Reformat The String</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an alphanumeric string <code style="user-select: auto;">s</code>. (<strong style="user-select: auto;">Alphanumeric string</strong> is a string consisting of lowercase English letters and digits).</p>

<p style="user-select: auto;">You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the reformatted string</em> or return <strong style="user-select: auto;">an empty string</strong> if it is impossible to reformat the string.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "a0b1c2"
<strong style="user-select: auto;">Output:</strong> "0a1b2c"
<strong style="user-select: auto;">Explanation:</strong> No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "leetcode"
<strong style="user-select: auto;">Output:</strong> ""
<strong style="user-select: auto;">Explanation:</strong> "leetcode" has only characters so we cannot separate them by digits.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "1229857369"
<strong style="user-select: auto;">Output:</strong> ""
<strong style="user-select: auto;">Explanation:</strong> "1229857369" has only digits so we cannot separate them by characters.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of only lowercase English letters and/or digits.</li>
</ul>
</div>