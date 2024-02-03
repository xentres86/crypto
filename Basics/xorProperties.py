from pwn import xor

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key1_2_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1b = bytes.fromhex(key1)
key1_2b = bytes.fromhex(key1_2)
key2_3b = bytes.fromhex(key2_3)
flag_1_2_3b = bytes.fromhex(flag_key1_2_3)

key2b = xor(key1b, key1_2b)
key3b = xor(key2b, key2_3b)
key1_2_3b = xor(key3b, key1_2b)

flagb = xor(flag_1_2_3b, key1_2_3b)

print("Flag: " + flagb.decode('utf-8'))