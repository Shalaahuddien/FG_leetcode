<h2><a href="https://leetcode.com/problems/crawler-log-folder/">1598. Crawler Log Folder</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">The Leetcode file system keeps a log each time some user performs a <em style="user-select: auto;">change folder</em> operation.</p>

<p style="user-select: auto;">The operations are described below:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">"../"</code> : Move to the parent folder of the current folder. (If you are already in the main folder, <strong style="user-select: auto;">remain in the same folder</strong>).</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"./"</code> : Remain in the same folder.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"x/"</code> : Move to the child folder named <code style="user-select: auto;">x</code> (This folder is <strong style="user-select: auto;">guaranteed to always exist</strong>).</li>
</ul>

<p style="user-select: auto;">You are given a list of strings <code style="user-select: auto;">logs</code> where <code style="user-select: auto;">logs[i]</code> is the operation performed by the user at the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> step.</p>

<p style="user-select: auto;">The file system starts in the main folder, then the operations in <code style="user-select: auto;">logs</code> are performed.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the minimum number of operations needed to go back to the main folder after the change folder operations.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png" style="width: 775px; height: 151px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> logs = ["d1/","d2/","../","d21/","./"]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation: </strong>Use this change folder operation "../" 2 times and go back to the main folder.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png" style="width: 600px; height: 270px; user-select: auto;" title=""></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> logs = ["d1/","d2/","./","d3/","../","d31/"]
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> logs = ["d1/","../","../","../"]
<strong style="user-select: auto;">Output:</strong> 0
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= logs.length &lt;= 10<sup style="user-select: auto;">3</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= logs[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">logs[i]</code> contains lowercase English letters, digits, <code style="user-select: auto;">'.'</code>, and <code style="user-select: auto;">'/'</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">logs[i]</code> follows the format described in the statement.</li>
	<li style="user-select: auto;">Folder names consist of lowercase English letters and digits.</li>
</ul>
</div>