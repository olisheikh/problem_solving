nums = [9,12,5,10,14,3,10]
pivot = 10

left_list = []
right_list = []
equal = []
for i in nums:
    if i > pivot:
        right_list.append(i)
    elif i < pivot:
        left_list.append(i)
    else:
        equal.append(i)
        
print(left_list + equal + right_list)
