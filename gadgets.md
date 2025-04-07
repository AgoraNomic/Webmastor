---
layout: puremd
---
<script src="http://cdn.rawgit.com/h2non/jsHashes/master/hashes.js"></script>
<script>
  async function handleHash() {
    const salt = document.getElementById("hash-salt").value;
    const plaintext = document.getElementById("hash-plaintext").value;
    const salted_plaintext = (salt.trim() + "\n" + plaintext.trim()).trim();
    const hashedMessage = new Hashes.SHA256().b64(salted_plaintext);
    const output = document.getElementById("hash-output");
    output.textContent = hashedMessage;
  }
</script>

# Webmastor's Gadgets

This page provides gadgets for hashing and password-based encryption.

This may not work in all browsers. Make sure yours is up-to-date!

## Which one should I use?

- A hashed text is useful when you want your confirmation to be "This is the original text/salt."
  - A salted hash is usually suitable as a Fingerprint. An unsalted hash is not recommended.
- An encrypted text is useful when you want your confirmation to be "Here is a password
to see the original text."
  - These are likely not suitable useful for most Fingerprints.
  - These may be useful when you want to publicly commit to a value and simultaneously share that value with a person, since it requires them to validate your public commitment to retrieve the content. (A hash could be skipped over by an individual assuming good faith.)

## Salted Hash

This tool will generate a (optionally salted) hash. The algorithm is SHA-256.
 _Don't forget to specify the algorithm used so others can easily verify!_

<label for="hash-salt">Salt:</label>
<input type="text" id="hash-salt" name="hash-salt" />

<textarea id="hash-plaintext" name="hash-plaintext" rows="6" cols="40">
  I register.
</textarea>
<textarea id="hash-output" name="hash-output" rows="6" cols="40" readonly>
</textarea>

<input type="button" value="Hash" onclick="handleHash();">


(The final input is just "salt + newline + plaintext".)


## Implementation Notes

This page runs entirely in your browser (hence why browser support is required) and does not make network requests beyond fetching the following dependencies:

- Hashing uses [jshashes](<https://www.npmjs.com/package/jshashes>).

The source code for this page is available in the [Webmastor's GitHub repository](<https://github.com/AgoraNomic/Webmastor/blob/gh-pages/gadgets.md?plain=1>).
