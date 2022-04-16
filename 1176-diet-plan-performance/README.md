<h2><a href="https://leetcode.com/problems/diet-plan-performance/">1176. Diet Plan Performance</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A dieter consumes&nbsp;<code style="user-select: auto;">calories[i]</code>&nbsp;calories on the <code style="user-select: auto;">i</code>-th day.&nbsp;</p>

<p style="user-select: auto;">Given an integer <code style="user-select: auto;">k</code>, for <strong style="user-select: auto;">every</strong> consecutive sequence of <code style="user-select: auto;">k</code> days (<code style="user-select: auto;">calories[i], calories[i+1], ..., calories[i+k-1]</code>&nbsp;for all <code style="user-select: auto;">0 &lt;= i &lt;= n-k</code>), they look at <em style="user-select: auto;">T</em>, the total calories consumed during that sequence of <code style="user-select: auto;">k</code> days (<code style="user-select: auto;">calories[i] + calories[i+1] + ... + calories[i+k-1]</code>):</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If <code style="user-select: auto;">T &lt; lower</code>, they performed poorly on their diet and lose 1 point;&nbsp;</li>
	<li style="user-select: auto;">If <code style="user-select: auto;">T &gt; upper</code>, they performed well on their diet and gain 1 point;</li>
	<li style="user-select: auto;">Otherwise, they performed normally and there is no change in points.</li>
</ul>

<p style="user-select: auto;">Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for <code style="user-select: auto;">calories.length</code>&nbsp;days.</p>

<p style="user-select: auto;">Note that the total points can be negative.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation</strong>: Since k = 1, we consider each element of the array separately and compare it to lower and upper.
calories[0] and calories[1] are less than lower so 2 points are lost.
calories[3] and calories[4] are greater than upper so 2 points are gained.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> calories = [3,2], k = 2, lower = 0, upper = 1
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation</strong>: Since k = 2, we consider subarrays of length 2.
calories[0] + calories[1] &gt; upper so 1 point is gained.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> calories = [6,5,0,0], k = 2, lower = 1, upper = 5
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation</strong>:
calories[0] + calories[1] &gt; upper so 1 point is gained.
lower &lt;= calories[1] + calories[2] &lt;= upper so no change in points.
calories[2] + calories[3] &lt; lower so 1 point is lost.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= calories.length &lt;= 10^5</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= calories[i] &lt;= 20000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= lower &lt;= upper</code></li>
</ul>
</div>