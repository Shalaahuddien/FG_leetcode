<h2><a href="https://leetcode.com/problems/find-the-celebrity/">277. Find the Celebrity</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Suppose you are at a party with <code style="user-select: auto;">n</code> people labeled from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">n - 1</code> and among them, there may exist one celebrity. The definition of a celebrity is that all the other <code style="user-select: auto;">n - 1</code> people know the celebrity, but the celebrity does not know any of them.</p>

<p style="user-select: auto;">Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).</p>

<p style="user-select: auto;">You are given a helper function <code style="user-select: auto;">bool knows(a, b)</code> that tells you whether A knows B. Implement a function <code style="user-select: auto;">int findCelebrity(n)</code>. There will be exactly one celebrity if they are at the party.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the celebrity's label if there is a celebrity at the party</em>. If there is no celebrity, return <code style="user-select: auto;">-1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g1.jpg" style="width: 224px; height: 145px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> graph = [[1,1,0],[0,1,0],[1,1,1]]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g2.jpg" style="width: 224px; height: 145px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> graph = [[1,0,1],[1,1,0],[0,1,1]]
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> There is no celebrity.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == graph.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == graph[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">graph[i][j]</code> is <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">graph[i][i] == 1</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> If the maximum number of allowed calls to the API <code style="user-select: auto;">knows</code> is <code style="user-select: auto;">3 * n</code>, could you find a solution without exceeding the maximum number of calls?</p>
</div>