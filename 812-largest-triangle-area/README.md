<h2><a href="https://leetcode.com/problems/largest-triangle-area/">812. Largest Triangle Area</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of points on the <strong style="user-select: auto;">X-Y</strong> plane <code style="user-select: auto;">points</code> where <code style="user-select: auto;">points[i] = [x<sub style="user-select: auto;">i</sub>, y<sub style="user-select: auto;">i</sub>]</code>, return <em style="user-select: auto;">the area of the largest triangle that can be formed by any three different points</em>. Answers within <code style="user-select: auto;">10<sup style="user-select: auto;">-5</sup></code> of the actual answer will be accepted.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height: 369px; width: 450px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong style="user-select: auto;">Output:</strong> 2.00000
<strong style="user-select: auto;">Explanation:</strong> The five points are shown in the above figure. The red triangle is the largest.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[1,0],[0,0],[0,1]]
<strong style="user-select: auto;">Output:</strong> 0.50000
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">3 &lt;= points.length &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-50 &lt;= x<sub style="user-select: auto;">i</sub>, y<sub style="user-select: auto;">i</sub> &lt;= 50</code></li>
	<li style="user-select: auto;">All the given points are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>