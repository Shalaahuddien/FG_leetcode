<h2><a href="https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/">1698. Number of Distinct Substrings in a String</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <em style="user-select: auto;">the number of <strong style="user-select: auto;">distinct</strong> substrings of</em>&nbsp;<code style="user-select: auto;">s</code>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">substring</strong> of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aabbaba"
<strong style="user-select: auto;">Output:</strong> 21
<strong style="user-select: auto;">Explanation:</strong> The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abcdefg"
<strong style="user-select: auto;">Output:</strong> 28
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of lowercase English letters.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Can you solve this problem in <code style="user-select: auto;">O(n)</code> time complexity?</div>