def duplicate():
    nums = [4,3,2,7,8,2,3,1,8]
    result = []
    
    index_demo = []
    
    for num in nums:
        index = abs(num) - 1
        index_demo.append(index)
        
        num2_demo = nums[index]
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
        
        
    print(result)
    
duplicate()