<h2><a href="https://leetcode.com/problems/sum-of-beauty-of-all-substrings/">1781. Sum of Beauty of All Substrings</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">The <strong style="user-select: auto;">beauty</strong> of a string is the difference in frequencies between the most frequent and least frequent characters.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the beauty of <code style="user-select: auto;">"abaacc"</code> is <code style="user-select: auto;">3 - 1 = 2</code>.</li>
</ul>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <em style="user-select: auto;">the sum of <strong style="user-select: auto;">beauty</strong> of all of its substrings.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aabcb"
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation: </strong>The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aabcbaa"
<strong style="user-select: auto;">Output:</strong> 17
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;=<sup style="user-select: auto;"> </sup>500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of only lowercase English letters.</li>
</ul>
</div>