class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        done = [[strs[0]]]
        checker = {"".join(sorted(strs[0])) : 0}
        counter = 1
        for sub in strs[1:]:
            sub_s = "".join(sorted(sub))
            if sub_s in checker:
                done[checker[sub_s]].append(sub)
            else:
                done.append([sub])
                checker["".join(sorted(sub))] = counter
                counter += 1
        return done
                    
        