<h2><a href="https://leetcode.com/problems/basic-calculator-iii/">772. Basic Calculator III</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Implement a basic calculator to evaluate a simple expression string.</p>

<p style="user-select: auto;">The expression string contains only non-negative integers, <code style="user-select: auto;">'+'</code>, <code style="user-select: auto;">'-'</code>, <code style="user-select: auto;">'*'</code>, <code style="user-select: auto;">'/'</code> operators, and open <code style="user-select: auto;">'('</code> and closing parentheses <code style="user-select: auto;">')'</code>. The integer division should <strong style="user-select: auto;">truncate toward zero</strong>.</p>

<p style="user-select: auto;">You may assume that the given expression is always valid. All intermediate results will be in the range of <code style="user-select: auto;">[-2<sup style="user-select: auto;">31</sup>, 2<sup style="user-select: auto;">31</sup> - 1]</code>.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Note:</strong> You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code style="user-select: auto;">eval()</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "1+1"
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "6-4/2"
<strong style="user-select: auto;">Output:</strong> 4
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "2*(5+5*2)/3+(6/2+8)"
<strong style="user-select: auto;">Output:</strong> 21
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of digits, <code style="user-select: auto;">'+'</code>, <code style="user-select: auto;">'-'</code>, <code style="user-select: auto;">'*'</code>, <code style="user-select: auto;">'/'</code>, <code style="user-select: auto;">'('</code>,&nbsp;and&nbsp;<code style="user-select: auto;">')'</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> is a <strong style="user-select: auto;">valid</strong> expression.</li>
</ul>
</div>