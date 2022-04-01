<h2><a href="https://leetcode.com/problems/brace-expansion/">1087. Brace Expansion</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">s</code> representing a list of words. Each letter in the word has one or more options.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If there is one option, the letter is represented as is.</li>
	<li style="user-select: auto;">If there is more than one option, then curly braces delimit the options. For example, <code style="user-select: auto;">"{a,b,c}"</code> represents options <code style="user-select: auto;">["a", "b", "c"]</code>.</li>
</ul>

<p style="user-select: auto;">For example, if <code style="user-select: auto;">s = "a{b,c}"</code>, the first character is always <code style="user-select: auto;">'a'</code>, but the second character can be <code style="user-select: auto;">'b'</code> or <code style="user-select: auto;">'c'</code>. The original list is <code style="user-select: auto;">["ab", "ac"]</code>.</p>

<p style="user-select: auto;">Return all words that can be formed in this manner, <strong style="user-select: auto;">sorted</strong> in lexicographical order.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "{a,b}c{d,e}f"
<strong style="user-select: auto;">Output:</strong> ["acdf","acef","bcdf","bcef"]
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abcd"
<strong style="user-select: auto;">Output:</strong> ["abcd"]
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of curly brackets <code style="user-select: auto;">'{}'</code>, commas&nbsp;<code style="user-select: auto;">','</code>, and lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> is guaranteed to be a valid input.</li>
	<li style="user-select: auto;">There are no nested curly brackets.</li>
	<li style="user-select: auto;">All characters inside a pair of consecutive opening and ending curly brackets are different.</li>
</ul>
</div>