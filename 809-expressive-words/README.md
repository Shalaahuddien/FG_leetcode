<h2><a href="https://leetcode.com/problems/expressive-words/">809. Expressive Words</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Sometimes people repeat letters to represent extra feeling. For example:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">"hello" -&gt; "heeellooo"</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">"hi" -&gt; "hiiii"</code></li>
</ul>

<p style="user-select: auto;">In these strings like <code style="user-select: auto;">"heeellooo"</code>, we have groups of adjacent letters that are all the same: <code style="user-select: auto;">"h"</code>, <code style="user-select: auto;">"eee"</code>, <code style="user-select: auto;">"ll"</code>, <code style="user-select: auto;">"ooo"</code>.</p>

<p style="user-select: auto;">You are given a string <code style="user-select: auto;">s</code> and an array of query strings <code style="user-select: auto;">words</code>. A query word is <strong style="user-select: auto;">stretchy</strong> if it can be made to be equal to <code style="user-select: auto;">s</code> by any number of applications of the following extension operation: choose a group consisting of characters <code style="user-select: auto;">c</code>, and add some number of characters <code style="user-select: auto;">c</code> to the group so that the size of the group is <strong style="user-select: auto;">three or more</strong>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, starting with <code style="user-select: auto;">"hello"</code>, we could do an extension on the group <code style="user-select: auto;">"o"</code> to get <code style="user-select: auto;">"hellooo"</code>, but we cannot get <code style="user-select: auto;">"helloo"</code> since the group <code style="user-select: auto;">"oo"</code> has a size less than three. Also, we could do another extension like <code style="user-select: auto;">"ll" -&gt; "lllll"</code> to get <code style="user-select: auto;">"helllllooo"</code>. If <code style="user-select: auto;">s = "helllllooo"</code>, then the query word <code style="user-select: auto;">"hello"</code> would be <strong style="user-select: auto;">stretchy</strong> because of these two extension operations: <code style="user-select: auto;">query = "hello" -&gt; "hellooo" -&gt; "helllllooo" = s</code>.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the number of query strings that are <strong style="user-select: auto;">stretchy</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "heeellooo", words = ["hello", "hi", "helo"]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length, words.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words[i].length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">words[i]</code> consist of lowercase letters.</li>
</ul>
</div>