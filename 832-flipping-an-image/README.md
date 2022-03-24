<h2><a href="https://leetcode.com/problems/flipping-an-image/">832. Flipping an Image</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an <code style="user-select: auto;">n x n</code> binary matrix <code style="user-select: auto;">image</code>, flip the image <strong style="user-select: auto;">horizontally</strong>, then invert it, and return <em style="user-select: auto;">the resulting image</em>.</p>

<p style="user-select: auto;">To flip an image horizontally means that each row of the image is reversed.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, flipping <code style="user-select: auto;">[1,1,0]</code> horizontally results in <code style="user-select: auto;">[0,1,1]</code>.</li>
</ul>

<p style="user-select: auto;">To invert an image means that each <code style="user-select: auto;">0</code> is replaced by <code style="user-select: auto;">1</code>, and each <code style="user-select: auto;">1</code> is replaced by <code style="user-select: auto;">0</code>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, inverting <code style="user-select: auto;">[0,1,1]</code> results in <code style="user-select: auto;">[1,0,0]</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> image = [[1,1,0],[1,0,1],[0,0,0]]
<strong style="user-select: auto;">Output:</strong> [[1,0,0],[0,1,0],[1,1,1]]
<strong style="user-select: auto;">Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong style="user-select: auto;">Output:</strong> [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong style="user-select: auto;">Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == image.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == image[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 20</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">images[i][j]</code> is either <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
</ul>
</div>