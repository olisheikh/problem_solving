def remove_element():
    nums = [0,1,2,2,3,0,4,2]
    count = 0
    j = 0
    val = 2
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    
            
    print(nums)
    print(j)
    
remove_element()