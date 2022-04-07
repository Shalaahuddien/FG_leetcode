<h2><a href="https://leetcode.com/problems/shortest-distance-to-a-character/">821. Shortest Distance to a Character</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code> and a character <code style="user-select: auto;">c</code> that occurs in <code style="user-select: auto;">s</code>, return <em style="user-select: auto;">an array of integers </em><code style="user-select: auto;">answer</code><em style="user-select: auto;"> where </em><code style="user-select: auto;">answer.length == s.length</code><em style="user-select: auto;"> and </em><code style="user-select: auto;">answer[i]</code><em style="user-select: auto;"> is the <strong style="user-select: auto;">distance</strong> from index </em><code style="user-select: auto;">i</code><em style="user-select: auto;"> to the <strong style="user-select: auto;">closest</strong> occurrence of character </em><code style="user-select: auto;">c</code><em style="user-select: auto;"> in </em><code style="user-select: auto;">s</code>.</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">distance</strong> between two indices <code style="user-select: auto;">i</code> and <code style="user-select: auto;">j</code> is <code style="user-select: auto;">abs(i - j)</code>, where <code style="user-select: auto;">abs</code> is the absolute value function.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "loveleetcode", c = "e"
<strong style="user-select: auto;">Output:</strong> [3,2,1,0,1,0,0,1,2,2,1,0]
<strong style="user-select: auto;">Explanation:</strong> The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aaab", c = "b"
<strong style="user-select: auto;">Output:</strong> [3,2,1,0]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s[i]</code> and <code style="user-select: auto;">c</code> are lowercase English letters.</li>
	<li style="user-select: auto;">It is guaranteed that <code style="user-select: auto;">c</code> occurs at least once in <code style="user-select: auto;">s</code>.</li>
</ul>
</div>