class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            if n not in h:
                h[n] = 1
            else:
                h[n] += 1
        l = [(x,y) for x,y in h.items()]
        l.sort(key=lambda x:x[1])
        distinct = len(h)
        res = []
        for i in range(distinct-k, distinct):
            res.append(l[i][0])
        
        return res