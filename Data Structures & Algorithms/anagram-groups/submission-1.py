class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sortedv = ''.join(sorted(i))
            res[sortedv].append(i)
        return list(res.values())