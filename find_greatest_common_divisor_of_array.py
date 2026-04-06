from typing import List
def findGCD(nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        common = 0
        if maxi % mini == 0:
            return mini
        else:
            for i in range(2, maxi):
                if mini % i == 0 and maxi % i == 0:
                    common = i
            
        if common != 0:
            return common
        else:
            return 1
            
findGCD([6,7,9])