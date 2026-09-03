class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = []
        nums.sort()
        curr = nums[0]
        count = 1
        for n in nums[1:]:
            if n == curr:
                count +=1
            if n != curr:
                frequence.append((count, curr))
                count = 1
                curr = n
        frequence.append((count, curr))
        frequence.sort()
        ret = []
        for i in frequence[k*-1:]:
            ret.append(i[1])
        return ret

            
        