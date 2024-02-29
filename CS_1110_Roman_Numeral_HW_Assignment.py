############################################
#   CS 1110 Roman Numeral HW Assignment
############################################

#This code was written in the Fall semester of 2017 for the CS 1110 course at the University of Virginia

#This code takes in a number from the user and converts it to Roman numeral.

num = int(input('Enter a number: '))
while num < 1 or num > 4000:
    num = int(input('Enter a number'))

chart_number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
chart_roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

pointer = 0
s = ""

while num > 0:
    # move down list
    x = chart_number[pointer]
    while num < x:
        pointer += 1
        x = chart_number[pointer]
    a = num // x
    num = num - a * x
    for i in range(a):
        s += chart_roman[pointer]

print(s)
