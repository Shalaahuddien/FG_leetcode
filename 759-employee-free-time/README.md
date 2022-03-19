<h2><a href="https://leetcode.com/problems/employee-free-time/">759. Employee Free Time</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">We are given a list <code style="user-select: auto;">schedule</code> of employees, which represents the working time for each employee.</p>

<p style="user-select: auto;">Each employee has a list of non-overlapping <code style="user-select: auto;">Intervals</code>, and these intervals are in sorted order.</p>

<p style="user-select: auto;">Return the list of finite intervals representing <b style="user-select: auto;">common, positive-length free time</b> for <i style="user-select: auto;">all</i> employees, also in sorted order.</p>

<p style="user-select: auto;">(Even though we are representing <code style="user-select: auto;">Intervals</code> in the form <code style="user-select: auto;">[x, y]</code>, the objects inside are <code style="user-select: auto;">Intervals</code>, not lists or arrays. For example, <code style="user-select: auto;">schedule[0][0].start = 1</code>, <code style="user-select: auto;">schedule[0][0].end = 2</code>, and <code style="user-select: auto;">schedule[0][0][0]</code> is not defined).&nbsp; Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
<strong style="user-select: auto;">Output:</strong> [[3,4]]
<strong style="user-select: auto;">Explanation:</strong> There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
<strong style="user-select: auto;">Output:</strong> [[5,6],[7,9]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= schedule.length , schedule[i].length &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= schedule[i].start &lt; schedule[i].end &lt;= 10^8</code></li>
</ul>
</div>