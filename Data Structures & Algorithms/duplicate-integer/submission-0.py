class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            for j in range (len(nums)):
                if (nums[i] == nums[j] and j != i):
                    return True
        return False
                
            

        