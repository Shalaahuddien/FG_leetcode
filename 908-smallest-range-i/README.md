<h2><a href="https://leetcode.com/problems/smallest-range-i/">908. Smallest Range I</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">nums</code> and an integer <code style="user-select: auto;">k</code>.</p>

<p style="user-select: auto;">In one operation, you can choose any index <code style="user-select: auto;">i</code> where <code style="user-select: auto;">0 &lt;= i &lt; nums.length</code> and change <code style="user-select: auto;">nums[i]</code> to <code style="user-select: auto;">nums[i] + x</code> where <code style="user-select: auto;">x</code> is an integer from the range <code style="user-select: auto;">[-k, k]</code>. You can apply this operation <strong style="user-select: auto;">at most once</strong> for each index <code style="user-select: auto;">i</code>.</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">score</strong> of <code style="user-select: auto;">nums</code> is the difference between the maximum and minimum elements in <code style="user-select: auto;">nums</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the minimum <strong style="user-select: auto;">score</strong> of </em><code style="user-select: auto;">nums</code><em style="user-select: auto;"> after applying the mentioned operation at most once for each index in it</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1], k = 0
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The score is max(nums) - min(nums) = 1 - 1 = 0.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0,10], k = 2
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation:</strong> Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,3,6], k = 3
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= k &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>