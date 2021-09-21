import json as j
nama = "fais"


ret = []
data = open("quotes.txt").read().split("\n")


for x in data:
    ret.append({
        "by": nama,
        "quote": x
    })


print(j.dumps(ret))