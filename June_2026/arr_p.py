nums = [4,3,2,1]
new_nums = []
count = 0
for i in nums:
    if i % 2 == 0:
        new_nums.append(0)
        if new_nums[count - i] < new_nums[count]:
            new_nums.insert(count - i, 0)
    else:
        new_nums.append(1)
        
print(new_nums)