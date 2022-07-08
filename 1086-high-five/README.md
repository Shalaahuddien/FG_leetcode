<h2><a href="https://leetcode.com/problems/high-five/">1086. High Five</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a list of the scores of different students, <code style="user-select: auto;">items</code>, where <code style="user-select: auto;">items[i] = [ID<sub style="user-select: auto;">i</sub>, score<sub style="user-select: auto;">i</sub>]</code> represents one score from a student with <code style="user-select: auto;">ID<sub style="user-select: auto;">i</sub></code>, calculate each student's <strong style="user-select: auto;">top five average</strong>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the answer as an array of pairs </em><code style="user-select: auto;">result</code><em style="user-select: auto;">, where </em><code style="user-select: auto;">result[j] = [ID<sub style="user-select: auto;">j</sub>, topFiveAverage<sub style="user-select: auto;">j</sub>]</code><em style="user-select: auto;"> represents the student with </em><code style="user-select: auto;">ID<sub style="user-select: auto;">j</sub></code><em style="user-select: auto;"> and their <strong style="user-select: auto;">top five average</strong>. Sort </em><code style="user-select: auto;">result</code><em style="user-select: auto;"> by </em><code style="user-select: auto;">ID<sub style="user-select: auto;">j</sub></code><em style="user-select: auto;"> in <strong style="user-select: auto;">increasing order</strong>.</em></p>

<p style="user-select: auto;">A student's <strong style="user-select: auto;">top five average</strong> is calculated by taking the sum of their top five scores and dividing it by <code style="user-select: auto;">5</code> using <strong style="user-select: auto;">integer division</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
<strong style="user-select: auto;">Output:</strong> [[1,87],[2,88]]
<strong style="user-select: auto;">Explanation: </strong>
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
<strong style="user-select: auto;">Output:</strong> [[1,100],[7,100]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= items.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">items[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= ID<sub style="user-select: auto;">i</sub> &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= score<sub style="user-select: auto;">i</sub> &lt;= 100</code></li>
	<li style="user-select: auto;">For each <code style="user-select: auto;">ID<sub style="user-select: auto;">i</sub></code>, there will be <strong style="user-select: auto;">at least</strong> five scores.</li>
</ul>
</div>