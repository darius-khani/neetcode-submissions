class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[num] = idx
        
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target):
                    #print(f"{nums[i]} + {nums[j]}")
                    return [i, j]
        """
        