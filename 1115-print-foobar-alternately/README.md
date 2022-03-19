<h2><a href="https://leetcode.com/problems/print-foobar-alternately/">1115. Print FooBar Alternately</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Suppose you are given the following code:</p>

<pre style="user-select: auto;">class FooBar {
  public void foo() {
    for (int i = 0; i &lt; n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i &lt; n; i++) {
      print("bar");
    }
  }
}
</pre>

<p style="user-select: auto;">The same instance of <code style="user-select: auto;">FooBar</code> will be passed to two different threads:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">thread <code style="user-select: auto;">A</code> will call <code style="user-select: auto;">foo()</code>, while</li>
	<li style="user-select: auto;">thread <code style="user-select: auto;">B</code> will call <code style="user-select: auto;">bar()</code>.</li>
</ul>

<p style="user-select: auto;">Modify the given program to output <code style="user-select: auto;">"foobar"</code> <code style="user-select: auto;">n</code> times.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 1
<strong style="user-select: auto;">Output:</strong> "foobar"
<strong style="user-select: auto;">Explanation:</strong> There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 2
<strong style="user-select: auto;">Output:</strong> "foobarfoobar"
<strong style="user-select: auto;">Explanation:</strong> "foobar" is being output 2 times.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 1000</code></li>
</ul>
</div>