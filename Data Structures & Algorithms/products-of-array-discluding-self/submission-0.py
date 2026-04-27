class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        product = 1
        prefix = []
        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= product
            product *= nums[i]
        return prefix