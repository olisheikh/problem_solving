# maximum = max(nums)

# if nums.count(maximum) == 2:
#     print(True)
# for i in nums:
#     if nums.count(i) > 1 and i != maximum:
#         print(False)

def isGood(nums: List[int]) -> bool:
        maximum = max(nums)

        if len(nums) != maximum + 1 or nums.count(maximum) != 2:
            return False
        
        for i in nums:
            if nums.count(i) == 2:
                return False

        return True

print(isGood([1, 3, 3, 2]))