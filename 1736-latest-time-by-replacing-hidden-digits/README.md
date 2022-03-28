<h2><a href="https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/">1736. Latest Time by Replacing Hidden Digits</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">time</code> in the form of <code style="user-select: auto;"> hh:mm</code>, where some of the digits in the string are hidden (represented by <code style="user-select: auto;">?</code>).</p>

<p style="user-select: auto;">The valid times are those inclusively between <code style="user-select: auto;">00:00</code> and <code style="user-select: auto;">23:59</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the latest valid time you can get from</em> <code style="user-select: auto;">time</code><em style="user-select: auto;"> by replacing the hidden</em> <em style="user-select: auto;">digits</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> time = "2?:?0"
<strong style="user-select: auto;">Output:</strong> "23:50"
<strong style="user-select: auto;">Explanation:</strong> The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> time = "0?:3?"
<strong style="user-select: auto;">Output:</strong> "09:39"
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> time = "1?:22"
<strong style="user-select: auto;">Output:</strong> "19:22"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">time</code> is in the format <code style="user-select: auto;">hh:mm</code>.</li>
	<li style="user-select: auto;">It is guaranteed that you can produce a valid time from the given string.</li>
</ul>
</div>