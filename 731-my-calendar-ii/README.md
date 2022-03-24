<h2><a href="https://leetcode.com/problems/my-calendar-ii/">731. My Calendar II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a <strong style="user-select: auto;">triple booking</strong>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">triple booking</strong> happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).</p>

<p style="user-select: auto;">The event can be represented as a pair of integers <code style="user-select: auto;">start</code> and <code style="user-select: auto;">end</code> that represents a booking on the half-open interval <code style="user-select: auto;">[start, end)</code>, the range of real numbers <code style="user-select: auto;">x</code> such that <code style="user-select: auto;">start &lt;= x &lt; end</code>.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">MyCalendarTwo</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">MyCalendarTwo()</code> Initializes the calendar object.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean book(int start, int end)</code> Returns <code style="user-select: auto;">true</code> if the event can be added to the calendar successfully without causing a <strong style="user-select: auto;">triple booking</strong>. Otherwise, return <code style="user-select: auto;">false</code> and do not add the event to the calendar.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong style="user-select: auto;">Output</strong>
[null, true, true, true, false, true, true]

<strong style="user-select: auto;">Explanation</strong>
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= start &lt; end &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">1000</code> calls will be made to <code style="user-select: auto;">book</code>.</li>
</ul>
</div>