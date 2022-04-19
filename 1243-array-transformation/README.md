<h2><a href="https://leetcode.com/problems/array-transformation/">1243. Array Transformation</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an initial array <code style="user-select: auto;">arr</code>, every day you produce a new array using the array of the previous day.</p>

<p style="user-select: auto;">On the <code style="user-select: auto;">i</code>-th day, you do the following operations on the array of day&nbsp;<code style="user-select: auto;">i-1</code>&nbsp;to produce the array of day <code style="user-select: auto;">i</code>:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.</li>
	<li style="user-select: auto;">If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.</li>
	<li style="user-select: auto;">The first&nbsp;and last elements never change.</li>
</ol>

<p style="user-select: auto;">After some days, the array does not change. Return that final array.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [6,2,3,4]
<strong style="user-select: auto;">Output:</strong> [6,3,3,4]
<strong style="user-select: auto;">Explanation: </strong>
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,6,3,4,3,5]
<strong style="user-select: auto;">Output:</strong> [1,4,4,4,4,5]
<strong style="user-select: auto;">Explanation: </strong>
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">3 &lt;= arr.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr[i] &lt;= 100</code></li>
</ul>
</div>