#!/usr/bin/env python3
message = 'Your final letter grade is'
print('What is your test score?')
connection = float(input())
if test score >= 90 & <= 100:
    message = message + 'A.'
elif test score >= 80 & <= 89:
    message = message + 'B.'
elif test score >= 70 & <= 79:
    message = message + 'C.'
elif test score >= 60 & <= 69:
    message = message + 'D.'
elif test score <= 59:
    message = message + 'F.'
else:
    message = 'Please enter your test score.'
print(message)
