nums = [0,1]


n = max(nums)

if n == 0:
    print(1)

for i in range(n+2):
    if i not in nums:
        print(i)