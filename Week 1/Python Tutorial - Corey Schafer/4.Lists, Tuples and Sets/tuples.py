# Mutable
list1 = ["History", "Math", "Physics", "Computer"]
list2 = list1

# both list1 and list2 are the same mutable object
print(list1)    # ['History', 'Math', 'Physics', 'Computer']
list2[0] = "EVS"
print(list1)    # ['EVS', 'Math', 'Physics', 'Computer']
print(list2)    # ['EVS', 'Math', 'Physics', 'Computer']

# Immutable
tuple1 = ('Olivia', "Dua", "Selena", "Lana", "Gaga")
tuple2 = tuple1
print(tuple1)
print(tuple2)
print(tuple2[3])
# tuple2[2] = "Sia"   # TypeError: 'tuple' object does not support item assignment