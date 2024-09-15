#A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruits = fruits[0]
print(first_fruits)
last_index = len(fruits) - 1
print(fruits[last_index])
print(fruits)

last_fruit = fruits[-1]
print(last_fruit)

all_fruits = fruits[0:4]
print(all_fruits)
print(fruits)

print(fruits[0:])
print(fruits[1:3])
print(fruits[-4:])
print(fruits[-3:-1])

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)

fruits = tuple(fruits)
print(fruits)

del fruits