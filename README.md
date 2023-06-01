Simple Digital Signature v1.0

This program is used to make a digital signature of file. It has 3 options:
1) Generate keys
2) Sign a file
3) Check a file digital signature

First of all, you need to generate RSA keys. The program use .wav sound files to 
generate private and public keys which have to be in sound-samples folder. 
Keys are written to .pem files in keys directory.

To sign a file, you have to choose it by typing its number in a console. 
Files to sign have to be in files directory. The signature is written to sign.dat
file in signature directory.

To validate a signature, you have to choose a file from files directory by 
typing its number in a console. The file sign.dat with signature is used in
validation process. Then in the console the result of the validation is printed. 
