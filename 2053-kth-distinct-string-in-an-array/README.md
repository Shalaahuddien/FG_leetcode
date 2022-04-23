<h2><a href="https://leetcode.com/problems/kth-distinct-string-in-an-array/">2053. Kth Distinct String in an Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;">distinct string</strong> is a string that is present only <strong style="user-select: auto;">once</strong> in an array.</p>

<p style="user-select: auto;">Given an array of strings <code style="user-select: auto;">arr</code>, and an integer <code style="user-select: auto;">k</code>, return <em style="user-select: auto;">the </em><code style="user-select: auto;">k<sup style="user-select: auto;">th</sup></code><em style="user-select: auto;"> <strong style="user-select: auto;">distinct string</strong> present in </em><code style="user-select: auto;">arr</code>. If there are <strong style="user-select: auto;">fewer</strong> than <code style="user-select: auto;">k</code> distinct strings, return <em style="user-select: auto;">an <strong style="user-select: auto;">empty string </strong></em><code style="user-select: auto;">""</code>.</p>

<p style="user-select: auto;">Note that the strings are considered in the <strong style="user-select: auto;">order in which they appear</strong> in the array.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = ["d","b","c","b","c","a"], k = 2
<strong style="user-select: auto;">Output:</strong> "a"
<strong style="user-select: auto;">Explanation:</strong>
The only distinct strings in arr are "d" and "a".
"d" appears 1<sup style="user-select: auto;">st</sup>, so it is the 1<sup style="user-select: auto;">st</sup> distinct string.
"a" appears 2<sup style="user-select: auto;">nd</sup>, so it is the 2<sup style="user-select: auto;">nd</sup> distinct string.
Since k == 2, "a" is returned. 
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = ["aaa","aa","a"], k = 1
<strong style="user-select: auto;">Output:</strong> "aaa"
<strong style="user-select: auto;">Explanation:</strong>
All strings in arr are distinct, so the 1<sup style="user-select: auto;">st</sup> string "aaa" is returned.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = ["a","b","a"], k = 3
<strong style="user-select: auto;">Output:</strong> ""
<strong style="user-select: auto;">Explanation:</strong>
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= arr.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr[i].length &lt;= 5</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">arr[i]</code> consists of lowercase English letters.</li>
</ul>
</div>