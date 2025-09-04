class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Efficient SOLUTION
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        # l=''
        # c=0
        # for i in range(len(s)):
        #     if s[i] not in l:
        #         l+=s[i]
        #         c=max(c, len(l))
        #     else:
        #         l=l.split(s[i]) # to take care of 'vdvdf' hence l= ['', 'd'] next l=['', 'v']
        #         l=l[-1] # l='d' next l='v'
        #         l+=s[i] # l='dv' next l='vd'
        # return c

