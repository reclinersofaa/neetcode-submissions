class Solution:
    def checkValidString(self, s: str) -> bool:
        openmin, openmax = 0, 0

        for i in s:
            if i == '(':
                openmin, openmax = openmin + 1, openmax + 1
            elif i == ')':
                openmin, openmax = openmin - 1, openmax - 1
            else: #* openmax increases if you consider that as (
                openmin, openmax = openmin - 1, openmax + 1
            
            if openmax < 0: #if even in best ( case is -ve then there are much more )
                return False
            
            if openmin < 0:
                openmin = 0
            
        return openmin == 0


            
