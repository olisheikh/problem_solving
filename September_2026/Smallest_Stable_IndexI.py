nums = [5,0,1,4]
k = 3

max_num = float('-inf')
min_num = float('inf')
found = False

for i in range(len(nums)):
    max_num = max(nums[0:i+1])
    min_num = min(nums[i:len(nums)])
    
    difference = max_num - min_num
    
    if difference <= k:
        print(i)
        found = True
        break
    
    
if not found:
    print(-1)
    