nums = [4,1,3]
k = 4
summation = sum(nums)
count = 0

while summation != 0:    
    if summation % k == 0:
        print(count)
        break
    else:
        summation -= 1
        count += 1