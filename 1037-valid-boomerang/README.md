<h2><a href="https://leetcode.com/problems/valid-boomerang/">1037. Valid Boomerang</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array <code style="user-select: auto;">points</code> where <code style="user-select: auto;">points[i] = [x<sub style="user-select: auto;">i</sub>, y<sub style="user-select: auto;">i</sub>]</code> represents a point on the <strong style="user-select: auto;">X-Y</strong> plane, return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if these points are a <strong style="user-select: auto;">boomerang</strong></em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">boomerang</strong> is a set of three points that are <strong style="user-select: auto;">all distinct</strong> and <strong style="user-select: auto;">not in a straight line</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[1,1],[2,3],[3,2]]
<strong style="user-select: auto;">Output:</strong> true
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong style="user-select: auto;">Output:</strong> false
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">points.length == 3</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">points[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= x<sub style="user-select: auto;">i</sub>, y<sub style="user-select: auto;">i</sub> &lt;= 100</code></li>
</ul>
</div>