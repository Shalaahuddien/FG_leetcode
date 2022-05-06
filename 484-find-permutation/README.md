<h2><a href="https://leetcode.com/problems/find-permutation/">484. Find Permutation</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A permutation <code style="user-select: auto;">perm</code> of <code style="user-select: auto;">n</code>&nbsp;integers of all the integers in the range <code style="user-select: auto;">[1, n]</code> can be represented as a string <code style="user-select: auto;">s</code> of length <code style="user-select: auto;">n - 1</code> where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">s[i] == 'I'</code> if <code style="user-select: auto;">perm[i] &lt; perm[i + 1]</code>, and</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s[i] == 'D'</code> if <code style="user-select: auto;">perm[i] &gt; perm[i + 1]</code>.</li>
</ul>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, reconstruct the lexicographically smallest permutation <code style="user-select: auto;">perm</code> and return it.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "I"
<strong style="user-select: auto;">Output:</strong> [1,2]
<strong style="user-select: auto;">Explanation:</strong> [1,2] is the only legal permutation that can represented by s, where the number 1 and 2 construct an increasing relationship.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "DI"
<strong style="user-select: auto;">Output:</strong> [2,1,3]
<strong style="user-select: auto;">Explanation:</strong> Both [2,1,3] and [3,1,2] can be represented as "DI", but since we want to find the smallest lexicographical permutation, you should return [2,1,3]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s[i]</code> is either <code style="user-select: auto;">'I'</code> or <code style="user-select: auto;">'D'</code>.</li>
</ul>
</div>