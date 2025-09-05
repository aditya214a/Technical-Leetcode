class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resL = 0

        def check(l, r, res,resL):
            while l>=0 and r<len(s) and s[r] ==s[l]:
                if (r - l + 1) > resL:
                    res = s[l:r+1]
                    resL = r - l +1
                l -=1
                r +=1
            return res, resL
        for i in range(len(s)):
            l = r = i # odd palindrome
            res, resL = check(l,r, res, resL)
            
            l, r = i, i+1 #even palindrome
            res, resL = check(l,r, res, resL)
        return res