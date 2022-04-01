<h2><a href="https://leetcode.com/problems/shopping-offers/">638. Shopping Offers</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">In LeetCode Store, there are <code style="user-select: auto;">n</code> items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.</p>

<p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">price</code> where <code style="user-select: auto;">price[i]</code> is the price of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> item, and an integer array <code style="user-select: auto;">needs</code> where <code style="user-select: auto;">needs[i]</code> is the number of pieces of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> item you want to buy.</p>

<p style="user-select: auto;">You are also given an array <code style="user-select: auto;">special</code> where <code style="user-select: auto;">special[i]</code> is of size <code style="user-select: auto;">n + 1</code> where <code style="user-select: auto;">special[i][j]</code> is the number of pieces of the <code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code> item in the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> offer and <code style="user-select: auto;">special[i][n]</code> (i.e., the last integer in the array) is the price of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> offer.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers</em>. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
<strong style="user-select: auto;">Output:</strong> 14
<strong style="user-select: auto;">Explanation:</strong> There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
<strong style="user-select: auto;">Output:</strong> 11
<strong style="user-select: auto;">Explanation:</strong> The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == price.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == needs.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 6</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= price[i] &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= needs[i] &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= special.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">special[i].length == n + 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= special[i][j] &lt;= 50</code></li>
</ul>
</div>