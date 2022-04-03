<h2><a href="https://leetcode.com/problems/find-palindrome-with-fixed-length/">2217. Find Palindrome With Fixed Length</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">queries</code> and a <strong style="user-select: auto;">positive</strong> integer <code style="user-select: auto;">intLength</code>, return <em style="user-select: auto;">an array</em> <code style="user-select: auto;">answer</code> <em style="user-select: auto;">where</em> <code style="user-select: auto;">answer[i]</code> <em style="user-select: auto;">is either the </em><code style="user-select: auto;">queries[i]<sup style="user-select: auto;">th</sup></code> <em style="user-select: auto;">smallest <strong style="user-select: auto;">positive palindrome</strong> of length</em> <code style="user-select: auto;">intLength</code> <em style="user-select: auto;">or</em> <code style="user-select: auto;">-1</code><em style="user-select: auto;"> if no such palindrome exists</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">palindrome</strong> is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> queries = [1,2,3,4,5,90], intLength = 3
<strong style="user-select: auto;">Output:</strong> [101,111,121,131,141,999]
<strong style="user-select: auto;">Explanation:</strong>
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90<sup style="user-select: auto;">th</sup> palindrome of length 3 is 999.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> queries = [2,4,6], intLength = 4
<strong style="user-select: auto;">Output:</strong> [1111,1331,1551]
<strong style="user-select: auto;">Explanation:</strong>
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= queries.length &lt;= 5 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= queries[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= intLength&nbsp;&lt;= 15</code></li>
</ul>
</div>