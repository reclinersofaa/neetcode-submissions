class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        used = set() 
        for i in range(len(strs)):
            if i in used:
                continue
            temp = [strs[i]]
            i_sort = ''.join(sorted(strs[i]))
            used.add(i)
            for j in range(i+1, len(strs)):
                if j in used:
                    continue
                j_sort = ''.join(sorted(strs[j]))
                if i_sort == j_sort:
                    temp.append(strs[j])
                    used.add(j)
            res.append(temp)
        return res

