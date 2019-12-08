# def func(x):
#     return x+5
# print(func(2))
#
#
# func2 = lambda x: x + 5
# print(func2(9))


def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85
print(func(2))

func3 = lambda x,y:x+y
print(func3(3,5))


a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x: x+5, a))
print(newList)

newList2 = list(filter(lambda x: x%2==0, a))
print(newList2)
