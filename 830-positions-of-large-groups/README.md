<h2><a href="https://leetcode.com/problems/positions-of-large-groups/">830. Positions of Large Groups</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">In a string <code style="user-select: auto;"><font face="monospace" style="user-select: auto;">s</font></code>&nbsp;of lowercase letters, these letters form consecutive groups of the same character.</p>

<p style="user-select: auto;">For example, a string like <code style="user-select: auto;">s = "abbxxxxzyy"</code> has the groups <code style="user-select: auto;">"a"</code>, <code style="user-select: auto;">"bb"</code>, <code style="user-select: auto;">"xxxx"</code>, <code style="user-select: auto;">"z"</code>, and&nbsp;<code style="user-select: auto;">"yy"</code>.</p>

<p style="user-select: auto;">A group is identified by an interval&nbsp;<code style="user-select: auto;">[start, end]</code>, where&nbsp;<code style="user-select: auto;">start</code>&nbsp;and&nbsp;<code style="user-select: auto;">end</code>&nbsp;denote the start and end&nbsp;indices (inclusive) of the group. In the above example,&nbsp;<code style="user-select: auto;">"xxxx"</code>&nbsp;has the interval&nbsp;<code style="user-select: auto;">[3,6]</code>.</p>

<p style="user-select: auto;">A group is considered&nbsp;<strong style="user-select: auto;">large</strong>&nbsp;if it has 3 or more characters.</p>

<p style="user-select: auto;">Return&nbsp;<em style="user-select: auto;">the intervals of every <strong style="user-select: auto;">large</strong> group sorted in&nbsp;<strong style="user-select: auto;">increasing order by start index</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abbxxxxzzy"
<strong style="user-select: auto;">Output:</strong> [[3,6]]
<strong style="user-select: auto;">Explanation:</strong> <code style="user-select: auto;">"xxxx" is the only </code>large group with start index 3 and end index 6.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abc"
<strong style="user-select: auto;">Output:</strong> []
<strong style="user-select: auto;">Explanation:</strong> We have groups "a", "b", and "c", none of which are large groups.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abcdddeeeeaabbbcd"
<strong style="user-select: auto;">Output:</strong> [[3,5],[6,9],[12,14]]
<strong style="user-select: auto;">Explanation:</strong> The large groups are "ddd", "eeee", and "bbb".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> contains lowercase English letters only.</li>
</ul>
</div>