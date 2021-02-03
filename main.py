
'''
Написать скрипт в котором пользователь вводит номер месяца в году (1 - Январь, 2 - Февраль и т.д.)
а на экран выводится название этого месяца.
'''

monthDict = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
    }

montch = int(input('Enter number montch: '))

try:
    print(monthDict[montch])
except KeyError:
    print('Not correct number')

'''
Написать скрипт в котором пользователь вводит номер месяца в году (1 - Январь, 2 - Февраль и т.д.)
а на экран выводится время года.
'''

montch = int(input('Enter number montch: '))

if montch < 1 or montch > 12:
    print('Not correct number')
elif montch <=2 or montch == 12:
    print('Winter')
elif montch <=5:
    print('Spring')
elif montch <=8:
    print('Summer')
else:
    print('Fall')

#Даны два целых числа (введенных пользвателем). Выведите значение наименьшего из них. 

numOne = int(input('Enter first value: '))
numTwo = int(input('Enter second value: '))

if numOne > numTwo:
    print('First value more !')
elif numOne < numTwo:
    print('Second value more !')
else: 
    print('The values ​​are the same !')


'''
Даны три целых числа. Определите, сколько среди них совпадающих. 
Программа должна вывести одно из чисел: 3 (если все совпадают), 
2 (если два совпадает) или 0 (если все числа различны). 
'''

numOne = int(input('Enter first value: '))
numTwo = int(input('Enter second value: '))
numThree = int(input('Enter third value: '))

if numOne == numTwo == numThree:
    print(3)
elif numOne == numTwo or numTwo == numThree or numThree == numOne:
    print(2)
else:
    print(0)

'''
Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. 
В соответствии с григорианским календарем, год является високосным, 
если он делится на четыре без остатка, но если он делится на 100 без остатка, 
это не високосный год. Однако, если он делится без остатка на 400, это високосный год.
'''

year = int(input('Enter year: '))
if year < 1:
    print('Not correct year !')
elif (year % 100 != 0) and (year % 4 == 0) or (year % 400 == 0):
    print('yes')
else:
    print('not')