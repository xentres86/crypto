from pwn import xor

# Variable declaration
text = "label"
number = 13
flag = ""

# Version without pwntools
for c in text:
	flag += chr(ord(c) ^ number)

print("crypto{" + flag + "}")

# Alternative with pwntools
flagpwn = xor(text, number)

print("crypto{" + flagpwn.decode('utf-8') + "}")