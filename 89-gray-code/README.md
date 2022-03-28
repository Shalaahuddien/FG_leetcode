<h2><a href="https://leetcode.com/problems/gray-code/">89. Gray Code</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">An <strong style="user-select: auto;">n-bit gray code sequence</strong> is a sequence of <code style="user-select: auto;">2<sup style="user-select: auto;">n</sup></code> integers where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Every integer is in the <strong style="user-select: auto;">inclusive</strong> range <code style="user-select: auto;">[0, 2<sup style="user-select: auto;">n</sup> - 1]</code>,</li>
	<li style="user-select: auto;">The first integer is <code style="user-select: auto;">0</code>,</li>
	<li style="user-select: auto;">An integer appears <strong style="user-select: auto;">no more than once</strong> in the sequence,</li>
	<li style="user-select: auto;">The binary representation of every pair of <strong style="user-select: auto;">adjacent</strong> integers differs by <strong style="user-select: auto;">exactly one bit</strong>, and</li>
	<li style="user-select: auto;">The binary representation of the <strong style="user-select: auto;">first</strong> and <strong style="user-select: auto;">last</strong> integers differs by <strong style="user-select: auto;">exactly one bit</strong>.</li>
</ul>

<p style="user-select: auto;">Given an integer <code style="user-select: auto;">n</code>, return <em style="user-select: auto;">any valid <strong style="user-select: auto;">n-bit gray code sequence</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 2
<strong style="user-select: auto;">Output:</strong> [0,1,3,2]
<strong style="user-select: auto;">Explanation:</strong>
The binary representation of [0,1,3,2] is [00,01,11,10].
- 0<u style="user-select: auto;">0</u> and 0<u style="user-select: auto;">1</u> differ by one bit
- <u style="user-select: auto;">0</u>1 and <u style="user-select: auto;">1</u>1 differ by one bit
- 1<u style="user-select: auto;">1</u> and 1<u style="user-select: auto;">0</u> differ by one bit
- <u style="user-select: auto;">1</u>0 and <u style="user-select: auto;">0</u>0 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- <u style="user-select: auto;">0</u>0 and <u style="user-select: auto;">1</u>0 differ by one bit
- 1<u style="user-select: auto;">0</u> and 1<u style="user-select: auto;">1</u> differ by one bit
- <u style="user-select: auto;">1</u>1 and <u style="user-select: auto;">0</u>1 differ by one bit
- 0<u style="user-select: auto;">1</u> and 0<u style="user-select: auto;">0</u> differ by one bit
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 1
<strong style="user-select: auto;">Output:</strong> [0,1]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 16</code></li>
</ul>
</div>