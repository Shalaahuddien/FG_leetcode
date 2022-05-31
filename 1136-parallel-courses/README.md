<h2><a href="https://leetcode.com/problems/parallel-courses/">1136. Parallel Courses</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer <code style="user-select: auto;">n</code>, which indicates that there are <code style="user-select: auto;">n</code> courses labeled from <code style="user-select: auto;">1</code> to <code style="user-select: auto;">n</code>. You are also given an array <code style="user-select: auto;">relations</code> where <code style="user-select: auto;">relations[i] = [prevCourse<sub style="user-select: auto;">i</sub>, nextCourse<sub style="user-select: auto;">i</sub>]</code>, representing a prerequisite relationship between course <code style="user-select: auto;">prevCourse<sub style="user-select: auto;">i</sub></code> and course <code style="user-select: auto;">nextCourse<sub style="user-select: auto;">i</sub></code>: course <code style="user-select: auto;">prevCourse<sub style="user-select: auto;">i</sub></code> has to be taken before course <code style="user-select: auto;">nextCourse<sub style="user-select: auto;">i</sub></code>.</p>

<p style="user-select: auto;">In one semester, you can take <strong style="user-select: auto;">any number</strong> of courses as long as you have taken all the prerequisites in the <strong style="user-select: auto;">previous</strong> semester for the courses you are taking.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum</strong> number of semesters needed to take all courses</em>. If there is no way to take all the courses, return <code style="user-select: auto;">-1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/24/course1graph.jpg" style="width: 222px; height: 222px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 3, relations = [[1,3],[2,3]]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/24/course2graph.jpg" style="width: 222px; height: 222px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 3, relations = [[1,2],[2,3],[3,1]]
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> No course can be studied because they are prerequisites of each other.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= relations.length &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">relations[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= prevCourse<sub style="user-select: auto;">i</sub>, nextCourse<sub style="user-select: auto;">i</sub> &lt;= n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">prevCourse<sub style="user-select: auto;">i</sub> != nextCourse<sub style="user-select: auto;">i</sub></code></li>
	<li style="user-select: auto;">All the pairs <code style="user-select: auto;">[prevCourse<sub style="user-select: auto;">i</sub>, nextCourse<sub style="user-select: auto;">i</sub>]</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>