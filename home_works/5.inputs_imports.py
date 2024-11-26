# Task 1:

print('\n')
import random
user_number = int(input())
random_number = random.randint(1, 10)

if user_number == random_number:
    print('You guessed it right! ', random_number)
else:
    print('Try again, the desired number was: ', random_number)


# Task 2:

u_name = input()
u_age = int(input())

print(f"Dear {u_name}, next year you are turning {u_age + 1}!" )

# Task 3:
import random
u_example = input('Enter the word: ')

for i in range(5):
    convertion_1 = list(u_example)
    random.shuffle(convertion_1)
    random_string = ''
    for x in convertion_1:
        random_string += x
    print(random_string)



