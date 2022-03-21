<h2><a href="https://leetcode.com/problems/strings-differ-by-one-character/">1554. Strings Differ by One Character</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a list of strings <code style="user-select: auto;">dict</code> where all the strings are of the same length.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> if there are 2 strings that only differ by 1 character in the same index, otherwise return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> dict = ["abcd","acbd", "aacd"]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Strings "a<strong style="user-select: auto;">b</strong>cd" and "a<strong style="user-select: auto;">a</strong>cd" differ only by one character in the index 1.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> dict = ["ab","cd","yz"]
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> dict = ["abcd","cccc","abyd","abab"]
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of characters in <code style="user-select: auto;">dict &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">dict[i].length == dict[j].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">dict[i]</code> should be unique.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">dict[i]</code> contains only lowercase English letters.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Could you solve this problem in <code style="user-select: auto;">O(n * m)</code> where n is the length of <code style="user-select: auto;">dict</code> and <code style="user-select: auto;">m</code> is the length of each string.</p>
</div>