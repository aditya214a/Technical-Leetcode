class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: # type: ignore
        def search(nums,target,findFirst):
            ans=-1
            start=0
            end=len(nums)-1
            while(start<=end):
                mid=(start+end) //2
                if(target<nums[mid]):
                    end=mid-1
                elif(target>nums[mid]):
                    start=mid+1
                else:
                    ans=mid
                    if(findFirst):
                        end=mid-1
                    else:
                        start=mid+1
            return ans
        start=search(nums,target,True)
        end=search(nums,target,False)
        return [start,end]

