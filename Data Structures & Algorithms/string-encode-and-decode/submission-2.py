class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for item in strs:
            for char in item:
                ret += char
            ret += "é"
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        adder = ""
        for char in s:
            if char == "é":
                ret.append(adder)
                adder = ""
            else:
                adder += char
        return ret

