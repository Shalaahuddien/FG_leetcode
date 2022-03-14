<h2><a href="https://leetcode.com/problems/the-kth-factor-of-n/">1492. The kth Factor of n</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given two positive integers <code style="user-select: auto;">n</code> and <code style="user-select: auto;">k</code>. A factor of an integer <code style="user-select: auto;">n</code> is defined as an integer <code style="user-select: auto;">i</code> where <code style="user-select: auto;">n % i == 0</code>.</p>

<p style="user-select: auto;">Consider a list of all factors of <code style="user-select: auto;">n</code> sorted in <strong style="user-select: auto;">ascending order</strong>, return <em style="user-select: auto;">the </em><code style="user-select: auto;">k<sup style="user-select: auto;">th</sup></code><em style="user-select: auto;"> factor</em> in this list or return <code style="user-select: auto;">-1</code> if <code style="user-select: auto;">n</code> has less than <code style="user-select: auto;">k</code> factors.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 12, k = 3
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> Factors list is [1, 2, 3, 4, 6, 12], the 3<sup style="user-select: auto;">rd</sup> factor is 3.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 7, k = 2
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation:</strong> Factors list is [1, 7], the 2<sup style="user-select: auto;">nd</sup> factor is 7.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 4, k = 4
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= n &lt;= 1000</code></li>
</ul>
</div>