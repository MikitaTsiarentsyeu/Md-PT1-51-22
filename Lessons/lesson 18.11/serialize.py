import json
import pickle

s = '{"width":500,"height":500,"resolution":96,"quality":96,"settings":[{"filename":"_preview1.jpg","seek":10},{"filename":"_preview2.jpg","seek":35},{"filename":"_preview3.jpg","seek":70},{"filename":"_preview4.jpg","seek":95}]}'

res = json.loads(s)
# print(type(res), res)

print(res["settings"][0]["seek"])
res["settings"][0]["seek"] = 12

print(json.dumps(res))

res["settings"] = tuple(res["settings"])
print(res, type(res["settings"]))

with open("test.json", 'w') as f:
    json.dump(res, f)

with open("test.json", 'r') as f:
    res = json.load(f)

print(type(res["settings"]))

print(pickle.dumps(res))

res["settings"] = tuple(res["settings"])
with open("test.pickle", 'wb') as f:
    pickle.dump(res, f)

with open("test.pickle", 'rb') as f:
    res = pickle.load(f)

print(type(res["settings"]))

s = pickle.dumps(print)
new_print = pickle.loads(s)

new_print("hello", "from", "new", "print")