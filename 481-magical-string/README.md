<h2><a href="https://leetcode.com/problems/magical-string/">481. Magical String</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A magical string <code style="user-select: auto;">s</code> consists of only <code style="user-select: auto;">'1'</code> and <code style="user-select: auto;">'2'</code> and obeys the following rules:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The string s is magical because concatenating the number of contiguous occurrences of characters <code style="user-select: auto;">'1'</code> and <code style="user-select: auto;">'2'</code> generates the string <code style="user-select: auto;">s</code> itself.</li>
</ul>

<p style="user-select: auto;">The first few elements of <code style="user-select: auto;">s</code> is <code style="user-select: auto;">s = "1221121221221121122……"</code>. If we group the consecutive <code style="user-select: auto;">1</code>'s and <code style="user-select: auto;">2</code>'s in <code style="user-select: auto;">s</code>, it will be <code style="user-select: auto;">"1 22 11 2 1 22 1 22 11 2 11 22 ......"</code> and the occurrences of <code style="user-select: auto;">1</code>'s or <code style="user-select: auto;">2</code>'s in each group are <code style="user-select: auto;">"1 2 2 1 1 2 1 2 2 1 2 2 ......"</code>. You can see that the occurrence sequence is <code style="user-select: auto;">s</code> itself.</p>

<p style="user-select: auto;">Given an integer <code style="user-select: auto;">n</code>, return the number of <code style="user-select: auto;">1</code>'s in the first <code style="user-select: auto;">n</code> number in the magical string <code style="user-select: auto;">s</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 6
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 1
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>