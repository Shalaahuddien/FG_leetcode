<h2><a href="https://leetcode.com/problems/candy/">135. Candy</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are <code style="user-select: auto;">n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code style="user-select: auto;">ratings</code>.</p>

<p style="user-select: auto;">You are giving candies to these children subjected to the following requirements:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Each child must have at least one candy.</li>
	<li style="user-select: auto;">Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the minimum number of candies you need to have to distribute the candies to the children</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> ratings = [1,0,2]
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> ratings = [1,2,2]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == ratings.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 2 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= ratings[i] &lt;= 2 * 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>