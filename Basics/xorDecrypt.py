from pwn import xor

ct = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

res = xor(ct[:7], "crypto{")
print("Partial Key: " + res.decode('utf-8'))

key = res.decode('utf-8') + "y"
flag = xor(ct, key)

print(flag.decode('utf-8'))