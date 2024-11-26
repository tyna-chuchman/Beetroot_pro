# task1:

# import random
# random_numbers = []

# while len(random_numbers) <= 10:
#     random_number = random.randint(1, 10)
#     random_numbers.append(random_number)

# index = 0 
# largest_number = random_numbers[0]

# while index < len(random_numbers):
#     if random_numbers[index] > largest_number:
#         largest_number = random_numbers[index]
#     index += 1
# print(f'List of random numbers: {random_numbers} \n Largest number:  , {largest_number}')

# task2:

# import random
# list_1 = []

# while len(list_1) < 10:
#     random_number = random.randint(1, 10)
#     list_1.append(random_number) 
# print (list_1)

# list_2 = []

# while len(list_2) < 10:
#     random_number2 = random.randint(1, 100)
#     list_2.append(random_number2) 
# print(list_2)

# common_digits = []
# index1 = 0
# while index1 < len(list_1):
#     if list_1[index1] in list_2:
#         common_digits.append(list_1[index1])
#     index1 += 1
# print('Here are list with common digits: ', common_digits)

# list = [rand.randint for i in range(10)]

# import random
# list_1 = [random.randint(1, 10) for i in range(10)]
# list_2 = [random.randint(1, 20) for i in range(10)]

# common_digits = []
# index1 = 0
# while index1 < len(list_1):
#     if list_1[index1] in list_2:
#         common_digits.append(list_1[index1])
#     index1 += 1
# print(list_1)
# print(list_2)
# print('Here are list with common digits: ', common_digits)

# task3:
list_0 = []
for i in range(1,101):
    list_0.append(i)
print(list_0)
list_1 = []
for x in list_0:
    if x / 7 and x % 5 != 0:
        list_1.append(x)
print(list_1)

