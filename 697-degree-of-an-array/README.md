<h2><a href="https://leetcode.com/problems/degree-of-an-array/">697. Degree of an Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a non-empty array of non-negative integers <code style="user-select: auto;">nums</code>, the <b style="user-select: auto;">degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>

<p style="user-select: auto;">Your task is to find the smallest possible length of a (contiguous) subarray of <code style="user-select: auto;">nums</code>, that has the same degree as <code style="user-select: auto;">nums</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,2,3,1]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,2,3,1,4,2]
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation:</strong> 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">nums.length</code> will be between 1 and 50,000.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i]</code> will be an integer between 0 and 49,999.</li>
</ul>
</div>