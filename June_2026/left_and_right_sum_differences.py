# 1. MySolution
# nums = [10,4,8,3]

# left_sum = [0]
# right_sum = [0] * (len(nums))
# subtraction_list = []

# for i in range(len(nums) - 1):
#     left_sum.append(nums[i] + left_sum[i])    
#     right_sum[len(nums)-2 - i] =  nums[len(nums) - 1 - i] + right_sum[len(nums) - 1 - i]
    
    
# print([abs(left_sum[i] - right_sum[i]) for i in range(len(nums))])

nums = [10, 4, 8, 3]

total_sum = sum(nums)
left_sum = 0
final_ar = []

for i, value in enumerate(nums):
    final_ar.append(abs(total_sum - left_sum - value))
    left_sum += value
    total_sum -= value    
    
print(final_ar)