# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# print(test)
# test.add(5)
# print(test)
# test.pop()
# print(test)
# test.pop()
# print(test)
# def func (d: dict):
#     print('input quant')
#     quant = int(input())
#     #name
#     #esteem
#     for i in range(quant):
#         name = input('input name')
#         esteem = input('input esteem')
#         d[name] = esteem
#     return d
#
# d = {}
# print(func(d))

# ??????????????
# d = {1: "1"}
# def update_dict (d: dict, key, meaning):
#     if (key in d) & (type(d[key]) == int):
#         list(d[key])
#         d[key].append(meaning)
#     if (key in d) & (type(d[key]) == list):
#         d[key].append(meaning)
#     if key not in d:
#         d[key] = meaning
#     return d
#
# print(update_dict(d, 2, 20))
# ??????????????


# with open("text.txt", "r") as f:
#     lines = f.readlines()

import random


# def Fact(n):
#     if (n == 1):
#         return 1
#     else:
#         return Fact(n-1)*n
#
# print(Fact(5))

def Fib(n):
    if (n == 1) or (n==2):

        return 1

    else:

        return Fib(n-1)+Fib(n-2)


print(Fib(6))















