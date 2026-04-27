import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        ans = set()
        # counter = Counter(nums)
        # distinct_nums = list(counter.keys())
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         target = -(nums[i] + nums[j])
        #         print(counter)
        #         counter[nums[i]] -= 1
        #         if counter[nums[i]] <= 0:
        #             counter.pop(nums[i])
        #         print(counter)
        #         counter[nums[j]] -= 1
        #         if counter[nums[j]] <= 0:
        #             counter.pop(nums[j])
        #         print(counter)
        #         if target in counter:
        #             ans.add(tuple(sorted([nums[i], nums[j], target])))
        #         counter[nums[i]] = counter.setdefault(nums[i], 0) + 1
        #         counter[nums[j]] = counter.setdefault(nums[j], 0) + 1
        # return list(ans)

        nums = sorted(nums)
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                target = -(nums[i] + nums[j])
                inx = bisect.bisect_left(nums, target)
                if inx not in [i, j, len(nums)] and nums[inx] == target:
                    ans.add(tuple(sorted([nums[i], nums[j], target])))
        return list(ans)