numbers = [100, 130, 140, 150, 190, 200, 200, 230, 250, 250]

# print('Normal List: ', numbers)

# numbers.sort()
# print("Sorted List: ", numbers)

# numbers.sort(reverse = True)
# print("Sorted Reversed List:", numbers)

# print(numbers[4:7])
# print(numbers[7:])

# 2D list

numbers_2d = [
    [25, 27, 28, 27],
    [23, 24, 26, 26],
    [24, 24, 27, 27],
    [22, 24, 25, 24]
]

print(numbers_2d[0:])

for i in numbers_2d:
    for j in i:
        print(j, end=' ')
    print()
