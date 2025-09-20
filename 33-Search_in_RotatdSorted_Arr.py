class Solution:
    def search(self, nums: List[int], target: int) -> int: # type:ignore
        # def findPivot(arr):   #find pivot
        #     start =0
        #     end=len(arr)-1
        #     while(start<=end):
        #         mid= start+(end-start)//2
        #         if(mid<end and arr[mid]>arr[mid+1]):
        #             return mid
        #         elif(mid>start and arr[mid]<arr[mid-1]):
        #             return mid-1
        #         elif(arr[mid]<arr[start]):
        #             end=mid-1
        #         else:
        #             start=mid+1
        #     return -1

        # def binarySearch(arr,target,start,end):
        #     while(start<=end):
        #         mid=start+(end-start) //2 
        #         if(arr[mid]>target):
        #             end=mid-1
        #         elif(arr[mid]<target):
        #             start=mid+1
        #         else:
        #             return mid
        #     return -1
        
        # pivot=findPivot(nums)
        # # print(binarySearch(nums,target,0,len(nums)-1))
        # # if(len(nums)==1 and target==nums[0]): return 0
        # if(pivot == -1): return binarySearch(nums,target,0,len(nums)-1)
        # elif(nums[pivot]==target): return pivot
        # elif(target>= nums[0]): return binarySearch(nums,target,0,pivot-1)
        # else: return binarySearch(nums,target,pivot+1,len(nums)-1)

        ## NEETCODE
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1








