<h2><a href="https://leetcode.com/problems/robot-room-cleaner/">489. Robot Room Cleaner</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are controlling a robot that is located somewhere in a room. The room is modeled as an <code style="user-select: auto;">m x n</code> binary grid where <code style="user-select: auto;">0</code> represents a wall and <code style="user-select: auto;">1</code> represents an empty slot.</p>

<p style="user-select: auto;">The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API <code style="user-select: auto;">Robot</code>.</p>

<p style="user-select: auto;">You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is <code style="user-select: auto;">90</code> degrees.</p>

<p style="user-select: auto;">When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.</p>

<p style="user-select: auto;">Design an algorithm to clean the entire room using the following APIs:</p>

<pre style="user-select: auto;">interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Note</strong> that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.</p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Custom testing:</strong></p>

<p style="user-select: auto;">The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/17/lc-grid.jpg" style="width: 500px; height: 314px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
<strong style="user-select: auto;">Output:</strong> Robot cleaned all rooms.
<strong style="user-select: auto;">Explanation:</strong> All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> room = [[1]], row = 0, col = 0
<strong style="user-select: auto;">Output:</strong> Robot cleaned all rooms.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == room.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == room[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">room[i][j]</code> is either <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= row &lt;&nbsp;m</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= col &lt; n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">room[row][col] == 1</code></li>
	<li style="user-select: auto;">All the empty cells can be visited from the starting position.</li>
</ul>
</div>