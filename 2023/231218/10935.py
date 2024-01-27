import base64

S = input()
S = base64.b64encode(S.encode()).decode()
print(S)
