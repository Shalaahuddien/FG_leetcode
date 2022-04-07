<h2><a href="https://leetcode.com/problems/design-hit-counter/">362. Design Hit Counter</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design a hit counter which counts the number of hits received in the past <code style="user-select: auto;">5</code> minutes (i.e., the past <code style="user-select: auto;">300</code> seconds).</p>

<p style="user-select: auto;">Your system should accept a <code style="user-select: auto;">timestamp</code> parameter (<strong style="user-select: auto;">in seconds</strong> granularity), and you may assume that calls are being made to the system in chronological order (i.e., <code style="user-select: auto;">timestamp</code> is monotonically increasing). Several hits may arrive roughly at the same time.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">HitCounter</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">HitCounter()</code> Initializes the object of the hit counter system.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void hit(int timestamp)</code> Records a hit that happened at <code style="user-select: auto;">timestamp</code> (<strong style="user-select: auto;">in seconds</strong>). Several hits may happen at the same <code style="user-select: auto;">timestamp</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int getHits(int timestamp)</code> Returns the number of hits in the past 5 minutes from <code style="user-select: auto;">timestamp</code> (i.e., the past <code style="user-select: auto;">300</code> seconds).</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
<strong style="user-select: auto;">Output</strong>
[null, null, null, null, 3, null, 4, 3]

<strong style="user-select: auto;">Explanation</strong>
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= timestamp &lt;= 2 * 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;">All the calls are being made to the system in chronological order (i.e., <code style="user-select: auto;">timestamp</code> is monotonically increasing).</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">300</code> calls will be made to <code style="user-select: auto;">hit</code> and <code style="user-select: auto;">getHits</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> What if the number of hits per second could be huge? Does your design scale?</p>
</div>