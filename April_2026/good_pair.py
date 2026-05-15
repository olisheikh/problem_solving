# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

nums = [1,2,3]
count = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] == nums[j] and i < j:
            count += 1
            
print(count)