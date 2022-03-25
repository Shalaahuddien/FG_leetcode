<h2><a href="https://leetcode.com/problems/delete-columns-to-make-sorted/">944. Delete Columns to Make Sorted</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an array of <code style="user-select: auto;">n</code> strings <code style="user-select: auto;">strs</code>, all of the same length.</p>

<p style="user-select: auto;">The strings can be arranged such that there is one on each line, making a grid. For example, <code style="user-select: auto;">strs = ["abc", "bce", "cae"]</code> can be arranged as:</p>

<pre style="user-select: auto;">abc
bce
cae
</pre>

<p style="user-select: auto;">You want to <strong style="user-select: auto;">delete</strong> the columns that are <strong style="user-select: auto;">not sorted lexicographically</strong>. In the above example (0-indexed), columns 0 (<code style="user-select: auto;">'a'</code>, <code style="user-select: auto;">'b'</code>, <code style="user-select: auto;">'c'</code>) and 2 (<code style="user-select: auto;">'c'</code>, <code style="user-select: auto;">'e'</code>, <code style="user-select: auto;">'e'</code>) are sorted while column 1 (<code style="user-select: auto;">'b'</code>, <code style="user-select: auto;">'c'</code>, <code style="user-select: auto;">'a'</code>) is not, so you would delete column 1.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of columns that you will delete</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> strs = ["cba","daf","ghi"]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> strs = ["a","b"]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> strs = ["zyx","wvu","tsr"]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == strs.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">strs[i]</code> consists of lowercase English letters.</li>
</ul>
</div>