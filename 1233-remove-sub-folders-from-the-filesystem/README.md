<h2><a href="https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/">1233. Remove Sub-Folders from the Filesystem</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a list of folders <code style="user-select: auto;">folder</code>, return <em style="user-select: auto;">the folders after removing all <strong style="user-select: auto;">sub-folders</strong> in those folders</em>. You may return the answer in <strong style="user-select: auto;">any order</strong>.</p>

<p style="user-select: auto;">If a <code style="user-select: auto;">folder[i]</code> is located within another <code style="user-select: auto;">folder[j]</code>, it is called a <strong style="user-select: auto;">sub-folder</strong> of it.</p>

<p style="user-select: auto;">The format of a path is one or more concatenated strings of the form: <code style="user-select: auto;">'/'</code> followed by one or more lowercase English letters.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">"/leetcode"</code> and <code style="user-select: auto;">"/leetcode/problems"</code> are valid paths while an empty string and <code style="user-select: auto;">"/"</code> are not.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
<strong style="user-select: auto;">Output:</strong> ["/a","/c/d","/c/f"]
<strong style="user-select: auto;">Explanation:</strong> Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> folder = ["/a","/a/b/c","/a/b/d"]
<strong style="user-select: auto;">Output:</strong> ["/a"]
<strong style="user-select: auto;">Explanation:</strong> Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> folder = ["/a/b/c","/a/b/ca","/a/b/d"]
<strong style="user-select: auto;">Output:</strong> ["/a/b/c","/a/b/ca","/a/b/d"]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= folder.length &lt;= 4 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= folder[i].length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">folder[i]</code> contains only lowercase letters and <code style="user-select: auto;">'/'</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">folder[i]</code> always starts with the character <code style="user-select: auto;">'/'</code>.</li>
	<li style="user-select: auto;">Each folder name is <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>