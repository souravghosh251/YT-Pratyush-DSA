
#Optimised Code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=1
        cm=1
        n=len(nums)
        while cm<n:
            if nums[cm]!=nums[cm-1]:
                nums[res]=nums[cm]
                res+=1
            cm+=1
        return res

        