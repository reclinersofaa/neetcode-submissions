class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashMap = {}
        for i in s1:
            hashMap[i] = 1 + hashMap.get(i, 0)        

        l = 0

        for r in range(len(s2)):
            if s2[r] in hashMap:
                hashMap[s2[r]] -= 1
            else:
                hashMap[s2[r]] = -1
            
            if (r - l + 1) > len(s1):
                hashMap[s2[l]] = hashMap.get(s2[l], 0) + 1
                if hashMap[s2[l]] == 0:
                    del hashMap[s2[l]]
                l += 1
            
            if s2[r] in hashMap and hashMap[s2[r]] == 0:
                del hashMap[s2[r]]
            
            if not hashMap:
                return True
        
        return False
            


        