class Solution:
    def letterCombinations(self, digits: str) -> List[str]: # type:ignore
        if not digits:
            return []
        
        res = []
        sub = ''
        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, sub):
            if len(sub) == len(digits):
                res.append(sub[:])
                return
            for c in digitMap[digits[i]]:
                backtrack(i+1, sub + c)
        backtrack(0, sub)
        return res