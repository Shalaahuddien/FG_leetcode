<h2><a href="https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/">1450. Number of Students Doing Homework at a Given Time</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two integer arrays <code style="user-select: auto;">startTime</code> and <code style="user-select: auto;">endTime</code> and given an integer <code style="user-select: auto;">queryTime</code>.</p>

<p style="user-select: auto;">The <code style="user-select: auto;">ith</code> student started doing their homework at the time <code style="user-select: auto;">startTime[i]</code> and finished it at time <code style="user-select: auto;">endTime[i]</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of students</em> doing their homework at time <code style="user-select: auto;">queryTime</code>. More formally, return the number of students where <code style="user-select: auto;">queryTime</code> lays in the interval <code style="user-select: auto;">[startTime[i], endTime[i]]</code> inclusive.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> startTime = [4], endTime = [4], queryTime = 4
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> The only student was doing their homework at the queryTime.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">startTime.length == endTime.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= startTime.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= startTime[i] &lt;= endTime[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= queryTime &lt;= 1000</code></li>
</ul>
</div>