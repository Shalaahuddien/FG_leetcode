<h2><a href="https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/">914. X of a Kind in a Deck of Cards</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">In a deck of cards, each card has an integer written on it.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> if and only if you can choose <code style="user-select: auto;">X &gt;= 2</code> such that it is possible to split the entire deck into 1 or more groups of cards, where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Each group has exactly <code style="user-select: auto;">X</code> cards.</li>
	<li style="user-select: auto;">All the cards in each group have the same integer.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> deck = [1,2,3,4,4,3,2,1]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> deck = [1,1,1,2,2,2,3,3]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation</strong>: No possible partition.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= deck.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= deck[i] &lt; 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>