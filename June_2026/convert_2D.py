nums = [1,3,4,1,2,3,1]

nums2D = []
dup_nums = nums 
temp_dup = []

while len(dup_nums) != 0:
    temp = []
    temp_dup = []
    for i in dup_nums:
        if i not in temp:
            temp.append(i)
        else:
            temp_dup.append(i)
            
    nums2D.append(temp)
    dup_nums = temp_dup
    
print(nums2D)
    
