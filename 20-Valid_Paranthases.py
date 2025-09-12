class Solution:
    def isValid(self, s: str) -> bool:
        #MY SOLUTION
        if len(s)%2 !=0:
            return False
        h=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                h.append(s[i])
            elif h:
                if s[i]==')' and h.pop() != '(':
                    return False 
                elif s[i]==']' and h.pop() != '[':
                    return False 
                elif s[i]=='}' and h.pop() != '{':
                    return False 
            else:
                return False

            
        return not h

        # NEETCODE
        # Map = {")": "(", "]": "[", "}": "{"}
        # stack = []

        # for c in s:
        #     if c not in Map:
        #         stack.append(c)
        #         continue
        #     if not stack or stack[-1] != Map[c]:
        #         return False
        #     stack.pop()

        # return not stack

