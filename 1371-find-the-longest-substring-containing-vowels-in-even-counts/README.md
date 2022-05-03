<h2><a href="https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/">1371. Find the Longest Substring Containing Vowels in Even Counts</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the string <code style="user-select: auto;">s</code>, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "eleetminicoworoep"
<strong style="user-select: auto;">Output:</strong> 13
<strong style="user-select: auto;">Explanation: </strong>The longest substring is "leetminicowor" which contains two each of the vowels: <strong style="user-select: auto;">e</strong>, <strong style="user-select: auto;">i</strong> and <strong style="user-select: auto;">o</strong> and zero of the vowels: <strong style="user-select: auto;">a</strong> and <strong style="user-select: auto;">u</strong>.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "leetcodeisgreat"
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong> The longest substring is "leetc" which contains two e's.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "bcbcbc"
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation:</strong> In this case, the given string "bcbcbc" is the longest because all vowels: <strong style="user-select: auto;">a</strong>, <strong style="user-select: auto;">e</strong>, <strong style="user-select: auto;">i</strong>, <strong style="user-select: auto;">o</strong> and <strong style="user-select: auto;">u</strong> appear zero times.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 5 x 10^5</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code>&nbsp;contains only lowercase English letters.</li>
</ul>
</div>