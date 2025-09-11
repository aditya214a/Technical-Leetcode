class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float: # type: ignore
        A, B = n1, n2
        total = len(A) + len(B)
        half = total//2

        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B
            
            Aleft = A[i] if i>=0 else float("-inf")
            Aright = A[i + 1] if (i + 1)<len(A) else float("inf")
            Bleft = B[j] if j>=0 else float("-inf")
            Bright = B[j + 1] if (j + 1)<len(B) else float("inf")

            #  Correct partion
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

    ## TC = O(log(min(m,n)))