import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
len_list = len(friends)
random_int =random.randint(0, len_list - 1)

print(friends[random_int])