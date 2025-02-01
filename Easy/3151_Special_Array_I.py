class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        result = True

        if len(nums) > 1:
            for i in range(len(nums) - 1):
                if nums[i] % 2 == 0 and nums[i+1] % 2 == 0:
                    result = False
                elif nums[i] % 2 != 0 and nums[i+1] % 2 != 0:
                    result = False
        
        return result
        
