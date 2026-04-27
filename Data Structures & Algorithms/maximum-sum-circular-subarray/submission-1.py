class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        # Standard Kadane's for max subarray
        max_sum, curr_max = nums[0], 0
        # Kadane's for min subarray
        min_sum, curr_min = nums[0], 0
        
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
            
        # If all numbers are negative, max_sum is the answer
        if max_sum < 0:
            return max_sum
        
        # Return max of linear subarray or circular subarray (total - min)
        return max(max_sum, total_sum - min_sum)