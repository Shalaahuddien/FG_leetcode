<h2><a href="https://leetcode.com/problems/flip-game/">293. Flip Game</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are playing a Flip Game with your friend.</p>

<p style="user-select: auto;">You are given a string <code style="user-select: auto;">currentState</code> that contains only <code style="user-select: auto;">'+'</code> and <code style="user-select: auto;">'-'</code>. You and your friend take turns to flip <strong style="user-select: auto;">two consecutive</strong> <code style="user-select: auto;">"++"</code> into <code style="user-select: auto;">"--"</code>. The game ends when a person can no longer make a move, and therefore the other person will be the winner.</p>

<p style="user-select: auto;">Return all possible states of the string <code style="user-select: auto;">currentState</code> after <strong style="user-select: auto;">one valid move</strong>. You may return the answer in <strong style="user-select: auto;">any order</strong>. If there is no valid move, return an empty list <code style="user-select: auto;">[]</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> currentState = "++++"
<strong style="user-select: auto;">Output:</strong> ["--++","+--+","++--"]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> currentState = "+"
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= currentState.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">currentState[i]</code> is either <code style="user-select: auto;">'+'</code> or <code style="user-select: auto;">'-'</code>.</li>
</ul>
</div>