class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        for i in range(len(nums)):
            if nums[i] == 0:
                return False
            for k in range(1, nums[i]+1):
                if self.canJump(nums[k:]):
                    return True
        
        return True
