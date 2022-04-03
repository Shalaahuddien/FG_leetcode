<h2><a href="https://leetcode.com/problems/encrypt-and-decrypt-strings/">2227. Encrypt and Decrypt Strings</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a character array <code style="user-select: auto;">keys</code> containing <strong style="user-select: auto;">unique</strong> characters and a string array <code style="user-select: auto;">values</code> containing strings of length 2. You are also given another string array <code style="user-select: auto;">dictionary</code> that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a <strong style="user-select: auto;">0-indexed</strong> string.</p>

<p style="user-select: auto;">A string is <strong style="user-select: auto;">encrypted</strong> with the following process:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">For each character <code style="user-select: auto;">c</code> in the string, we find the index <code style="user-select: auto;">i</code> satisfying <code style="user-select: auto;">keys[i] == c</code> in <code style="user-select: auto;">keys</code>.</li>
	<li style="user-select: auto;">Replace <code style="user-select: auto;">c</code> with <code style="user-select: auto;">values[i]</code> in the string.</li>
</ol>

<p style="user-select: auto;">A string is <strong style="user-select: auto;">decrypted</strong> with the following process:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">For each substring <code style="user-select: auto;">s</code> of length 2 occurring at an even index in the string, we find an <code style="user-select: auto;">i</code> such that <code style="user-select: auto;">values[i] == s</code>. If there are multiple valid <code style="user-select: auto;">i</code>, we choose <strong style="user-select: auto;">any</strong> one of them. This means a string could have multiple possible strings it can decrypt to.</li>
	<li style="user-select: auto;">Replace <code style="user-select: auto;">s</code> with <code style="user-select: auto;">keys[i]</code> in the string.</li>
</ol>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">Encrypter</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">Encrypter(char[] keys, String[] values, String[] dictionary)</code> Initializes the <code style="user-select: auto;">Encrypter</code> class with <code style="user-select: auto;">keys, values</code>, and <code style="user-select: auto;">dictionary</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">String encrypt(String word1)</code> Encrypts <code style="user-select: auto;">word1</code> with the encryption process described above and returns the encrypted string.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int decrypt(String word2)</code> Returns the number of possible strings <code style="user-select: auto;">word2</code> could decrypt to that also appear in <code style="user-select: auto;">dictionary</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
<strong style="user-select: auto;">Output</strong>
[null, "eizfeiam", 2]

<strong style="user-select: auto;">Explanation</strong>
Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // return "eizfeiam". 
&nbsp;                          // 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
encrypter.decrypt("eizfeiam"); // return 2. 
                              // "ei" can map to 'a' or 'c', "zf" maps to 'b', and "am" maps to 'd'. 
                              // Thus, the possible strings after decryption are "abad", "cbad", "abcd", and "cbcd". 
                              // 2 of those strings, "abad" and "abcd", appear in dictionary, so the answer is 2.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= keys.length == values.length &lt;= 26</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">values[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= dictionary.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li style="user-select: auto;">All <code style="user-select: auto;">keys[i]</code> and <code style="user-select: auto;">dictionary[i]</code> are <strong style="user-select: auto;">unique</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word1.length &lt;= 2000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word2.length &lt;= 200</code></li>
	<li style="user-select: auto;">All <code style="user-select: auto;">word1[i]</code> appear in <code style="user-select: auto;">keys</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">word2.length</code> is even.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">keys</code>, <code style="user-select: auto;">values[i]</code>, <code style="user-select: auto;">dictionary[i]</code>, <code style="user-select: auto;">word1</code>, and <code style="user-select: auto;">word2</code> only contain lowercase English letters.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">200</code> calls will be made to <code style="user-select: auto;">encrypt</code> and <code style="user-select: auto;">decrypt</code> <strong style="user-select: auto;">in total</strong>.</li>
</ul>
</div>