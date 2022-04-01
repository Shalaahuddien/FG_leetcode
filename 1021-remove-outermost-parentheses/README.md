<h2><a href="https://leetcode.com/problems/remove-outermost-parentheses/">1021. Remove Outermost Parentheses</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A valid parentheses string is either empty <code style="user-select: auto;">""</code>, <code style="user-select: auto;">"(" + A + ")"</code>, or <code style="user-select: auto;">A + B</code>, where <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code> are valid parentheses strings, and <code style="user-select: auto;">+</code> represents string concatenation.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">""</code>, <code style="user-select: auto;">"()"</code>, <code style="user-select: auto;">"(())()"</code>, and <code style="user-select: auto;">"(()(()))"</code> are all valid parentheses strings.</li>
</ul>

<p style="user-select: auto;">A valid parentheses string <code style="user-select: auto;">s</code> is primitive if it is nonempty, and there does not exist a way to split it into <code style="user-select: auto;">s = A + B</code>, with <code style="user-select: auto;">A</code> and <code style="user-select: auto;">B</code> nonempty valid parentheses strings.</p>

<p style="user-select: auto;">Given a valid parentheses string <code style="user-select: auto;">s</code>, consider its primitive decomposition: <code style="user-select: auto;">s = P<sub style="user-select: auto;">1</sub> + P<sub style="user-select: auto;">2</sub> + ... + P<sub style="user-select: auto;">k</sub></code>, where <code style="user-select: auto;">P<sub style="user-select: auto;">i</sub></code> are primitive valid parentheses strings.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">s</code> <em style="user-select: auto;">after removing the outermost parentheses of every primitive string in the primitive decomposition of </em><code style="user-select: auto;">s</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "(()())(())"
<strong style="user-select: auto;">Output:</strong> "()()()"
<strong style="user-select: auto;">Explanation:</strong> 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "(()())(())(()(()))"
<strong style="user-select: auto;">Output:</strong> "()()()()(())"
<strong style="user-select: auto;">Explanation:</strong> 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "()()"
<strong style="user-select: auto;">Output:</strong> ""
<strong style="user-select: auto;">Explanation:</strong> 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s[i]</code> is either <code style="user-select: auto;">'('</code> or <code style="user-select: auto;">')'</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> is a valid parentheses string.</li>
</ul>
</div>