class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        
        if len(s) <= 1:
            return True
        if len(s) % 2 == 0:
            mid = len(s)//2
        else:
            mid = len(s)//2 + 1 
        for idx, char in enumerate(reversed(s)):
            print(char + "|" + s[idx])
            if char != s[idx]:
                return False
            if idx == mid:
                return True
        

        