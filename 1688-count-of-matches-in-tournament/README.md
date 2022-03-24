<h2><a href="https://leetcode.com/problems/count-of-matches-in-tournament/">1688. Count of Matches in Tournament</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer <code style="user-select: auto;">n</code>, the number of teams in a tournament that has strange rules:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If the current number of teams is <strong style="user-select: auto;">even</strong>, each team gets paired with another team. A total of <code style="user-select: auto;">n / 2</code> matches are played, and <code style="user-select: auto;">n / 2</code> teams advance to the next round.</li>
	<li style="user-select: auto;">If the current number of teams is <strong style="user-select: auto;">odd</strong>, one team randomly advances in the tournament, and the rest gets paired. A total of <code style="user-select: auto;">(n - 1) / 2</code> matches are played, and <code style="user-select: auto;">(n - 1) / 2 + 1</code> teams advance to the next round.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of matches played in the tournament until a winner is decided.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 7
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation:</strong> Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 14
<strong style="user-select: auto;">Output:</strong> 13
<strong style="user-select: auto;">Explanation:</strong> Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 200</code></li>
</ul>
</div>