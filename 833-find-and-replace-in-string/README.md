<h2><a href="https://leetcode.com/problems/find-and-replace-in-string/">833. Find And Replace in String</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a <strong style="user-select: auto;">0-indexed</strong> string <code style="user-select: auto;">s</code> that you must perform <code style="user-select: auto;">k</code> replacement operations on. The replacement operations are given as three <strong style="user-select: auto;">0-indexed</strong> parallel arrays, <code style="user-select: auto;">indices</code>, <code style="user-select: auto;">sources</code>, and <code style="user-select: auto;">targets</code>, all of length <code style="user-select: auto;">k</code>.</p>

<p style="user-select: auto;">To complete the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> replacement operation:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">Check if the <strong style="user-select: auto;">substring</strong> <code style="user-select: auto;">sources[i]</code> occurs at index <code style="user-select: auto;">indices[i]</code> in the <strong style="user-select: auto;">original string</strong> <code style="user-select: auto;">s</code>.</li>
	<li style="user-select: auto;">If it does not occur, <strong style="user-select: auto;">do nothing</strong>.</li>
	<li style="user-select: auto;">Otherwise if it does occur, <strong style="user-select: auto;">replace</strong> that substring with <code style="user-select: auto;">targets[i]</code>.</li>
</ol>

<p style="user-select: auto;">For example, if <code style="user-select: auto;">s = "<u style="user-select: auto;">ab</u>cd"</code>, <code style="user-select: auto;">indices[i] = 0</code>, <code style="user-select: auto;">sources[i] = "ab"</code>, and <code style="user-select: auto;">targets[i] = "eee"</code>, then the result of this replacement will be <code style="user-select: auto;">"<u style="user-select: auto;">eee</u>cd"</code>.</p>

<p style="user-select: auto;">All replacement operations must occur <strong style="user-select: auto;">simultaneously</strong>, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will <strong style="user-select: auto;">not overlap</strong>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, a testcase with <code style="user-select: auto;">s = "abc"</code>, <code style="user-select: auto;">indices = [0, 1]</code>, and <code style="user-select: auto;">sources = ["ab","bc"]</code> will not be generated because the <code style="user-select: auto;">"ab"</code> and <code style="user-select: auto;">"bc"</code> replacements overlap.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">resulting string</strong> after performing all replacement operations on </em><code style="user-select: auto;">s</code>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">substring</strong> is a contiguous sequence of characters in a string.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png" style="width: 411px; height: 251px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
<strong style="user-select: auto;">Output:</strong> "eeebffff"
<strong style="user-select: auto;">Explanation:</strong>
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png" style="width: 411px; height: 251px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
<strong style="user-select: auto;">Output:</strong> "eeecd"
<strong style="user-select: auto;">Explanation:</strong>
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">k == indices.length == sources.length == targets.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= indexes[i] &lt; s.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= sources[i].length, targets[i].length &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of only lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">sources[i]</code> and <code style="user-select: auto;">targets[i]</code> consist of only lowercase English letters.</li>
</ul>
</div>