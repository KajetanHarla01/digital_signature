<h1>Digital Signature System v1.0</h1>

This program is used to make a digital signature of file. It has 3 options:
1) Generate keys
2) Sign a file
3) Check a file digital signature

<h2>Generating keys</h2>
To generate private and public keys, the program use <b>.wav</b> sound files which have to be in the <b>sound-samples</b> folder. Keys are written to <b>.pem</b> files in the <b>keys</b> directory.

<h2>Signing a file</h2>
Files to sign have to be in <b>files</b> directory. The signature is written to <b>sign.dat</b> file in the <b>signature</b> directory.

<h2>Signature validation</h2>
To validate a signature, you have to choose a signed file from the <b>files</b> directory. The file <b>sign.dat</b> with signature is used validation process. Then in the console, the result of the validation is printed.
