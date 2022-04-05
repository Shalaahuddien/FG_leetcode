<h2><a href="https://leetcode.com/problems/distribute-candies/">575. Distribute Candies</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Alice has <code style="user-select: auto;">n</code> candies, where the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> candy is of type <code style="user-select: auto;">candyType[i]</code>. Alice noticed that she started to gain weight, so she visited a doctor.</p>

<p style="user-select: auto;">The doctor advised Alice to only eat <code style="user-select: auto;">n / 2</code> of the candies she has (<code style="user-select: auto;">n</code> is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.</p>

<p style="user-select: auto;">Given the integer array <code style="user-select: auto;">candyType</code> of length <code style="user-select: auto;">n</code>, return <em style="user-select: auto;">the <strong style="user-select: auto;">maximum</strong> number of different types of candies she can eat if she only eats </em><code style="user-select: auto;">n / 2</code><em style="user-select: auto;"> of them</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> candyType = [1,1,2,2,3,3]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> candyType = [1,1,2,3]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> candyType = [6,6,6,6]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == candyType.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= n &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n</code>&nbsp;is even.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= candyType[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>