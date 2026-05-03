nums = [1,2,3]

s_nums = set(nums)
maximum = max(nums)
moves = 0

for i in s_nums:
    moves += maximum - i 
    
print(moves)