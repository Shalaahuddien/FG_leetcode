<h2><a href="https://leetcode.com/problems/statistics-from-a-large-sample/">1093. Statistics from a Large Sample</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a large sample of integers in the range <code style="user-select: auto;">[0, 255]</code>. Since the sample is so large, it is represented by an array <code style="user-select: auto;">count</code>&nbsp;where <code style="user-select: auto;">count[k]</code> is the <strong style="user-select: auto;">number of times</strong> that <code style="user-select: auto;">k</code> appears in the sample.</p>

<p style="user-select: auto;">Calculate the following statistics:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">minimum</code>: The minimum element in the sample.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">maximum</code>: The maximum element in the sample.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">mean</code>: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">median</code>:
	<ul style="user-select: auto;">
		<li style="user-select: auto;">If the sample has an odd number of elements, then the <code style="user-select: auto;">median</code> is the middle element once the sample is sorted.</li>
		<li style="user-select: auto;">If the sample has an even number of elements, then the <code style="user-select: auto;">median</code> is the average of the two middle elements once the sample is sorted.</li>
	</ul>
	</li>
	<li style="user-select: auto;"><code style="user-select: auto;">mode</code>: The number that appears the most in the sample. It is guaranteed to be <strong style="user-select: auto;">unique</strong>.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the statistics of the sample as an array of floating-point numbers </em><code style="user-select: auto;">[minimum, maximum, mean, median, mode]</code><em style="user-select: auto;">. Answers within </em><code style="user-select: auto;">10<sup style="user-select: auto;">-5</sup></code><em style="user-select: auto;"> of the actual answer will be accepted.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong style="user-select: auto;">Output:</strong> [1.00000,3.00000,2.37500,2.50000,3.00000]
<strong style="user-select: auto;">Explanation:</strong> The sample represented by count is [1,2,2,2,3,3,3,3].
The minimum and maximum are 1 and 3 respectively.
The mean is (1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375.
Since the size of the sample is even, the median is the average of the two middle elements 2 and 3, which is 2.5.
The mode is 3 as it appears the most in the sample.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong style="user-select: auto;">Output:</strong> [1.00000,4.00000,2.18182,2.00000,1.00000]
<strong style="user-select: auto;">Explanation:</strong> The sample represented by count is [1,1,1,1,2,2,2,3,3,4,4].
The minimum and maximum are 1 and 4 respectively.
The mean is (1+1+1+1+2+2+2+3+3+4+4) / 11 = 24 / 11 = 2.18181818... (for display purposes, the output shows the rounded number 2.18182).
Since the size of the sample is odd, the median is the middle element 2.
The mode is 1 as it appears the most in the sample.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">count.length == 256</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= count[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= sum(count) &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;">The mode of the sample that <code style="user-select: auto;">count</code> represents is <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>