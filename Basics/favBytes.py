ct = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
flag = ""

for secret in range(256):
	res = [chr(c ^ secret) for c in ct]
	flag = "".join(res)

	if flag.startswith("crypto"):
		print(flag)
		print(secret)