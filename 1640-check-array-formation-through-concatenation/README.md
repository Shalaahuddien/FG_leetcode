<h2><a href="https://leetcode.com/problems/check-array-formation-through-concatenation/">1640. Check Array Formation Through Concatenation</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an array of <strong style="user-select: auto;">distinct</strong> integers <code style="user-select: auto;">arr</code> and an array of integer arrays <code style="user-select: auto;">pieces</code>, where the integers in <code style="user-select: auto;">pieces</code> are <strong style="user-select: auto;">distinct</strong>. Your goal is to form <code style="user-select: auto;">arr</code> by concatenating the arrays in <code style="user-select: auto;">pieces</code> <strong style="user-select: auto;">in any order</strong>. However, you are <strong style="user-select: auto;">not</strong> allowed to reorder the integers in each array <code style="user-select: auto;">pieces[i]</code>.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if it is possible </em><em style="user-select: auto;">to form the array </em><code style="user-select: auto;">arr</code><em style="user-select: auto;"> from </em><code style="user-select: auto;">pieces</code>. Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [15,88], pieces = [[88],[15]]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Concatenate [15] then [88]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [49,18,16], pieces = [[16,18,49]]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> Even though the numbers match, we cannot reorder pieces[0].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Concatenate [91] then [4,64] then [78]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= pieces.length &lt;= arr.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">sum(pieces[i].length) == arr.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= pieces[i].length &lt;= arr.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr[i], pieces[i][j] &lt;= 100</code></li>
	<li style="user-select: auto;">The integers in <code style="user-select: auto;">arr</code> are <strong style="user-select: auto;">distinct</strong>.</li>
	<li style="user-select: auto;">The integers in <code style="user-select: auto;">pieces</code> are <strong style="user-select: auto;">distinct</strong> (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).</li>
</ul>
</div>