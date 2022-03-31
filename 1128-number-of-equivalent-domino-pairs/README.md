<h2><a href="https://leetcode.com/problems/number-of-equivalent-domino-pairs/">1128. Number of Equivalent Domino Pairs</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a list of <code style="user-select: auto;">dominoes</code>, <code style="user-select: auto;">dominoes[i] = [a, b]</code> is <strong style="user-select: auto;">equivalent to</strong> <code style="user-select: auto;">dominoes[j] = [c, d]</code> if and only if either (<code style="user-select: auto;">a == c</code> and <code style="user-select: auto;">b == d</code>), or (<code style="user-select: auto;">a == d</code> and <code style="user-select: auto;">b == c</code>) - that is, one domino can be rotated to be equal to another domino.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of pairs </em><code style="user-select: auto;">(i, j)</code><em style="user-select: auto;"> for which </em><code style="user-select: auto;">0 &lt;= i &lt; j &lt; dominoes.length</code><em style="user-select: auto;">, and </em><code style="user-select: auto;">dominoes[i]</code><em style="user-select: auto;"> is <strong style="user-select: auto;">equivalent to</strong> </em><code style="user-select: auto;">dominoes[j]</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> dominoes = [[1,2],[2,1],[3,4],[5,6]]
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= dominoes.length &lt;= 4 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">dominoes[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= dominoes[i][j] &lt;= 9</code></li>
</ul>
</div>