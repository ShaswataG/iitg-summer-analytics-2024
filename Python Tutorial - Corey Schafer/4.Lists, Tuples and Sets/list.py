# slicing
# list methods - append, insert

people1 = ["Raj", "Shyam", "Johnny"]
people2 = ["Shreya", "Priya"]
# people1.insert(0, people2)    # [['Shreya', 'Priya'], 'Raj', 'Shyam', 'Johnny']
# people1.append(people2)       # ['Raj', 'Shyam', 'Johnny', ['Shreya', 'Priya']].

# people1 = people2+people1     # ['Shreya', 'Priya', 'Raj', 'Shyam', 'Johnny']
# people1.extend(people2)       # ['Raj', 'Shyam', 'Johnny', 'Shreya', 'Priya']

print(people1)

# people1.remove('dfd')
people1.pop()
print(people1)

people1.reverse()
print(people1)

people1.sort()
print(people1)

people1.sort(reverse=True)
print(people1)

# we can return a duplicate sorted list instead of altering the original list by using sorted function instead of sorted method
a = [35, 24, 1, 345, 0]
cpy = sorted(a)
print(a)
print(cpy)

print(min(a))
sum(a)
max(a)
a.index(35)
print(100 in a)

for person in people1:
    print(person)

for index, person in enumerate(people1):
    print(f'people1[{index}] = {person}')

for index, person in enumerate(people1, start= 3):  # indexing starts from 3
    print(f'people1[{index}] = {person}')


characters = ["Sasuke", "Gojo", "Hinata", "Jiraya", "Naruto"]
charStr = ' -> '.join(characters)
print(charStr)

charStrToList = charStr.split(' -> ')
print(charStrToList)