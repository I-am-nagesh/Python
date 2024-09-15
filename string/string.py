

#multiline string is created using ''' and """
multiline_string = '''i am a student,learning
python  programming language'''
print(multiline_string)

#string concatenation
first_name = 'nagesh'
last_name = 'pandey'
space = ' '
full_name = first_name + space + last_name
print(full_name)

#escape sequences
print('i am learning pyhton.\nare you learnong too ?') #line break
print('Days\tTopics\tExercises')   #adding tab spaces or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t8\t21')
print('Day 3\t2\t30')
print('this is a backslash symbol (\\)')  #to write backslash
print('in every programming language it starts with \"hello world!\"')  # to write a double quote


#string formatting
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'area of a circle with a radius {} is  {}' .format(radius, area)
print(formated_string)

language = 'Pyhton'
 
#unpacking character
a,b,c,d,e,f = language
print(a)
print(b)
print(f)

#accessing character
first_letter = language[0]
print(first_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

last_letterr = language[-1]
print(last_letterr)

#slicing
first_three = language[0:3]
print(first_three)  #pyt
last_three = language[3:6]
print(last_three)    #hon

#reverse string
print(language[::-1])

#string method

#capitalize()
print(language.capitalize())

#count()
print(language.count('n'))
