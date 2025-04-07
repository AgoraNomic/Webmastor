---
layout: puremd
---
<script src="http://cdn.rawgit.com/h2non/jsHashes/master/hashes.js"></script>
<script src="https://unpkg.com/openpgp@6.1.0/dist/openpgp.min.js"></script>
<script>
  async function handleHash() {
    const salt = document.getElementById("hash-salt").value;
    const plaintext = document.getElementById("hash-plaintext").value;
    const salted_plaintext = (salt.trim() + "\n" + plaintext.trim()).trim();
    const hashedMessage = new Hashes.SHA256().b64(salted_plaintext);
    const output = document.getElementById("hash-output");
    output.textContent = hashedMessage;
  }
  async function handleEncrypt() {
    const password = document.getElementById("cry-password").value;
    const plaintext = document.getElementById("cry-plaintext").value;
    const message = await openpgp.createMessage({ text: plaintext.trim() });
    const encryptedMessage = await openpgp.encrypt({
      message,
      passwords: [password],
    });
    const output = document.getElementById("cry-ciphertext");
    output.value = encryptedMessage;
  }
  async function handleDecrypt() {
    const password = document.getElementById("cry-password").value;
    const ciphertext = document.getElementById("cry-ciphertext").value;
    const message = await openpgp.readMessage({ armoredMessage: ciphertext.trim() });
    const decryptedMessage = await openpgp.decrypt({
      message,
      passwords: [password],
    });
    const output = document.getElementById("cry-plaintext");
    output.value = decryptedMessage;
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

## Password-Encrypted Cipher

This tool will encrypt a plaintext with a password, or decrypt from a password. The algorithm used is AES-256.
 _Don't forget to specify the algorithm used so others can easily verify!_

<label for="cry-password">Password:</label>
<input type="text" id="cry-password" name="cry-password" />

<textarea id="cry-plaintext" name="cry-plaintext" rows="6" cols="40">
  I register.
</textarea>
<textarea id="cry-ciphertext" name="cry-ciphertext" rows="6" cols="40">
</textarea>

<input type="button" value="Encrypt" onclick="handleEncrypt();">
<input type="button" value="Decrypt" onclick="handleDecrypt();">


## Implementation Notes

This page runs entirely in your browser (hence why browser support is required) and does not make network requests beyond fetching the following dependencies:

- Hashing uses [jshashes](<https://www.npmjs.com/package/jshashes>).
- Password encryption uses [OpenPGPjs](<https://openpgpjs.org>).

The source code for this page is available in the [Webmastor's GitHub repository](<https://github.com/AgoraNomic/Webmastor/blob/gh-pages/gadgets.md?plain=1>).
