class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        done = [[strs[0]]]
        checker = {"".join(sorted(strs[0]))}
        print(done)
        for sub in strs[1:]:
            #print(sub)
            if "".join(sorted(sub)) in checker:
                for i in range(len(done)):
                    if "".join(sorted(sub)) == "".join(sorted(done[i][0])):
                        done[i].append(sub)
                        #print(f"{sub} {done[i][0]}")
                        #print(done)
                        break
            else:
                done.append([sub])
                checker.add("".join(sorted(sub)))
                #print(done)
        return done
                    
        