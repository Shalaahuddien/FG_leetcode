<h2><a href="https://leetcode.com/problems/prefix-and-suffix-search/">745. Prefix and Suffix Search</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">WordFilter</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">WordFilter(string[] words)</code> Initializes the object with the <code style="user-select: auto;">words</code> in the dictionary.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">f(string prefix, string suffix)</code> Returns <em style="user-select: auto;">the index of the word in the dictionary,</em> which has the prefix <code style="user-select: auto;">prefix</code> and the suffix <code style="user-select: auto;">suffix</code>. If there is more than one valid index, return <strong style="user-select: auto;">the largest</strong> of them. If there is no such word in the dictionary, return <code style="user-select: auto;">-1</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
<strong style="user-select: auto;">Output</strong>
[null, 0]

<strong style="user-select: auto;">Explanation</strong>
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words.length &lt;= 15000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= prefix.length, suffix.length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">words[i]</code>, <code style="user-select: auto;">prefix</code> and <code style="user-select: auto;">suffix</code> consist of lower-case English letters only.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">15000</code> calls will be made to the function <code style="user-select: auto;">f</code>.</li>
</ul>
</div>