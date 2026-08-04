class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cto = {")" : "(", "]" : "[", "}" : "{"}

        for i in s:
            if i in ('(','[','{'):
                stack.append(i)
                print(stack)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if cto[i] != p:
                    return False
        if not stack:
            return True
        else:
            return False

