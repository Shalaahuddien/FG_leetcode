<h2><a href="https://leetcode.com/problems/solve-the-equation/">640. Solve the Equation</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Solve a given equation and return the value of <code style="user-select: auto;">'x'</code> in the form of a string <code style="user-select: auto;">"x=#value"</code>. The equation contains only <code style="user-select: auto;">'+'</code>, <code style="user-select: auto;">'-'</code> operation, the variable <code style="user-select: auto;">'x'</code> and its coefficient. You should return <code style="user-select: auto;">"No solution"</code> if there is no solution for the equation, or <code style="user-select: auto;">"Infinite solutions"</code> if there are infinite solutions for the equation.</p>

<p style="user-select: auto;">If there is exactly one solution for the equation, we ensure that the value of <code style="user-select: auto;">'x'</code> is an integer.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> equation = "x+5-3+x=6+x-2"
<strong style="user-select: auto;">Output:</strong> "x=2"
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> equation = "x=x"
<strong style="user-select: auto;">Output:</strong> "Infinite solutions"
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> equation = "2x=x"
<strong style="user-select: auto;">Output:</strong> "x=0"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">3 &lt;= equation.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">equation</code> has exactly one <code style="user-select: auto;">'='</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">equation</code> consists of integers with an absolute value in the range <code style="user-select: auto;">[0, 100]</code> without any leading zeros, and the variable <code style="user-select: auto;">'x'</code>.</li>
</ul>
</div>