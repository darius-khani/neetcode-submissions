class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequenceM = {}
        for num in nums:
            frequenceM[num] = frequenceM.get(num, 0) + 1  
        #print(frequenceM)
        
        frequenceL = []
        for num, frq in frequenceM.items():
            frequenceL.append((frq, num))
        #print(frequenceL)
        frequenceL.sort()

        ret = []
        for i in frequenceL[k*-1:]:
            ret.append(i[1])
        return ret
        
        """
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
        """

            
        