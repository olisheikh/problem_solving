nums = [0,1,0,3,12]

l = len(nums)
for i in range(l):
    if nums[i] == 0:
        nums.append(0)
        if i < l:
            nums[i] = nums[i + 1]
            nums.remove(nums[i + 1])
            
print(nums)
    
    