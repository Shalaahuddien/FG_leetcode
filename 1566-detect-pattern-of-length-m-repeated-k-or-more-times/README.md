<h2><a href="https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/">1566. Detect Pattern of Length M Repeated K or More Times</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of positive integers <code style="user-select: auto;">arr</code>, find a pattern of length <code style="user-select: auto;">m</code> that is repeated <code style="user-select: auto;">k</code> or more times.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">pattern</strong> is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times <strong style="user-select: auto;">consecutively </strong>without overlapping. A pattern is defined by its length and the number of repetitions.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if there exists a pattern of length</em> <code style="user-select: auto;">m</code> <em style="user-select: auto;">that is repeated</em> <code style="user-select: auto;">k</code> <em style="user-select: auto;">or more times, otherwise return</em> <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,2,4,4,4,4], m = 1, k = 3
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation: </strong>The pattern <strong style="user-select: auto;">(4)</strong> of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation: </strong>The pattern <strong style="user-select: auto;">(1,2)</strong> of length 2 is repeated 2 consecutive times. Another valid pattern <strong style="user-select: auto;">(2,1) is</strong> also repeated 2 times.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,2,1,2,1,3], m = 2, k = 3
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation: </strong>The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= arr.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr[i] &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= k &lt;= 100</code></li>
</ul>
</div>