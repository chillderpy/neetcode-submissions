class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashCompare = []
        res = []
        for s in strs:
            temp = {}
            for ch in s:
                if ch not in temp:
                    temp[ch] = 1
                else:
                    temp[ch] += 1
            if temp not in hashCompare:
                hashCompare.append(temp)
                res.append([s])
            else:
                for idx in range(len(hashCompare)):
                    if hashCompare[idx] == temp:
                        res[idx].append(s)
        
        return res