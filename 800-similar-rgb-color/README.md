<h2><a href="https://leetcode.com/problems/similar-rgb-color/">800. Similar RGB Color</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">The red-green-blue color <code style="user-select: auto;">"#AABBCC"</code> can be written as <code style="user-select: auto;">"#ABC"</code> in shorthand.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">"#15c"</code> is shorthand for the color <code style="user-select: auto;">"#1155cc"</code>.</li>
</ul>

<p style="user-select: auto;">The similarity between the two colors <code style="user-select: auto;">"#ABCDEF"</code> and <code style="user-select: auto;">"#UVWXYZ"</code> is <code style="user-select: auto;">-(AB - UV)<sup style="user-select: auto;">2</sup> - (CD - WX)<sup style="user-select: auto;">2</sup> - (EF - YZ)<sup style="user-select: auto;">2</sup></code>.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">color</code> that follows the format <code style="user-select: auto;">"#ABCDEF"</code>, return a string represents the color that is most similar to the given color and has a shorthand (i.e., it can be represented as some <code style="user-select: auto;">"#XYZ"</code>).</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Any answer</strong> which has the same highest similarity as the best answer will be accepted.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> color = "#09f166"
<strong style="user-select: auto;">Output:</strong> "#11ee66"
<strong style="user-select: auto;">Explanation:</strong> 
The similarity is -(0x09 - 0x11)<sup style="user-select: auto;">2</sup> -(0xf1 - 0xee)<sup style="user-select: auto;">2</sup> - (0x66 - 0x66)<sup style="user-select: auto;">2</sup> = -64 -9 -0 = -73.
This is the highest among any shorthand color.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> color = "#4e3fe1"
<strong style="user-select: auto;">Output:</strong> "#5544dd"
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">color.length == 7</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">color[0] == '#'</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">color[i]</code> is either digit or character in the range <code style="user-select: auto;">['a', 'f']</code> for <code style="user-select: auto;">i &gt; 0</code>.</li>
</ul>
</div>