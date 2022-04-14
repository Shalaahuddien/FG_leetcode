<h2><a href="https://leetcode.com/problems/construct-quad-tree/">427. Construct Quad Tree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <code style="user-select: auto;">n * n</code> matrix <code style="user-select: auto;">grid</code> of <code style="user-select: auto;">0's</code> and <code style="user-select: auto;">1's</code> only. We want to represent the <code style="user-select: auto;">grid</code> with a Quad-Tree.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the root of the Quad-Tree</em> representing the <code style="user-select: auto;">grid</code>.</p>

<p style="user-select: auto;">Notice that you can assign the value of a node to <strong style="user-select: auto;">True</strong> or <strong style="user-select: auto;">False</strong> when <code style="user-select: auto;">isLeaf</code> is <strong style="user-select: auto;">False</strong>, and both are <strong style="user-select: auto;">accepted</strong> in the answer.</p>

<p style="user-select: auto;">A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">val</code>: True if the node represents a grid of 1's or False if the node represents a grid of 0's.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">isLeaf</code>: True if the node is leaf node on the tree or False if the node has the four children.</li>
</ul>

<pre style="user-select: auto;">class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}</pre>

<p style="user-select: auto;"><lighter data-id="lgt9372863991172615" data-unique-lighter-id="2" style="background-color: rgb(255, 255, 131); user-select: auto;">We can construct a Quad-Tree from a two-dimensional area using the </lighter><div class="liner-thread-icon FIRST owner HIDE" data-id="254300641" data-unique-lighter-id="2" id="lgt254300641" style="display: block; user-select: auto;">
              <img class="liner-thread-bubble" data-id="254300641" src="https://gcpstorage.getliner.com/liner-service-bucket/user_photo/4614321-4d0d20a3-64f4-4d26-93d9-ea1a56d23457.svg+xml" style="user-select: auto;">
          </div><lighter data-id="lgt9280942060649284" data-unique-lighter-id="1" style="background-color: rgb(255, 255, 131); user-select: auto;"><lighter data-id="lgt9372863991172615" data-unique-lighter-id="2" style="background-color: rgb(255, 255, 131); user-select: auto;">following steps:</lighter></lighter><div class="liner-thread-icon FIRST owner HIDE" data-id="254300635" data-unique-lighter-id="1" id="lgt254300635" style="display: block; user-select: auto;">
              <img class="liner-thread-bubble" data-id="254300635" src="https://gcpstorage.getliner.com/liner-service-bucket/user_photo/4614321-4d0d20a3-64f4-4d26-93d9-ea1a56d23457.svg+xml" style="user-select: auto;">
          </div></p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">If the current grid has the same value (i.e all <code style="user-select: auto;">1's</code> or all <code style="user-select: auto;">0's</code>) set <code style="user-select: auto;">isLeaf</code> True and set <code style="user-select: auto;">val</code> to the value of the grid and set the four children to Null and stop.</li>
	<li style="user-select: auto;">If the current grid has different values, set <code style="user-select: auto;">isLeaf</code> to False and set <code style="user-select: auto;">val</code> to any value and divide the current grid into four sub-grids as shown in the photo.</li>
	<li style="user-select: auto;">Recurse for each of the children with the proper sub-grid.</li>
</ol>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" style="width: 777px; height: 181px; user-select: auto;" title="">
<p style="user-select: auto;">If you want to know more about the Quad-Tree, you can refer to the <a href="https://en.wikipedia.org/wiki/Quadtree" style="user-select: auto;">wiki</a>.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Quad-Tree format:</strong></p>

<p style="user-select: auto;">The output represents the serialized format of a Quad-Tree using <lighter data-id="lgt5792250140466602" data-unique-lighter-id="3" style="background-color: rgb(255, 255, 131); user-select: auto;">level order traversal,</lighter><div class="liner-thread-icon FIRST owner HIDE" data-id="254300658" data-unique-lighter-id="3" id="lgt254300658" style="display: block; user-select: auto;">
              <img class="liner-thread-bubble" data-id="254300658" src="https://gcpstorage.getliner.com/liner-service-bucket/user_photo/4614321-4d0d20a3-64f4-4d26-93d9-ea1a56d23457.svg+xml" style="user-select: auto;">
          </div> where <code style="user-select: auto;">null</code> signifies a path terminator where no node exists below.</p>

<p style="user-select: auto;">It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list <code style="user-select: auto;">[isLeaf, val]</code>.</p>

<p style="user-select: auto;">If the value of <code style="user-select: auto;">isLeaf</code> or <code style="user-select: auto;">val</code> is True we represent it as <strong style="user-select: auto;">1</strong> in the list <code style="user-select: auto;">[isLeaf, val]</code> and if the value of <code style="user-select: auto;">isLeaf</code> or <code style="user-select: auto;">val</code> is False we represent it as <strong style="user-select: auto;">0</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/grid1.png" style="width: 777px; height: 99px; user-select: auto;" title="">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[0,1],[1,0]]
<strong style="user-select: auto;">Output:</strong> [[0,1],[1,0],[1,1],[1,1],[1,0]]
<strong style="user-select: auto;">Explanation:</strong> The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e1tree.png" style="width: 777px; height: 186px; user-select: auto;">
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2mat.png" style="width: 777px; height: 343px; user-select: auto;" title=""></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
<strong style="user-select: auto;">Output:</strong> [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
<strong style="user-select: auto;">Explanation:</strong> All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2tree.png" style="width: 777px; height: 328px; user-select: auto;" title="">
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == grid.length == grid[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == 2<sup style="user-select: auto;">x</sup></code> where <code style="user-select: auto;">0 &lt;= x &lt;= 6</code></li>
</ul>
</div>