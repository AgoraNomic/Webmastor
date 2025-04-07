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

- A hashed text is useful when you want your confirmation to be "This is the original text (and salt)." A salted hash is usually suitable as a Fingerprint.
- An encrypted text is useful when you want your confirmation to be "Here is a password
to see the original text." These are likely not useful for a Fingerprint. It may be useful when you want to publicly commit to some value while privately sharing what that value is, as it requires the other party to use your publicly-committed value to determine the contents.

## Salted Hash

This tool will generate a (optionally salted) hash. The algorithm is SHA-256.
 _Don't forget to specify the algorithm used so others can easily verify!_

<input type="text" id="hash-salt" name="hash-salt" />

<textarea id="hash-plaintext" name="hash-plaintext" rows="6" cols="50">
</textarea>
<textarea id="hash-output" name="hash-output" rows="6" cols="50" readonly>
</textarea>

<input type="button" value="Hash" onclick="handleHash();">


(The final input is just "salt + newline + plaintext".)

## Password-Encrypted Cipher

This tool will encrypt a plaintext with a password, or decrypt from a password. The algorithm used is AES-256.
 _Don't forget to specify the algorithm used so others can easily verify!_

<input type="text" id="cry-password" name="cry-password" />

<textarea id="cry-plaintext" name="cry-plaintext">
</textarea>
<textarea id="cry-ciphertext" name="cry-ciphertext">
</textarea>

<input type="button" value="Encrypt" onclick="handleEncrypt();">
<input type="button" value="Decrypt" onclick="handleDecrypt();">


## Implementation Notes

Hashing uses [jshashes](<>). Password encryption uses [OpenPGPjs](<https://openpgpjs.org>) version 6.1.0.

This page runs entirely in your browser (hence why browser support is required), and the source code is available in the Webmastor's GitHub repository.
