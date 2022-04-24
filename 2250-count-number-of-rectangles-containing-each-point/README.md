<h2><a href="https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/">2250. Count Number of Rectangles Containing Each Point</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a 2D integer array <code style="user-select: auto;">rectangles</code> where <code style="user-select: auto;">rectangles[i] = [l<sub style="user-select: auto;">i</sub>, h<sub style="user-select: auto;">i</sub>]</code> indicates that <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> rectangle has a length of <code style="user-select: auto;">l<sub style="user-select: auto;">i</sub></code> and a height of <code style="user-select: auto;">h<sub style="user-select: auto;">i</sub></code>. You are also given a 2D integer array <code style="user-select: auto;">points</code> where <code style="user-select: auto;">points[j] = [x<sub style="user-select: auto;">j</sub>, y<sub style="user-select: auto;">j</sub>]</code> is a point with coordinates <code style="user-select: auto;">(x<sub style="user-select: auto;">j</sub>, y<sub style="user-select: auto;">j</sub>)</code>.</p>

<p style="user-select: auto;">The <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> rectangle has its <strong style="user-select: auto;">bottom-left corner</strong> point at the coordinates <code style="user-select: auto;">(0, 0)</code> and its <strong style="user-select: auto;">top-right corner</strong> point at <code style="user-select: auto;">(l<sub style="user-select: auto;">i</sub>, h<sub style="user-select: auto;">i</sub>)</code>.</p>

<p style="user-select: auto;">Return<em style="user-select: auto;"> an integer array </em><code style="user-select: auto;">count</code><em style="user-select: auto;"> of length </em><code style="user-select: auto;">points.length</code><em style="user-select: auto;"> where </em><code style="user-select: auto;">count[j]</code><em style="user-select: auto;"> is the number of rectangles that <strong style="user-select: auto;">contain</strong> the </em><code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code><em style="user-select: auto;"> point.</em></p>

<p style="user-select: auto;">The <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> rectangle <strong style="user-select: auto;">contains</strong> the <code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code> point if <code style="user-select: auto;">0 &lt;= x<sub style="user-select: auto;">j</sub> &lt;= l<sub style="user-select: auto;">i</sub></code> and <code style="user-select: auto;">0 &lt;= y<sub style="user-select: auto;">j</sub> &lt;= h<sub style="user-select: auto;">i</sub></code>. Note that points that lie on the <strong style="user-select: auto;">edges</strong> of a rectangle are also considered to be contained by that rectangle.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/example1.png" style="width: 300px; height: 509px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
<strong style="user-select: auto;">Output:</strong> [2,1]
<strong style="user-select: auto;">Explanation:</strong> 
The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/example2.png" style="width: 300px; height: 312px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
<strong style="user-select: auto;">Output:</strong> [1,3]
<strong style="user-select: auto;">Explanation:
</strong>The first rectangle contains only the point (1, 1).
The second rectangle contains only the point (1, 1).
The third rectangle contains the points (1, 3) and (1, 1).
The number of rectangles that contain the point (1, 3) is 1.
The number of rectangles that contain the point (1, 1) is 3.
Therefore, we return [1, 3].
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= rectangles.length, points.length &lt;= 5 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">rectangles[i].length == points[j].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= l<sub style="user-select: auto;">i</sub>, x<sub style="user-select: auto;">j</sub> &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= h<sub style="user-select: auto;">i</sub>, y<sub style="user-select: auto;">j</sub> &lt;= 100</code></li>
	<li style="user-select: auto;">All the <code style="user-select: auto;">rectangles</code> are <strong style="user-select: auto;">unique</strong>.</li>
	<li style="user-select: auto;">All the <code style="user-select: auto;">points</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>