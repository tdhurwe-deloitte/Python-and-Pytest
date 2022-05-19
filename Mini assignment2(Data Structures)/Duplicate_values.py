from collections import Counter


def find_duplicates(arr):
    for i in range(len(arr)):
        dictionary = dict(Counter(arr[i]))
        print_duplicates(dictionary)


def print_duplicates(dictionary):
    for key, value in dictionary.items():
        if value > 1:
            print(f"{key} -> {value}")


num = int(input("Enter the number of arrays : "))
arr = []
for i in range(num):
    ls = list(map(int, input("Enter space separated : ").split(" ")))
    arr.append(ls)
find_duplicates(arr)
