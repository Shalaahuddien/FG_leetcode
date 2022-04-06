<h2><a href="https://leetcode.com/problems/brightest-position-on-street/">2021. Brightest Position on Street</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A perfectly straight street is represented by a number line. The street has street lamp(s) on it and is represented by a 2D integer array <code style="user-select: auto;">lights</code>. Each <code style="user-select: auto;">lights[i] = [position<sub style="user-select: auto;">i</sub>, range<sub style="user-select: auto;">i</sub>]</code> indicates that there is a street lamp at position <code style="user-select: auto;">position<sub style="user-select: auto;">i</sub></code> that lights up the area from <code style="user-select: auto;">[position<sub style="user-select: auto;">i</sub> - range<sub style="user-select: auto;">i</sub>, position<sub style="user-select: auto;">i</sub> + range<sub style="user-select: auto;">i</sub>]</code> (<strong style="user-select: auto;">inclusive</strong>).</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">brightness</strong> of a position <code style="user-select: auto;">p</code> is defined as the number of street lamp that light up the position <code style="user-select: auto;">p</code>.</p>

<p style="user-select: auto;">Given <code style="user-select: auto;">lights</code>, return <em style="user-select: auto;">the <strong style="user-select: auto;">brightest</strong> position on the</em><em style="user-select: auto;"> street. If there are multiple brightest positions, return the <strong style="user-select: auto;">smallest</strong> one.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/09/28/image-20210928155140-1.png" style="width: 700px; height: 165px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> lights = [[-3,2],[1,2],[3,3]]
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong>
The first street lamp lights up the area from [(-3) - 2, (-3) + 2] = [-5, -1].
The second street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].
The third street lamp lights up the area from [3 - 3, 3 + 3] = [0, 6].

Position -1 has a brightness of 2, illuminated by the first and second street light.
Positions 0, 1, 2, and 3 have a brightness of 2, illuminated by the second and third street light.
Out of all these positions, -1 is the smallest, so return it.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> lights = [[1,0],[0,1]]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong>
The first street lamp lights up the area from [1 - 0, 1 + 0] = [1, 1].
The second street lamp lights up the area from [0 - 1, 0 + 1] = [-1, 1].

Position 1 has a brightness of 2, illuminated by the first and second street light.
Return 1 because it is the brightest position on the street.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> lights = [[1,2]]
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong>
The first street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].

Positions -1, 0, 1, 2, and 3 have a brightness of 1, illuminated by the first street light.
Out of all these positions, -1 is the smallest, so return it.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= lights.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">lights[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">8</sup> &lt;= position<sub style="user-select: auto;">i</sub> &lt;= 10<sup style="user-select: auto;">8</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= range<sub style="user-select: auto;">i</sub> &lt;= 10<sup style="user-select: auto;">8</sup></code></li>
</ul>
</div>