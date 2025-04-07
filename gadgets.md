---
layout: puremd
---
<script>
  async function handleHash() {
    const salt = document.getElementById("hash-salt").value.trim();
    const plaintext = document
      .getElementById("hash-plaintext")
      .value
      .split(/\r?\n|\r|\n/g)
      .map((line) => line.trim())
      .join("\n")
      .trim();
    const saltedPlaintext = (salt + "\n" + plaintext).trim();
    const encodedPlaintext = new TextEncoder().encode(saltedPlaintext);
    const hashedMessage = await window.crypto.subtle.digest("SHA-256", encodedPlaintext);
    const encodedHashedMessage = btoa(
      new Uint8Array(hashedMessage)
        .reduce((data, byte) => data + String.fromCharCode(byte), '')
    );
    const output = document.getElementById("hash-output");
    output.value = encodedHashedMessage;
  }
</script>

# Webmastor's Gadgets

This page provides gadgets for helping to create Fingerprints and other digitally-altered artifacts.

## Salted Hash

This tool will generate an (optionally salted) hash using the SHA-256 algorithm.

An example of a strong salt might be four or more dictionary words chosen at random.

<label for="hash-salt">Salt</label>
<input type="text" id="hash-salt" name="hash-salt" />

<textarea id="hash-plaintext" name="hash-plaintext" rows="6" cols="80">
I transfer 1 spendie to the Webmastor.
</textarea>

<textarea id="hash-output" name="hash-output" rows="1" cols="60" readonly>
</textarea>

<input type="button" value="Hash" onclick="handleHash();">

The process used to generate this hash is as follows:

1. We remove leading and trailing whitespace from each line of both the salt and the hashed message, as well as any empty lines at the beginning or end.
2. We standardize all new-line characters to `\n`.
3. If `salt` is given, we combine the salt and plaintext (salt + newline + plaintext).
4. We run the bytes of the text through SHA-256 encryption.
5. We encode the result in [base 64](<https://en.wikipedia.org/wiki/Base64>) for displaying.

You should specify the algorithm/process to recreate the hash and/or link back to this page when you make your commitment.

## Implementation Notes

This page runs entirely in your browser. Values do not leave your computer.

The source code for this page is available in the [Webmastor's GitHub repository](<https://github.com/AgoraNomic/Webmastor/blob/gh-pages/gadgets.md?plain=1>).
