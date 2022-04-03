<h2><a href="https://leetcode.com/problems/find-the-index-of-the-large-integer/">1533. Find the Index of the Large Integer</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">We have an integer array <code style="user-select: auto;">arr</code>, where all the integers in <code style="user-select: auto;">arr</code> are equal except for one integer which is <strong style="user-select: auto;">larger</strong> than the rest of the integers. You will not be given direct access to the array, instead, you will have an <strong style="user-select: auto;">API</strong> <code style="user-select: auto;">ArrayReader</code> which have the following functions:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">int compareSub(int l, int r, int x, int y)</code>: where <code style="user-select: auto;">0 &lt;= l, r, x, y &lt; ArrayReader.length()</code>, <code style="user-select: auto;">l &lt;= r and</code> <code style="user-select: auto;">x &lt;= y</code>. The function compares the sum of sub-array <code style="user-select: auto;">arr[l..r]</code> with the sum of the sub-array <code style="user-select: auto;">arr[x..y]</code> and returns:

	<ul style="user-select: auto;">
		<li style="user-select: auto;"><strong style="user-select: auto;">1</strong> if <code style="user-select: auto;">arr[l]+arr[l+1]+...+arr[r] &gt; arr[x]+arr[x+1]+...+arr[y]</code>.</li>
		<li style="user-select: auto;"><strong style="user-select: auto;">0</strong> if <code style="user-select: auto;">arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y]</code>.</li>
		<li style="user-select: auto;"><strong style="user-select: auto;">-1</strong> if <code style="user-select: auto;">arr[l]+arr[l+1]+...+arr[r] &lt; arr[x]+arr[x+1]+...+arr[y]</code>.</li>
	</ul>
	</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int length()</code>: Returns the size of the array.</li>
</ul>

<p style="user-select: auto;">You are allowed to call <code style="user-select: auto;">compareSub()</code> <b style="user-select: auto;">20 times</b> at most. You can assume both functions work in <code style="user-select: auto;">O(1)</code> time.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the index of the array <code style="user-select: auto;">arr</code> which has the largest integer</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [7,7,7,7,10,7,7,7]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> The following calls to the API
reader.compareSub(0, 0, 1, 1) // returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with arr[1]).
Thus we know that arr[0] and arr[1] doesn't contain the largest element.
reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
Notice that we made only 3 calls, so the answer is valid.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [6,6,12]
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= arr.length &lt;= 5 * 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr[i] &lt;= 100</code></li>
	<li style="user-select: auto;">All elements of <code style="user-select: auto;">arr</code> are equal except for one element which is larger than all other elements.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">What if there are two numbers in <code style="user-select: auto;">arr</code> that are bigger than all other numbers?</li>
	<li style="user-select: auto;">What if there is one number that is bigger than other numbers and one number that is smaller than other numbers?</li>
</ul>
</div>