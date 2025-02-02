class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        temp_nums = nums

        if sorted_nums == nums:
            return True
        else:
            for i in range(len(nums)):
                poped_num = temp_nums[0]
                temp_nums.pop(0)
                temp_nums.append(poped_num)

                if sorted_nums == temp_nums:
                    return True
        
        return False
