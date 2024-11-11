# Task1: program that has your name and the current day of the week

name = 'Krystyna'
day = 'Monday'

print('\n\nTask1\n\n')
print(
     f'Good day, {name}! {day} is a perfect day to learn some python.'
     )

print(
     'Good evening, %s! %s was a perfect day to learn some python.' % (name, day)
     )


# Task2: Save your first and last name as separate variables,
# then use string concatenation to add them together with 
# a white space in between and print a greeting

name = 'Tina'
last_name = 'Chuchman'

print('\n\nTask2\n\n')
print('Grettings, ' + name + ' ' + last_name + '!')


# Task3: Make a program with 2 numbers saved in separate variables
# a and b, then print the result for each of the following

a = 10
b = 3

print('\n\nTask3\n\n')
print('Addition: ', a+b)
print('Subtraction: ', a-b)
print('Division: ', a/b)
print('Multiplication: ', a*b)
print('Power: ', a**b)
print('Modulus: ', a%b)
print(f'Floor division: ', a//b)

