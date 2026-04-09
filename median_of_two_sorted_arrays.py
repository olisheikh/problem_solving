# 1. Merge two array
# 2. Find the mid value of the merged array if odd elements.
# 3. Find the mean of mid values of the merged array if even elements.
num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10,11,12,13,14,15,16,17]

num3 = (num1 + num2).sort()

print()

if length_num3 % 2:
    print(num3[(length_num3 // 2)-1])
    print(num3[(length_num3 // 2)])
    print((num3[(length_num3 // 2)-1] + num3[(length_num3 // 2)])/2)
else:
    print(round(length_num3/2))
    print(num3[round(length_num3/2) - 1])
