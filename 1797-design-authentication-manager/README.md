<h2><a href="https://leetcode.com/problems/design-authentication-manager/">1797. Design Authentication Manager</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire <code style="user-select: auto;">timeToLive</code> seconds after the <code style="user-select: auto;">currentTime</code>. If the token is renewed, the expiry time will be <b style="user-select: auto;">extended</b> to expire <code style="user-select: auto;">timeToLive</code> seconds after the (potentially different) <code style="user-select: auto;">currentTime</code>.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">AuthenticationManager</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">AuthenticationManager(int timeToLive)</code> constructs the <code style="user-select: auto;">AuthenticationManager</code> and sets the <code style="user-select: auto;">timeToLive</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">generate(string tokenId, int currentTime)</code> generates a new token with the given <code style="user-select: auto;">tokenId</code> at the given <code style="user-select: auto;">currentTime</code> in seconds.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">renew(string tokenId, int currentTime)</code> renews the <strong style="user-select: auto;">unexpired</strong> token with the given <code style="user-select: auto;">tokenId</code> at the given <code style="user-select: auto;">currentTime</code> in seconds. If there are no unexpired tokens with the given <code style="user-select: auto;">tokenId</code>, the request is ignored, and nothing happens.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">countUnexpiredTokens(int currentTime)</code> returns the number of <strong style="user-select: auto;">unexpired</strong> tokens at the given currentTime.</li>
</ul>

<p style="user-select: auto;">Note that if a token expires at time <code style="user-select: auto;">t</code>, and another action happens on time <code style="user-select: auto;">t</code> (<code style="user-select: auto;">renew</code> or <code style="user-select: auto;">countUnexpiredTokens</code>), the expiration takes place <strong style="user-select: auto;">before</strong> the other actions.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/copy-of-pc68_q2.png" style="width: 500px; height: 287px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["AuthenticationManager", "<code style="user-select: auto;">renew</code>", "generate", "<code style="user-select: auto;">countUnexpiredTokens</code>", "generate", "<code style="user-select: auto;">renew</code>", "<code style="user-select: auto;">renew</code>", "<code style="user-select: auto;">countUnexpiredTokens</code>"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
<strong style="user-select: auto;">Output</strong>
[null, null, null, 1, null, null, null, 0]

<strong style="user-select: auto;">Explanation</strong>
AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with <code style="user-select: auto;">timeToLive</code> = 5 seconds.
authenticationManager.<code style="user-select: auto;">renew</code>("aaa", 1); // No token exists with tokenId "aaa" at time 1, so nothing happens.
authenticationManager.generate("aaa", 2); // Generates a new token with tokenId "aaa" at time 2.
authenticationManager.<code style="user-select: auto;">countUnexpiredTokens</code>(6); // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
authenticationManager.generate("bbb", 7); // Generates a new token with tokenId "bbb" at time 7.
authenticationManager.<code style="user-select: auto;">renew</code>("aaa", 8); // The token with tokenId "aaa" expired at time 7, and 8 &gt;= 7, so at time 8 the <code style="user-select: auto;">renew</code> request is ignored, and nothing happens.
authenticationManager.<code style="user-select: auto;">renew</code>("bbb", 10); // The token with tokenId "bbb" is unexpired at time 10, so the <code style="user-select: auto;">renew</code> request is fulfilled and now the token will expire at time 15.
authenticationManager.<code style="user-select: auto;">countUnexpiredTokens</code>(15); // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= timeToLive &lt;= 10<sup style="user-select: auto;">8</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= currentTime &lt;= 10<sup style="user-select: auto;">8</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= tokenId.length &lt;= 5</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">tokenId</code> consists only of lowercase letters.</li>
	<li style="user-select: auto;">All calls to <code style="user-select: auto;">generate</code> will contain unique values of <code style="user-select: auto;">tokenId</code>.</li>
	<li style="user-select: auto;">The values of <code style="user-select: auto;">currentTime</code> across all the function calls will be <strong style="user-select: auto;">strictly increasing</strong>.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">2000</code> calls will be made to all functions combined.</li>
</ul>
</div>