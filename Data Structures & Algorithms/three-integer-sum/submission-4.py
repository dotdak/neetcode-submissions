import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        ans = set()
        counter = Counter(nums)
        distinct_nums = list(counter.keys())
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                counter[nums[i]] -= 1
                counter[nums[j]] -= 1
                if target in counter and counter[target] > 0:
                    ans.add(tuple(sorted([nums[i], nums[j], target])))
                counter[nums[i]] += 1
                counter[nums[j]] += 1

        # nums = sorted(nums)
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         target = -(nums[i] + nums[j])
        #         inx = bisect.bisect_left(nums, target)
        #         if inx not in [i, j, len(nums)] and nums[inx] == target:
        #             ans.add(tuple(sorted([nums[i], nums[j], target])))
        return list(ans)