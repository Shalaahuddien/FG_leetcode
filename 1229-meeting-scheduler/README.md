<h2><a href="https://leetcode.com/problems/meeting-scheduler/">1229. Meeting Scheduler</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the availability time slots arrays <code style="user-select: auto;">slots1</code> and <code style="user-select: auto;">slots2</code> of two people and a meeting duration <code style="user-select: auto;">duration</code>, return the <strong style="user-select: auto;">earliest time slot</strong> that works for both of them and is of duration <code style="user-select: auto;">duration</code>.</p>

<p style="user-select: auto;">If there is no common time slot that satisfies the requirements, return an <strong style="user-select: auto;">empty array</strong>.</p>

<p style="user-select: auto;">The format of a time slot is an array of two elements <code style="user-select: auto;">[start, end]</code> representing an inclusive time range from <code style="user-select: auto;">start</code> to <code style="user-select: auto;">end</code>.</p>

<p style="user-select: auto;">It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots <code style="user-select: auto;">[start1, end1]</code> and <code style="user-select: auto;">[start2, end2]</code> of the same person, either <code style="user-select: auto;">start1 &gt; end2</code> or <code style="user-select: auto;">start2 &gt; end1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
<strong style="user-select: auto;">Output:</strong> [60,68]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= slots1.length, slots2.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">slots1[i].length, slots2[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">slots1[i][0] &lt; slots1[i][1]</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">slots2[i][0] &lt; slots2[i][1]</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= slots1[i][j], slots2[i][j] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= duration &lt;= 10<sup style="user-select: auto;">6</sup></code></li>
</ul>
</div>