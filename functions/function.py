

def generate_full_name ():
    first_name = 'Nagesh'
    last_name = 'Pandey'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name ()


def generate_full_name ():
    first_name = 'Nagesh'
    last_name = 'Pandey'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name ())


def generate_ful_name (first_name, last_name):
    space = ' '
    full_name =first_name + space + last_name
    return full_name
print('Full Name: ',generate_ful_name('Nagesh', 'Pandey'))


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Nagesh', lastname = 'Pandey'))



def generate_full_name (first_name = 'Nagesh', last_name = 'Pandey'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Nagesh','Pandey'))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,4))