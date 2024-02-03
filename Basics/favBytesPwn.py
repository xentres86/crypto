from pwn import xor

ct = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
flag = ""

for secret in range(256):
	resb = [xor(c, secret) for c in ct]
	ress = [x.decode('utf-8') for x in resb]

	flag = "".join(ress)

	if flag.startswith("crypto"):
		print(flag)
		print(secret)
		break