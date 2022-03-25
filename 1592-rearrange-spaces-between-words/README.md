<h2><a href="https://leetcode.com/problems/rearrange-spaces-between-words/">1592. Rearrange Spaces Between Words</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">text</code> of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that <code style="user-select: auto;">text</code> <strong style="user-select: auto;">contains at least one word</strong>.</p>

<p style="user-select: auto;">Rearrange the spaces so that there is an <strong style="user-select: auto;">equal</strong> number of spaces between every pair of adjacent words and that number is <strong style="user-select: auto;">maximized</strong>. If you cannot redistribute all the spaces equally, place the <strong style="user-select: auto;">extra spaces at the end</strong>, meaning the returned string should be the same length as <code style="user-select: auto;">text</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the string after rearranging the spaces</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> text = "  this   is  a sentence "
<strong style="user-select: auto;">Output:</strong> "this   is   a   sentence"
<strong style="user-select: auto;">Explanation:</strong> There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> text = " practice   makes   perfect"
<strong style="user-select: auto;">Output:</strong> "practice   makes   perfect "
<strong style="user-select: auto;">Explanation:</strong> There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= text.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">text</code> consists of lowercase English letters and <code style="user-select: auto;">' '</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">text</code> contains at least one word.</li>
</ul>
</div>