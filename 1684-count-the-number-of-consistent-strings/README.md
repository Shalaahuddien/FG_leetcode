<h2><a href="https://leetcode.com/problems/count-the-number-of-consistent-strings/">1684. Count the Number of Consistent Strings</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">allowed</code> consisting of <strong style="user-select: auto;">distinct</strong> characters and an array of strings <code style="user-select: auto;">words</code>. A string is <strong style="user-select: auto;">consistent </strong>if all characters in the string appear in the string <code style="user-select: auto;">allowed</code>.</p>

<p style="user-select: auto;">Return<em style="user-select: auto;"> the number of <strong style="user-select: auto;">consistent</strong> strings in the array </em><code style="user-select: auto;">words</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation:</strong> All strings are consistent.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> Strings "cc", "acd", "ac", and "d" are consistent.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= allowed.length &lt;=<sup style="user-select: auto;"> </sup>26</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words[i].length &lt;= 10</code></li>
	<li style="user-select: auto;">The characters in <code style="user-select: auto;">allowed</code> are <strong style="user-select: auto;">distinct</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">words[i]</code> and <code style="user-select: auto;">allowed</code> contain only lowercase English letters.</li>
</ul>
</div>