class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = defaultdict(int)
        res = []

        for i,n in enumerate(s):
            hm[n] = i
        
        end = 0
        size = 1
        for i in range(len(s)):
            end = max(end, hm[s[i]])

            if end == i: #trigger: append curr size to res, reset size and move on
                res.append(size)
                size = 1
                continue
            
            #end = max(end, hm[s[i]])
            
            size += 1
            print(end, size)

        return res
            


            
