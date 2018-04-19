"""
MIT License

Copyright (c) 2018 Kyle Kowalczyk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Kyle Kowalczyk
Purpose: To have a module that someone can integrate into an exisiting project
or use directly on the command line and convert time from military time to
standard and vice versa.
"""

def mili_to_standard(militaryTime):

    """Function to convert military time to Standard time.

    :param militaryTime: Military time in format HH:MM
    :type militaryTime: str
    :return: Standard time that was converted from the supplied military time
    :rtype: str
    """

    # Handles formatting errors in the military time supplied
    if ':' not in militaryTime or len(militaryTime.split(':')) != 2:
        raise ValueError('militaryTime value must be supplied in the following format HH:MM')

    # Creates variables for the hours and minutes supplied by the user and interprets them as integers
    hour, minute = militaryTime.split(':')
    hour, minute = int(hour), int(minute)

    # handles errors in the supplied hour and minute of the military time
    if minute > 60:
        raise ValueError('Supplied minute value can not be greater than 60, you entered {}'.format(minute))

    if hour > 24:
        raise ValueError('Supplied hour value can not be greater than 24, you entered {}'.format(hour))

    # Determines weather the military time specified is AM or PM and converts it to standard time
    if hour > 12:
        ampm = 'PM'
        hour -= 12
    else:
        ampm = 'AM'

    # Returns standard time to user
    return '{}:{}:{}'.format(hour, minute, ampm)


def standard_to_mili(standardTime):

    '''Function to convert standard time in format HH:MM:AM/HH:MM:PM into military
    time in format HH:MM.

    :param standardTime: Standard time in format HH:MM:AM or HH:MM:PM
    :type standardTime: str
    :return: Military conversion of the supplied standard time in format HH:MM
    :rtype: str
    '''

    if ':' not in standardTime or len(standardTime.split(':')) != 3:
        raise ValueError('standardTime variable must be formatted in "HH:MM:AM" or "HH:MM:PM"')

    hour, minute, letters = standardTime.split(':')
    hour, minute, letters = int(hour), int(minute), str(letters)

    if minute > 60:
        raise ValueError('Max value for minute is 60, you specified {}'.format(minute))

    if hour > 12:
        raise ValueError('Max value for hour is 12, you supplied {}'.format(hour))

    if letters.lower() == 'am' or letters.lower() == 'pm':
        pass
    else:
        raise ValueError('You must specify AM or PM, you specified'.format(letters))

    if letters.lower() == 'pm':
        hour += 12

    return '{}:{}'.format(hour, minute)






if __name__ == '__main__':

    """Small Script to utilize the 2 functions to convert military time to standard or vice versa
    This will be run if the module is called directly so you can use this as a command line tool
    """

    import sys

    usage = '''
    converter.py <ENTER>
    converter.py -m2s HH:MM <ENTER> --> converts Military time to Standard time
    converter.py -s2m HH:MM:AM/HH:MM:PM <ENTER> --> converts Standard time to Military time
    
    '''

    if len(sys.argv) == 1:

        answer = input('Make Selection\n1) Military time --> Standard time\n2) Standard time --> Military Time\n> ')

        try:
            answer = int(answer)
        except:
            print('Invalid Selection, exiting')
            exit()

        if answer == 1:
            variablefunction = mili_to_standard
            time = input('Enter time in format HH:MM\n> ')
        elif answer == 2:
            variablefunction = standard_to_mili
            time = input('Enter time in format HH:MM:AM or HH:MM:PM\n> ')
        else:
            print('Invalid Selection, exiting')
            exit()

        try:
            print(variablefunction(time))
        except ValueError as E:
            print('Incorrect data entered, ValueError exception caught:\n"{}"'.format(E))

    elif len(sys.argv) == 3:

        if sys.argv[1] == '-m2s':
            print(mili_to_standard(sys.argv[2]))
        elif sys.argv[1] == '-s2m':
            print(standard_to_mili(sys.argv[2]))
        else:
            print('Invalid Usage, see examples below')
            print(usage)
            exit()
    else:
        print(usage)