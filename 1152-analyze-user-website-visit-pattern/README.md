<h2><a href="https://leetcode.com/problems/analyze-user-website-visit-pattern/">1152. Analyze User Website Visit Pattern</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given two string arrays <code style="user-select: auto;">username</code> and <code style="user-select: auto;">website</code> and an integer array <code style="user-select: auto;">timestamp</code>. All the given arrays are of the same length and the tuple <code style="user-select: auto;">[username[i], website[i], timestamp[i]]</code> indicates that the user <code style="user-select: auto;">username[i]</code> visited the website <code style="user-select: auto;">website[i]</code> at time <code style="user-select: auto;">timestamp[i]</code>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">pattern</strong> is a list of three websites (not necessarily distinct).</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">["home", "away", "love"]</code>, <code style="user-select: auto;">["leetcode", "love", "leetcode"]</code>, and <code style="user-select: auto;">["luffy", "luffy", "luffy"]</code> are all patterns.</li>
</ul>

<p style="user-select: auto;">The <strong style="user-select: auto;">score</strong> of a <strong style="user-select: auto;">pattern</strong> is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, if the pattern is <code style="user-select: auto;">["home", "away", "love"]</code>, the score is the number of users <code style="user-select: auto;">x</code> such that <code style="user-select: auto;">x</code> visited <code style="user-select: auto;">"home"</code> then visited <code style="user-select: auto;">"away"</code> and visited <code style="user-select: auto;">"love"</code> after that.</li>
	<li style="user-select: auto;">Similarly, if the pattern is <code style="user-select: auto;">["leetcode", "love", "leetcode"]</code>, the score is the number of users <code style="user-select: auto;">x</code> such that <code style="user-select: auto;">x</code> visited <code style="user-select: auto;">"leetcode"</code> then visited <code style="user-select: auto;">"love"</code> and visited <code style="user-select: auto;">"leetcode"</code> <strong style="user-select: auto;">one more time</strong> after that.</li>
	<li style="user-select: auto;">Also, if the pattern is <code style="user-select: auto;">["luffy", "luffy", "luffy"]</code>, the score is the number of users <code style="user-select: auto;">x</code> such that <code style="user-select: auto;">x</code> visited <code style="user-select: auto;">"luffy"</code> three different times at different timestamps.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">pattern</strong> with the largest <strong style="user-select: auto;">score</strong></em>. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
<strong style="user-select: auto;">Output:</strong> ["home","about","career"]
<strong style="user-select: auto;">Explanation:</strong> The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
<strong style="user-select: auto;">Output:</strong> ["a","b","a"]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">3 &lt;= username.length &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= username[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">timestamp.length == username.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= timestamp[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">website.length == username.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= website[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">username[i]</code> and <code style="user-select: auto;">website[i]</code> consist of lowercase English letters.</li>
	<li style="user-select: auto;">It is guaranteed that there is at least one user who visited at least three websites.</li>
	<li style="user-select: auto;">All the tuples <code style="user-select: auto;">[username[i], timestamp[i], website[i]]</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>