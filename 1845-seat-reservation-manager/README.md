<h2><a href="https://leetcode.com/problems/seat-reservation-manager/">1845. Seat Reservation Manager</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design a system that manages the reservation state of <code style="user-select: auto;">n</code> seats that are numbered from <code style="user-select: auto;">1</code> to <code style="user-select: auto;">n</code>.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">SeatManager</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">SeatManager(int n)</code> Initializes a <code style="user-select: auto;">SeatManager</code> object that will manage <code style="user-select: auto;">n</code> seats numbered from <code style="user-select: auto;">1</code> to <code style="user-select: auto;">n</code>. All seats are initially available.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int reserve()</code> Fetches the <strong style="user-select: auto;">smallest-numbered</strong> unreserved seat, reserves it, and returns its number.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void unreserve(int seatNumber)</code> Unreserves the seat with the given <code style="user-select: auto;">seatNumber</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
<strong style="user-select: auto;">Output</strong>
[null, 1, 2, null, 2, 3, 4, 5, null]

<strong style="user-select: auto;">Explanation</strong>
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= seatNumber &lt;= n</code></li>
	<li style="user-select: auto;">For each call to <code style="user-select: auto;">reserve</code>, it is guaranteed that there will be at least one unreserved seat.</li>
	<li style="user-select: auto;">For each call to <code style="user-select: auto;">unreserve</code>, it is guaranteed that <code style="user-select: auto;">seatNumber</code> will be reserved.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">10<sup style="user-select: auto;">5</sup></code> calls <strong style="user-select: auto;">in total</strong> will be made to <code style="user-select: auto;">reserve</code> and <code style="user-select: auto;">unreserve</code>.</li>
</ul>
</div>