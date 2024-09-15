
person = {
  'first_name': 'Nagesh',
  'last_name' : 'Pandey',
  'age' : 20,
  'country' : 'India',
  'is_marred' : 'True',
  'skills' :['javascript', 'reatct', 'node', 'mongoDB', 'python'],
  'address' :{
      'city' : 'bhojpur',
        'pincode' : '802312'  
    }
 }

print(len(person))    #dictionary length
print(person['first_name'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['city'])
# print(person['state'])   error
print(person.get('state'))   #return NoneType object data type
print(person.get('first_name'))

#adding value in dictionary
person['job_title'] = 'engineer'
person['skills'].append('HTML')
print(person)

#modifying value in dictionary
person['age'] = 21
print(person)

#removing key and value
person.pop('first_name')
person.popitem()
del person['is_marred']
print(person)

#changing dictionary to a list of items
print(person.items())

#clearing a dictionary
# print(person.clear())

#copy a dictionary
copy_person = person.copy()
print(copy_person)

#getting keys as a list
keys = person.keys()
print(keys)

#getting values as a list
values = person.values()
print(values)




