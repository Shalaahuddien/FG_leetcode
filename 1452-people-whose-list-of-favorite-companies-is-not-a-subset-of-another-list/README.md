<h2><a href="https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/">1452. People Whose List of Favorite Companies Is Not a Subset of Another List</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the array <code style="user-select: auto;">favoriteCompanies</code> where <code style="user-select: auto;">favoriteCompanies[i]</code> is the list of favorites companies for the <code style="user-select: auto;">ith</code> person (<strong style="user-select: auto;">indexed from 0</strong>).</p>

<p style="user-select: auto;"><em style="user-select: auto;">Return the indices of people whose list of favorite companies is not a <strong style="user-select: auto;">subset</strong> of any other list of favorites companies</em>. You must return the indices in increasing order.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
<strong style="user-select: auto;">Output:</strong> [0,1,4] 
<strong style="user-select: auto;">Explanation:</strong> 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
<strong style="user-select: auto;">Output:</strong> [0,1] 
<strong style="user-select: auto;">Explanation:</strong> In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
<strong style="user-select: auto;">Output:</strong> [0,1,2,3]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= favoriteCompanies.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= favoriteCompanies[i].length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= favoriteCompanies[i][j].length &lt;= 20</code></li>
	<li style="user-select: auto;">All strings in <code style="user-select: auto;">favoriteCompanies[i]</code> are <strong style="user-select: auto;">distinct</strong>.</li>
	<li style="user-select: auto;">All lists of favorite companies are <strong style="user-select: auto;">distinct</strong>, that is, If we sort alphabetically each list then <code style="user-select: auto;">favoriteCompanies[i] != favoriteCompanies[j].</code></li>
	<li style="user-select: auto;">All strings consist of lowercase English letters only.</li>
</ul>
</div>