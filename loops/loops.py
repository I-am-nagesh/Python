

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count ==3:
#         break


# count = 0
# while count < 5:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# numbers = [0,1,2,3,4,5]
# for number in numbers:
#     print(number)

# language = "Python"
# for letters in language:
#     print(letters)

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)

# person = {
#     'firsat_name' : 'Nagesh',
#     'last_name' : 'Pandey',
#     'age' : 20,
#     'country' : 'India',
#     'is_married' : True,
#     'skills' : ['javascript', 'react', 'node', 'mongoDB', 'python'],
# }
# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value)
    

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')