<h2><a href="https://leetcode.com/problems/truncate-sentence/">1816. Truncate Sentence</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;">sentence</strong> is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of <strong style="user-select: auto;">only</strong> uppercase and lowercase English letters (no punctuation).</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">"Hello World"</code>, <code style="user-select: auto;">"HELLO"</code>, and <code style="user-select: auto;">"hello world hello world"</code> are all sentences.</li>
</ul>

<p style="user-select: auto;">You are given a sentence <code style="user-select: auto;">s</code>​​​​​​ and an integer <code style="user-select: auto;">k</code>​​​​​​. You want to <strong style="user-select: auto;">truncate</strong> <code style="user-select: auto;">s</code>​​​​​​ such that it contains only the <strong style="user-select: auto;">first</strong> <code style="user-select: auto;">k</code>​​​​​​ words. Return <code style="user-select: auto;">s</code>​​​​<em style="user-select: auto;">​​ after <strong style="user-select: auto;">truncating</strong> it.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "Hello how are you Contestant", k = 4
<strong style="user-select: auto;">Output:</strong> "Hello how are you"
<strong style="user-select: auto;">Explanation:</strong>
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "What is the solution to this problem", k = 4
<strong style="user-select: auto;">Output:</strong> "What is the solution"
<strong style="user-select: auto;">Explanation:</strong>
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "chopper is not a tanuki", k = 5
<strong style="user-select: auto;">Output:</strong> "chopper is not a tanuki"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">k</code> is in the range <code style="user-select: auto;">[1, the number of words in s]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consist of only lowercase and uppercase English letters and spaces.</li>
	<li style="user-select: auto;">The words in <code style="user-select: auto;">s</code> are separated by a single space.</li>
	<li style="user-select: auto;">There are no leading or trailing spaces.</li>
</ul>
</div>