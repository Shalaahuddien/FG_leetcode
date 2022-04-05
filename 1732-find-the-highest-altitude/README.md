<h2><a href="https://leetcode.com/problems/find-the-highest-altitude/">1732. Find the Highest Altitude</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is a biker going on a road trip. The road trip consists of <code style="user-select: auto;">n + 1</code> points at different altitudes. The biker starts his trip on point <code style="user-select: auto;">0</code> with altitude equal <code style="user-select: auto;">0</code>.</p>

<p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">gain</code> of length <code style="user-select: auto;">n</code> where <code style="user-select: auto;">gain[i]</code> is the <strong style="user-select: auto;">net gain in altitude</strong> between points <code style="user-select: auto;">i</code>​​​​​​ and <code style="user-select: auto;">i + 1</code> for all (<code style="user-select: auto;">0 &lt;= i &lt; n)</code>. Return <em style="user-select: auto;">the <strong style="user-select: auto;">highest altitude</strong> of a point.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> gain = [-5,1,5,0,-7]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> gain = [-4,-3,-2,-1,4,3,2]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == gain.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= gain[i] &lt;= 100</code></li>
</ul>
</div>