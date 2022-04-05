<h2><a href="https://leetcode.com/problems/product-of-the-last-k-numbers/">1352. Product of the Last K Numbers</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design an algorithm that accepts a stream of integers and retrieves the product of the last <code style="user-select: auto;">k</code> integers of the stream.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">ProductOfNumbers</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">ProductOfNumbers()</code> Initializes the object with an empty stream.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void add(int num)</code> Appends the integer <code style="user-select: auto;">num</code> to the stream.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int getProduct(int k)</code> Returns the product of the last <code style="user-select: auto;">k</code> numbers in the current list. You can assume that always the current list has at least <code style="user-select: auto;">k</code> numbers.</li>
</ul>

<p style="user-select: auto;">The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

<strong style="user-select: auto;">Output</strong>
[null,null,null,null,null,null,20,40,0,null,32]

<strong style="user-select: auto;">Explanation</strong>
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= num &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 4 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">4 * 10<sup style="user-select: auto;">4</sup></code> calls will be made to <code style="user-select: auto;">add</code> and <code style="user-select: auto;">getProduct</code>.</li>
	<li style="user-select: auto;">The product of the stream at any point in time will fit in a <strong style="user-select: auto;">32-bit</strong> integer.</li>
</ul>
</div>