# user = {
#     "name": "Euler",
#     "age": "err",
#     1: "34",
#     "isMarried": True
# }

user = {
    "name": "Euler",
    "age": 32,
    "isMarried": True
}

# print(user["phone"])    # KeyError: 'phone'
print(user.get('phone'))
print(user.get("phone", "Not found"))

print(user["name"])
user["name"] = "Jane"
print(user)

user.update({"name": "Mark", "age": 45})
print(user)

del user["isMarried"]
print(user)

user.update({"phone": "24234245344"})
print(user)

age = user.pop("age")
print(user)
print(age)

print(len(user))
print(type(user.keys()))
print(user.keys())
print(user.values())
print(user.items())

for key in user:
    print(key)

for key, value in user.items():
    print(key, value)