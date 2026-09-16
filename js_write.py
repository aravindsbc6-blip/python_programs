import json
data = {
    "name": "Aravindh",
    "age": 22

}

with open("read.json","w") as file:
    json.dump(data,file)
print("ok written on read.json file")


with open("read.json","r")as file:
    data=json.load(file)
    print(data)