def longest_common_prefix():
    nums = [0,0,1,1,1,2,2,3,3,4]
    j = 0
    count = 1
        
    for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[count] = nums[i]
                count += 1
                j += 1
            else:
                j += 1
            
    print(nums)
    
    
longest_common_prefix()