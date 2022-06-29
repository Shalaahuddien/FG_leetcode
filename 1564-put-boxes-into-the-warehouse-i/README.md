<h2><a href="https://leetcode.com/problems/put-boxes-into-the-warehouse-i/">1564. Put Boxes Into the Warehouse I</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given two arrays of positive integers, <code style="user-select: auto;">boxes</code> and <code style="user-select: auto;">warehouse</code>, representing the heights of some boxes of unit width and the heights of <code style="user-select: auto;">n</code> rooms in a warehouse respectively. The warehouse's rooms are labelled from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">n - 1</code> from left to right where <code style="user-select: auto;">warehouse[i]</code> (0-indexed) is the height of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> room.</p>

<p style="user-select: auto;">Boxes are put into the warehouse by the following rules:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Boxes cannot be stacked.</li>
	<li style="user-select: auto;">You can rearrange the insertion order of the boxes.</li>
	<li style="user-select: auto;">Boxes can only be pushed into the warehouse from left to right only.</li>
	<li style="user-select: auto;">If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the maximum number of boxes you can put into the warehouse.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/11.png" style="width: 400px; height: 242px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/12.png" style="width: 280px; height: 242px; user-select: auto;">
We can first put the box of height 1 in room 4. Then we can put the box of height 3 in either of the 3 rooms 1, 2, or 3. Lastly, we can put one box of height 4 in room 0.
There is no way we can fit all 4 boxes in the warehouse.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/21.png" style="width: 400px; height: 202px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/22.png" style="width: 280px; height: 202px; user-select: auto;">
Notice that it's not possible to put the box of height 4 into the warehouse since it cannot pass the first room of height 3.
Also, for the last two rooms, 2 and 3, only boxes of height 1 can fit.
We can fit 3 boxes maximum as shown above. The yellow box can also be put in room 2 instead.
Swapping the orange and green boxes is also valid, or swapping one of them with the red box.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> boxes = [1,2,3], warehouse = [1,2,3,4]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> Since the first room in the warehouse is of height 1, we can only put boxes of height 1.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == warehouse.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= boxes.length, warehouse.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= boxes[i], warehouse[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>