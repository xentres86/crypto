import base64

ct = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

res = bytes.fromhex(ct)
print(base64.b64encode(res).decode('utf-8'))