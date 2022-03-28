<h2><a href="https://leetcode.com/problems/bold-words-in-string/">758. Bold Words in String</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of keywords <code style="user-select: auto;">words</code> and a string <code style="user-select: auto;">s</code>, make all appearances of all keywords <code style="user-select: auto;">words[i]</code> in <code style="user-select: auto;">s</code> bold. Any letters between <code style="user-select: auto;">&lt;b&gt;</code> and <code style="user-select: auto;">&lt;/b&gt;</code> tags become bold.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">s</code> <em style="user-select: auto;">after adding the bold tags</em>. The returned string should use the least number of tags possible, and the tags should form a valid combination.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> words = ["ab","bc"], s = "aabcd"
<strong style="user-select: auto;">Output:</strong> "a&lt;b&gt;abc&lt;/b&gt;d"
<strong style="user-select: auto;">Explanation:</strong> Note that returning <code style="user-select: auto;">"a&lt;b&gt;a&lt;b&gt;b&lt;/b&gt;c&lt;/b&gt;d"</code> would use more tags, so it is incorrect.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> words = ["ab","cb"], s = "aabcd"
<strong style="user-select: auto;">Output:</strong> "a&lt;b&gt;ab&lt;/b&gt;cd"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= words.length &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">words[i]</code> consist of lowercase English letters.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Note:</strong> This question is the same as 616: <a href="https://leetcode.com/problems/add-bold-tag-in-string/" target="_blank" style="user-select: auto;">https://leetcode.com/problems/add-bold-tag-in-string/</a></p>
</div>