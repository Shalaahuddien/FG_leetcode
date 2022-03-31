<h2><a href="https://leetcode.com/problems/lemonade-change/">860. Lemonade Change</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">At a lemonade stand, each lemonade costs <code style="user-select: auto;">$5</code>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a <code style="user-select: auto;">$5</code>, <code style="user-select: auto;">$10</code>, or <code style="user-select: auto;">$20</code> bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <code style="user-select: auto;">$5</code>.</p>

<p style="user-select: auto;">Note that you do not have any change in hand at first.</p>

<p style="user-select: auto;">Given an integer array <code style="user-select: auto;">bills</code> where <code style="user-select: auto;">bills[i]</code> is the bill the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> customer pays, return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if you can provide every customer with the correct change, or</em> <code style="user-select: auto;">false</code> <em style="user-select: auto;">otherwise</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> bills = [5,5,5,10,20]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> bills = [5,5,10,10,20]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= bills.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">bills[i]</code> is either <code style="user-select: auto;">5</code>, <code style="user-select: auto;">10</code>, or <code style="user-select: auto;">20</code>.</li>
</ul>
</div>