import json

with open("menu.txt","r+") as f:
    s=f.read()
    res=json.loads(s)

print(res)