<h2><a href="https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/">1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two arrays of integers <code style="user-select: auto;">nums1</code> and <code style="user-select: auto;">nums2</code>, return the number of triplets formed (type 1 and type 2) under the following rules:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Type 1: Triplet (i, j, k) if <code style="user-select: auto;">nums1[i]<sup style="user-select: auto;">2</sup> == nums2[j] * nums2[k]</code> where <code style="user-select: auto;">0 &lt;= i &lt; nums1.length</code> and <code style="user-select: auto;">0 &lt;= j &lt; k &lt; nums2.length</code>.</li>
	<li style="user-select: auto;">Type 2: Triplet (i, j, k) if <code style="user-select: auto;">nums2[i]<sup style="user-select: auto;">2</sup> == nums1[j] * nums1[k]</code> where <code style="user-select: auto;">0 &lt;= i &lt; nums2.length</code> and <code style="user-select: auto;">0 &lt;= j &lt; k &lt; nums1.length</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums1 = [7,4], nums2 = [5,2,8,9]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> Type 1: (1, 1, 2), nums1[1]<sup style="user-select: auto;">2</sup> = nums2[1] * nums2[2]. (4<sup style="user-select: auto;">2</sup> = 2 * 8). 
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums1 = [1,1], nums2 = [1,1,1]
<strong style="user-select: auto;">Output:</strong> 9
<strong style="user-select: auto;">Explanation:</strong> All Triplets are valid, because 1<sup style="user-select: auto;">2</sup> = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]<sup style="user-select: auto;">2</sup> = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]<sup style="user-select: auto;">2</sup> = nums1[j] * nums1[k].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums1 = [7,7,8,3], nums2 = [1,2,9,7]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]<sup style="user-select: auto;">2</sup> = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]<sup style="user-select: auto;">2</sup> = nums1[0] * nums1[1].
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums1[i], nums2[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>