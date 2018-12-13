#!/usr/bin/env python3
#message = 'Your final letter grade is '
print('What is your testscore?: ')
testscore = float(input())

# Convert it to an integer, which will truncate the decimal portion
testscore =int(testscore)

#This formats the testscore as a string with no decimal places
#testscore = format(testscore, '.0f')

print(testscore)
if testscore >= 90:
    print('Your final letter grade is an A.')
elif testscore in range (80, 89):
    print('Your final letter grade is a B.')
elif testscore in range (70, 79):
    print('Your final letter grade is a C.')
elif testscore in range (60, 69):
    print('Your final letter grade is a D.')
elif testscore <= 59:
    print('Your final letter grade is an F.')
print('You are done assessing your grade')
print()
