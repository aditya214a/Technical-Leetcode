class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if height[l]< height[r]:
                l+=1
            else:
                r-=1
            maxA= max(maxA,area)
        return maxA