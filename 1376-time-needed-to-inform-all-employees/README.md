<h2><a href="https://leetcode.com/problems/time-needed-to-inform-all-employees/">1376. Time Needed to Inform All Employees</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A company has <code style="user-select: auto;">n</code> employees with a unique ID for each employee from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">n - 1</code>. The head of the company is the one with <code style="user-select: auto;">headID</code>.</p>

<p style="user-select: auto;">Each employee has one direct manager given in the <code style="user-select: auto;">manager</code> array where <code style="user-select: auto;">manager[i]</code> is the direct manager of the <code style="user-select: auto;">i-th</code> employee, <code style="user-select: auto;">manager[headID] = -1</code>. Also, it is guaranteed that the subordination relationships have a tree structure.</p>

<p style="user-select: auto;">The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.</p>

<p style="user-select: auto;">The <code style="user-select: auto;">i-th</code> employee needs <code style="user-select: auto;">informTime[i]</code> minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of minutes</em> needed to inform all the employees about the urgent news.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 1, headID = 0, manager = [-1], informTime = [0]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The head of the company is the only employee in the company.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/27/graph.png" style="width: 404px; height: 174px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= headID &lt; n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">manager.length == n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= manager[i] &lt; n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">manager[headID] == -1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">informTime.length == n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= informTime[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">informTime[i] == 0</code> if employee <code style="user-select: auto;">i</code> has no subordinates.</li>
	<li style="user-select: auto;">It is <strong style="user-select: auto;">guaranteed</strong> that all the employees can be informed.</li>
</ul>
</div>