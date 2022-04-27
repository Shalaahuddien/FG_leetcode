<h2><a href="https://leetcode.com/problems/design-file-system/">1166. Design File System</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are asked to design a file system&nbsp;that allows you to create new paths and associate them with different values.</p>

<p style="user-select: auto;">The format of a path is&nbsp;one or more concatenated strings of the form:&nbsp;<code style="user-select: auto;">/</code> followed by one or more lowercase English letters. For example, "<code style="user-select: auto;">/leetcode"</code>&nbsp;and "<code style="user-select: auto;">/leetcode/problems"</code>&nbsp;are valid paths while an empty&nbsp;string <code style="user-select: auto;">""</code> and <code style="user-select: auto;">"/"</code>&nbsp;are not.</p>

<p style="user-select: auto;">Implement the&nbsp;<code style="user-select: auto;">FileSystem</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">bool createPath(string path, int value)</code>&nbsp;Creates a new <code style="user-select: auto;">path</code> and associates a <code style="user-select: auto;">value</code> to it if possible and returns <code style="user-select: auto;">true</code>.&nbsp;Returns <code style="user-select: auto;">false</code>&nbsp;if the path <strong style="user-select: auto;">already exists</strong> or its parent path <strong style="user-select: auto;">doesn't exist</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int get(string path)</code>&nbsp;Returns the value associated with <code style="user-select: auto;">path</code> or returns&nbsp;<code style="user-select: auto;">-1</code>&nbsp;if the path doesn't exist.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
<strong style="user-select: auto;">Output:</strong> 
[null,true,1]
<strong style="user-select: auto;">Explanation:</strong> 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
<strong style="user-select: auto;">Output:</strong> 
[null,true,true,2,false,-1]
<strong style="user-select: auto;">Explanation:</strong> 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of&nbsp;calls to the two functions&nbsp;is less than or equal to <code style="user-select: auto;">10<sup style="user-select: auto;">4</sup></code> in total.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= path.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= value &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>