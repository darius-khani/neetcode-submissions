class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = []
        nums.sort()
        curr = nums[0]
        count = 1
        #added = False
        #print(nums)
        for n in nums[1:]:
            if n == curr:
                count +=1
                #added = False
            if n != curr:
                frequence.append((count, curr))
                count = 1
                curr = n
                #added = False
        frequence.append((count, curr))
        frequence.sort()
        #print(added)
        #print(curr)
        #print(frequence)
        ret = []
        for i in frequence[k*-1:]:
            ret.append(i[1])
        return ret

            
        