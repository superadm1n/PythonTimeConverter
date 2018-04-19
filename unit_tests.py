from converter import *

# tests standard_to_mili function
print('Testing standard_to_mili function')
bad_values = ['12:30AM', '12:30 AM', '1230AM', '13:20:AM', '12:61:PM']
good_values = ['12:30:PM', '12:30:AM']


counter = 0
for value in bad_values:
    try:
        standard_to_mili(value)
    except ValueError:
        counter += 1

if counter == len(bad_values):
    print('Formatting Test: Pass')
else:
    print('Formatting Test: Fail!')


counter = 0
for value in good_values:
    try:
        returned_value = standard_to_mili(value)
        counter += 1
    except ValueError as E:
        print(E)

if counter == len(good_values):
    print('Value Test: Pass')
else:
    print('Value Test: Fail!')

# Tests mili_to_standard function
print('Testing mili_to_standard function')

bad_values = ['25:30',
              '14:61',
              '1430',
              '15:30:5']

good_values = ['15:45',
               '9:15']

counter = 0
for value in bad_values:
    try:
        mili_to_standard(value)
    except ValueError:
        counter += 1

if counter == len(bad_values):
    print('Formatting Test: Pass')
else:
    print('Formatting Test: False')

counter = 0
for value in good_values:
    try:
        mili_to_standard(value)
        counter += 1
    except ValueError:
        pass

if counter == len(good_values):
    print('Value Test: Pass')
else:
    print('Value Test: False')
