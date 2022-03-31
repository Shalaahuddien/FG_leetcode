<h2><a href="https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/">1807. Evaluate the Bracket Pairs of a String</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">s</code> that contains some bracket pairs, with each pair containing a <strong style="user-select: auto;">non-empty</strong> key.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, in the string <code style="user-select: auto;">"(name)is(age)yearsold"</code>, there are <strong style="user-select: auto;">two</strong> bracket pairs that contain the keys <code style="user-select: auto;">"name"</code> and <code style="user-select: auto;">"age"</code>.</li>
</ul>

<p style="user-select: auto;">You know the values of a wide range of keys. This is represented by a 2D string array <code style="user-select: auto;">knowledge</code> where each <code style="user-select: auto;">knowledge[i] = [key<sub style="user-select: auto;">i</sub>, value<sub style="user-select: auto;">i</sub>]</code> indicates that key <code style="user-select: auto;">key<sub style="user-select: auto;">i</sub></code> has a value of <code style="user-select: auto;">value<sub style="user-select: auto;">i</sub></code>.</p>

<p style="user-select: auto;">You are tasked to evaluate <strong style="user-select: auto;">all</strong> of the bracket pairs. When you evaluate a bracket pair that contains some key <code style="user-select: auto;">key<sub style="user-select: auto;">i</sub></code>, you will:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Replace <code style="user-select: auto;">key<sub style="user-select: auto;">i</sub></code> and the bracket pair with the key's corresponding <code style="user-select: auto;">value<sub style="user-select: auto;">i</sub></code>.</li>
	<li style="user-select: auto;">If you do not know the value of the key, you will replace <code style="user-select: auto;">key<sub style="user-select: auto;">i</sub></code> and the bracket pair with a question mark <code style="user-select: auto;">"?"</code> (without the quotation marks).</li>
</ul>

<p style="user-select: auto;">Each key will appear at most once in your <code style="user-select: auto;">knowledge</code>. There will not be any nested brackets in <code style="user-select: auto;">s</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the resulting string after evaluating <strong style="user-select: auto;">all</strong> of the bracket pairs.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
<strong style="user-select: auto;">Output:</strong> "bobistwoyearsold"
<strong style="user-select: auto;">Explanation:</strong>
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "hi(name)", knowledge = [["a","b"]]
<strong style="user-select: auto;">Output:</strong> "hi?"
<strong style="user-select: auto;">Explanation:</strong> As you do not know the value of the key "name", replace "(name)" with "?".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
<strong style="user-select: auto;">Output:</strong> "yesyesyesaaa"
<strong style="user-select: auto;">Explanation:</strong> The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= knowledge.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">knowledge[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= key<sub style="user-select: auto;">i</sub>.length, value<sub style="user-select: auto;">i</sub>.length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of lowercase English letters and round brackets <code style="user-select: auto;">'('</code> and <code style="user-select: auto;">')'</code>.</li>
	<li style="user-select: auto;">Every open bracket <code style="user-select: auto;">'('</code> in <code style="user-select: auto;">s</code> will have a corresponding close bracket <code style="user-select: auto;">')'</code>.</li>
	<li style="user-select: auto;">The key in each bracket pair of <code style="user-select: auto;">s</code> will be non-empty.</li>
	<li style="user-select: auto;">There will not be any nested bracket pairs in <code style="user-select: auto;">s</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">key<sub style="user-select: auto;">i</sub></code> and <code style="user-select: auto;">value<sub style="user-select: auto;">i</sub></code> consist of lowercase English letters.</li>
	<li style="user-select: auto;">Each <code style="user-select: auto;">key<sub style="user-select: auto;">i</sub></code> in <code style="user-select: auto;">knowledge</code> is unique.</li>
</ul>
</div>