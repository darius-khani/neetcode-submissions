class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            if prices[right] - prices[left] > max:
                max = prices[right] - prices[left]
        return max

        