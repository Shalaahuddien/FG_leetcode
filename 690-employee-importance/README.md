<h2><a href="https://leetcode.com/problems/employee-importance/">690. Employee Importance</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.</p>

<p style="user-select: auto;">You are given an array of employees <code style="user-select: auto;">employees</code> where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">employees[i].id</code> is the ID of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> employee.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">employees[i].importance</code> is the importance value of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> employee.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">employees[i].subordinates</code> is a list of the IDs of the direct subordinates of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> employee.</li>
</ul>

<p style="user-select: auto;">Given an integer <code style="user-select: auto;">id</code> that represents an employee's ID, return <em style="user-select: auto;">the <strong style="user-select: auto;">total</strong> importance value of this employee and all their direct and indirect subordinates</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/31/emp1-tree.jpg" style="width: 400px; height: 258px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
<strong style="user-select: auto;">Output:</strong> 11
<strong style="user-select: auto;">Explanation:</strong> Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/31/emp2-tree.jpg" style="width: 362px; height: 361px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> employees = [[1,2,[5]],[5,-3,[]]], id = 5
<strong style="user-select: auto;">Output:</strong> -3
<strong style="user-select: auto;">Explanation:</strong> Employee 5 has an importance value of -3 and has no direct subordinates.
Thus, the total importance value of employee 5 is -3.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= employees.length &lt;= 2000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= employees[i].id &lt;= 2000</code></li>
	<li style="user-select: auto;">All <code style="user-select: auto;">employees[i].id</code> are <strong style="user-select: auto;">unique</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= employees[i].importance &lt;= 100</code></li>
	<li style="user-select: auto;">One employee has at most one direct leader and may have several subordinates.</li>
	<li style="user-select: auto;">The IDs in <code style="user-select: auto;">employees[i].subordinates</code> are valid IDs.</li>
</ul>
</div>