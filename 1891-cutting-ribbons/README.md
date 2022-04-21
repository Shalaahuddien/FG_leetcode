<h2><a href="https://leetcode.com/problems/cutting-ribbons/">1891. Cutting Ribbons</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">ribbons</code>, where <code style="user-select: auto;">ribbons[i]</code> represents the length of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> ribbon, and an integer <code style="user-select: auto;">k</code>. You may cut any of the ribbons into any number of segments of <strong style="user-select: auto;">positive integer</strong> lengths, or perform no cuts at all.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, if you have a ribbon of length <code style="user-select: auto;">4</code>, you can:

	<ul style="user-select: auto;">
		<li style="user-select: auto;">Keep the ribbon of length <code style="user-select: auto;">4</code>,</li>
		<li style="user-select: auto;">Cut it into one ribbon of length <code style="user-select: auto;">3</code> and one ribbon of length <code style="user-select: auto;">1</code>,</li>
		<li style="user-select: auto;">Cut it into two ribbons of length <code style="user-select: auto;">2</code>,</li>
		<li style="user-select: auto;">Cut it into one ribbon of length <code style="user-select: auto;">2</code> and two ribbons of length <code style="user-select: auto;">1</code>, or</li>
		<li style="user-select: auto;">Cut it into four ribbons of length <code style="user-select: auto;">1</code>.</li>
	</ul>
	</li>
</ul>

<p style="user-select: auto;">Your goal is to obtain <code style="user-select: auto;">k</code> ribbons of all the <strong style="user-select: auto;">same positive integer length</strong>. You are allowed to throw away any excess ribbon as a result of cutting.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">maximum</strong> possible positive integer length that you can obtain </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> ribbons of</em><em style="user-select: auto;">, or </em><code style="user-select: auto;">0</code><em style="user-select: auto;"> if you cannot obtain </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> ribbons of the same length</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> ribbons = [9,7,5], k = 3
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong>
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> ribbons = [7,5,9], k = 4
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong>
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> ribbons = [5,7,9], k = 22
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> You cannot obtain k ribbons of the same positive integer length.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= ribbons.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= ribbons[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>