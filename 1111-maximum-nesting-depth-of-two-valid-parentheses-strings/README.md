<h2><a href="https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/">1111. Maximum Nesting Depth of Two Valid Parentheses Strings</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A string is a <em style="user-select: auto;">valid parentheses string</em>&nbsp;(denoted VPS) if and only if it consists of <code style="user-select: auto;">"("</code> and <code style="user-select: auto;">")"</code> characters only, and:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">It is the empty string, or</li>
	<li style="user-select: auto;">It can be written as&nbsp;<code style="user-select: auto;">AB</code>&nbsp;(<code style="user-select: auto;">A</code>&nbsp;concatenated with&nbsp;<code style="user-select: auto;">B</code>), where&nbsp;<code style="user-select: auto;">A</code>&nbsp;and&nbsp;<code style="user-select: auto;">B</code>&nbsp;are VPS's, or</li>
	<li style="user-select: auto;">It can be written as&nbsp;<code style="user-select: auto;">(A)</code>, where&nbsp;<code style="user-select: auto;">A</code>&nbsp;is a VPS.</li>
</ul>

<p style="user-select: auto;">We can&nbsp;similarly define the <em style="user-select: auto;">nesting depth</em> <code style="user-select: auto;">depth(S)</code> of any VPS <code style="user-select: auto;">S</code> as follows:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">depth("") = 0</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">depth(A + B) = max(depth(A), depth(B))</code>, where <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code> are VPS's</li>
	<li style="user-select: auto;"><code style="user-select: auto;">depth("(" + A + ")") = 1 + depth(A)</code>, where <code style="user-select: auto;">A</code> is a VPS.</li>
</ul>

<p style="user-select: auto;">For example,&nbsp; <code style="user-select: auto;">""</code>,&nbsp;<code style="user-select: auto;">"()()"</code>, and&nbsp;<code style="user-select: auto;">"()(()())"</code>&nbsp;are VPS's (with nesting depths 0, 1, and 2), and <code style="user-select: auto;">")("</code> and <code style="user-select: auto;">"(()"</code> are not VPS's.</p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;">Given a VPS <font face="monospace" style="user-select: auto;">seq</font>, split it into two disjoint subsequences <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code>, such that&nbsp;<code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code> are VPS's (and&nbsp;<code style="user-select: auto;">A.length + B.length = seq.length</code>).</p>

<p style="user-select: auto;">Now choose <strong style="user-select: auto;">any</strong> such <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code> such that&nbsp;<code style="user-select: auto;">max(depth(A), depth(B))</code> is the minimum possible value.</p>

<p style="user-select: auto;">Return an <code style="user-select: auto;">answer</code> array (of length <code style="user-select: auto;">seq.length</code>) that encodes such a&nbsp;choice of <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code>:&nbsp; <code style="user-select: auto;">answer[i] = 0</code> if <code style="user-select: auto;">seq[i]</code> is part of <code style="user-select: auto;">A</code>, else <code style="user-select: auto;">answer[i] = 1</code>.&nbsp; Note that even though multiple answers may exist, you may return any of them.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> seq = "(()())"
<strong style="user-select: auto;">Output:</strong> [0,1,1,1,1,0]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> seq = "()(())()"
<strong style="user-select: auto;">Output:</strong> [0,0,0,1,1,0,1,1]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= seq.size &lt;= 10000</code></li>
</ul>
</div>