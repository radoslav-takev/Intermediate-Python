li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x ** x


# This is version 1
# newList = []
# for x in li:
#     newList.append(func(x))
#
# print(newList)

# this is the version 2 of the code with map
print(list(map(func, li)))

# this is the version 3 of the same code - this is list comprehension
print([func(x) for x in li])
