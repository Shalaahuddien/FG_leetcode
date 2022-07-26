<h2><a href="https://leetcode.com/problems/all-paths-from-source-lead-to-destination/">1059. All Paths from Source Lead to Destination</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">edges</code> of a directed graph where <code style="user-select: auto;">edges[i] = [a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub>]</code> indicates there is an edge between nodes <code style="user-select: auto;">a<sub style="user-select: auto;">i</sub></code> and <code style="user-select: auto;">b<sub style="user-select: auto;">i</sub></code>, and two nodes <code style="user-select: auto;">source</code> and <code style="user-select: auto;">destination</code> of this graph, determine whether or not all paths starting from <code style="user-select: auto;">source</code> eventually, end at <code style="user-select: auto;">destination</code>, that is:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">At least one path exists from the <code style="user-select: auto;">source</code> node to the <code style="user-select: auto;">destination</code> node</li>
	<li style="user-select: auto;">If a path exists from the <code style="user-select: auto;">source</code> node to a node with no outgoing edges, then that node is equal to <code style="user-select: auto;">destination</code>.</li>
	<li style="user-select: auto;">The number of possible paths from <code style="user-select: auto;">source</code> to <code style="user-select: auto;">destination</code> is a finite number.</li>
</ul>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> if and only if all roads from <code style="user-select: auto;">source</code> lead to <code style="user-select: auto;">destination</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/16/485_example_1.png" style="width: 200px; height: 208px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> It is possible to reach and get stuck on both node 1 and node 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/16/485_example_2.png" style="width: 200px; height: 230px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/16/485_example_3.png" style="width: 200px; height: 183px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= edges.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">edges.length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub> &lt;= n - 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= source &lt;= n - 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= destination &lt;= n - 1</code></li>
	<li style="user-select: auto;">The given graph may have self-loops and parallel edges.</li>
</ul>
</div>