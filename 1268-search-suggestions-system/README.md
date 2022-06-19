<h2><a href="https://leetcode.com/problems/search-suggestions-system/">1268. Search Suggestions System</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an array of strings <code style="user-select: auto;">products</code> and a string <code style="user-select: auto;">searchWord</code>.</p>

<p style="user-select: auto;">Design a system that suggests at most three product names from <code style="user-select: auto;">products</code> after each character of <code style="user-select: auto;">searchWord</code> is typed. Suggested products should have common prefix with <code style="user-select: auto;">searchWord</code>. If there are more than three products with a common prefix return the three lexicographically minimums products.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">a list of lists of the suggested products after each character of </em><code style="user-select: auto;">searchWord</code><em style="user-select: auto;"> is typed</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
<strong style="user-select: auto;">Output:</strong> [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
<strong style="user-select: auto;">Explanation:</strong> products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> products = ["havana"], searchWord = "havana"
<strong style="user-select: auto;">Output:</strong> [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
<strong style="user-select: auto;">Output:</strong> [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= products.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= products[i].length &lt;= 3000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= sum(products[i].length) &lt;= 2 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;">All the strings of <code style="user-select: auto;">products</code> are <strong style="user-select: auto;">unique</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">products[i]</code> consists of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= searchWord.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">searchWord</code> consists of lowercase English letters.</li>
</ul>
</div>