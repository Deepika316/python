import json
inp='{"name":"Alice","age":90}'
r=json.loads(inp)#str to dict
print(r)
r=json.dumps(r)#dict to str
print(r)