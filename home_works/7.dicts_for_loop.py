# Task 1:

# sentence = input ('Please, enter some text: ')

# words = sentence.split()

# word_counts = {}
# for word in words:
#     word = word.lower()
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1

# print('Words occurancies: ', word_counts)

# task 2

# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# end_price = {}
# for key in prices.keys():
#         end_price[key] = prices[key] * stock[key]
# print(end_price)

# task 3

# list_new = [(i, i*i) for i in range(1,11)]
# print(list_new)

# task 4
list_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
my_dict = {}
for i in range(1, 8):
    my_dict[i] = list_week[i-1]
print(my_dict)
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)