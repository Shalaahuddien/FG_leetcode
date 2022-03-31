<h2><a href="https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/">2037. Minimum Number of Moves to Seat Everyone</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are <code style="user-select: auto;">n</code> seats and <code style="user-select: auto;">n</code> students in a room. You are given an array <code style="user-select: auto;">seats</code> of length <code style="user-select: auto;">n</code>, where <code style="user-select: auto;">seats[i]</code> is the position of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> seat. You are also given the array <code style="user-select: auto;">students</code> of length <code style="user-select: auto;">n</code>, where <code style="user-select: auto;">students[j]</code> is the position of the <code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code> student.</p>

<p style="user-select: auto;">You may perform the following move any number of times:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Increase or decrease the position of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> student by <code style="user-select: auto;">1</code> (i.e., moving the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> student from position&nbsp;<code style="user-select: auto;">x</code>&nbsp;to <code style="user-select: auto;">x + 1</code> or <code style="user-select: auto;">x - 1</code>)</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum number of moves</strong> required to move each student to a seat</em><em style="user-select: auto;"> such that no two students are in the same seat.</em></p>

<p style="user-select: auto;">Note that there may be <strong style="user-select: auto;">multiple</strong> seats or students in the <strong style="user-select: auto;">same </strong>position at the beginning.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> seats = [3,1,5], students = [2,7,4]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> The students are moved as follows:
- The first student is moved from from position 2 to position 1 using 1 move.
- The second student is moved from from position 7 to position 5 using 2 moves.
- The third student is moved from from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> seats = [4,1,5,9], students = [1,3,2,6]
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation:</strong> The students are moved as follows:
- The first student is not moved.
- The second student is moved from from position 3 to position 4 using 1 move.
- The third student is moved from from position 2 to position 5 using 3 moves.
- The fourth student is moved from from position 6 to position 9 using 3 moves.
In total, 0 + 1 + 3 + 3 = 7 moves were used.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> seats = [2,2,6,6], students = [1,3,2,6]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> Note that there are two seats at position 2 and two seats at position 6.
The students are moved as follows:
- The first student is moved from from position 1 to position 2 using 1 move.
- The second student is moved from from position 3 to position 6 using 3 moves.
- The third student is not moved.
- The fourth student is not moved.
In total, 1 + 3 + 0 + 0 = 4 moves were used.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == seats.length == students.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= seats[i], students[j] &lt;= 100</code></li>
</ul>
</div>