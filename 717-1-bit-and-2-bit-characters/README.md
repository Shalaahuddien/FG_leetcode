<h2><a href="https://leetcode.com/problems/1-bit-and-2-bit-characters/">717. 1-bit and 2-bit Characters</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">We have two special characters:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The first character can be represented by one bit <code style="user-select: auto;">0</code>.</li>
	<li style="user-select: auto;">The second character can be represented by two bits (<code style="user-select: auto;">10</code> or <code style="user-select: auto;">11</code>).</li>
</ul>

<p style="user-select: auto;">Given a binary array <code style="user-select: auto;">bits</code> that ends with <code style="user-select: auto;">0</code>, return <code style="user-select: auto;">true</code> if the last character must be a one-bit character.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> bits = [1,0,0]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> bits = [1,1,1,0]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= bits.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">bits[i]</code> is either <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
</ul>
</div>