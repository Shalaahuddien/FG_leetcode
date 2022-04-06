<h2><a href="https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/">2086. Minimum Number of Buckets Required to Collect Rainwater from Houses</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a <b style="user-select: auto;">0-index</b><strong style="user-select: auto;">ed</strong> string <code style="user-select: auto;">street</code>. Each character in <code style="user-select: auto;">street</code> is either <code style="user-select: auto;">'H'</code> representing a house or <code style="user-select: auto;">'.'</code> representing an empty space.</p>

<p style="user-select: auto;">You can place buckets on the <strong style="user-select: auto;">empty spaces</strong> to collect rainwater that falls from the adjacent houses. The rainwater from a house at index <code style="user-select: auto;">i</code> is collected if a bucket is placed at index <code style="user-select: auto;">i - 1</code> <strong style="user-select: auto;">and/or</strong> index <code style="user-select: auto;">i + 1</code>. A single bucket, if placed adjacent to two houses, can collect the rainwater from <strong style="user-select: auto;">both</strong> houses.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum </strong>number of buckets needed so that for <strong style="user-select: auto;">every</strong> house, there is <strong style="user-select: auto;">at least</strong> one bucket collecting rainwater from it, or </em><code style="user-select: auto;">-1</code><em style="user-select: auto;"> if it is impossible.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> street = "H..H"
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong>
We can put buckets at index 1 and index 2.
"H..H" -&gt; "HBBH" ('B' denotes where a bucket is placed).
The house at index 0 has a bucket to its right, and the house at index 3 has a bucket to its left.
Thus, for every house, there is at least one bucket collecting rainwater from it.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> street = ".H.H."
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong>
We can put a bucket at index 2.
".H.H." -&gt; ".HBH." ('B' denotes where a bucket is placed).
The house at index 1 has a bucket to its right, and the house at index 3 has a bucket to its left.
Thus, for every house, there is at least one bucket collecting rainwater from it.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> street = ".HHH."
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong>
There is no empty space to place a bucket to collect the rainwater from the house at index 2.
Thus, it is impossible to collect the rainwater from all the houses.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= street.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">street[i]</code> is either<code style="user-select: auto;">'H'</code> or <code style="user-select: auto;">'.'</code>.</li>
</ul>
</div>