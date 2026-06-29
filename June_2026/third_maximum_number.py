nums = [2,2,3,1]

maximum_value = second_max = third_max = float('-inf')


for i in nums:
    if i == maximum_value or i == second_max or i == third_max:
        continue
    if i > maximum_value:
        third_max = second_max
        second_max = maximum_value
        maximum_value = i
    elif i > second_max:
        third_max = second_max
        second_max = i
    elif i > third_max:
        third_max = i

if third_max == float('-inf'):
    print(maximum_value)
    
else:
    print(third_max)