class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixes = [0]
        curr_sum = 0
        max_sum = nums[0]
        for num in nums:
            curr_sum += num
            prefixes.append(curr_sum)
            max_sum = max(max_sum, num)

        n = len(prefixes)
        for i in range(n-1):
            for j in range(i+1, n):
                max_sum = max(max_sum, prefixes[j] - prefixes[i])
        
        return max_sum
        