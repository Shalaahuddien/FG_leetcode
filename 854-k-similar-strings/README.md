<h2><a href="https://leetcode.com/problems/k-similar-strings/">854. K-Similar Strings</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Strings <code style="user-select: auto;">s1</code> and <code style="user-select: auto;">s2</code> are <code style="user-select: auto;">k</code><strong style="user-select: auto;">-similar</strong> (for some non-negative integer <code style="user-select: auto;">k</code>) if we can swap the positions of two letters in <code style="user-select: auto;">s1</code> exactly <code style="user-select: auto;">k</code> times so that the resulting string equals <code style="user-select: auto;">s2</code>.</p>

<p style="user-select: auto;">Given two anagrams <code style="user-select: auto;">s1</code> and <code style="user-select: auto;">s2</code>, return the smallest <code style="user-select: auto;">k</code> for which <code style="user-select: auto;">s1</code> and <code style="user-select: auto;">s2</code> are <code style="user-select: auto;">k</code><strong style="user-select: auto;">-similar</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s1 = "ab", s2 = "ba"
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s1 = "abc", s2 = "bca"
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s1.length &lt;= 20</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s2.length == s1.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s1</code> and <code style="user-select: auto;">s2</code> contain only lowercase letters from the set <code style="user-select: auto;">{'a', 'b', 'c', 'd', 'e', 'f'}</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s2</code> is an anagram of <code style="user-select: auto;">s1</code>.</li>
</ul>
</div>