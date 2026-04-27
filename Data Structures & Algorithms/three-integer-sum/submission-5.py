import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        ans = set()
        # counter = Counter(nums)
        # distinct_nums = list(counter.keys())
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         target = -(nums[i] + nums[j])
        #         counter[nums[i]] -= 1
        #         counter[nums[j]] -= 1
        #         if target in counter and counter[target] > 0:
        #             ans.add(tuple(sorted([nums[i], nums[j], target])))
        #         counter[nums[i]] += 1
        #         counter[nums[j]] += 1

        # nums = sorted(nums)
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         target = -(nums[i] + nums[j])
        #         inx = bisect.bisect_left(nums, target)
        #         if inx not in [i, j, len(nums)] and nums[inx] == target:
        #             ans.add(tuple([nums[i], nums[j], target]))

        nums = sorted(nums)
        print(nums)
        for i, num in enumerate(nums):
            if num > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                ssum = num + nums[l] + nums[r]
                if ssum > 0:
                    r -= 1
                elif ssum < 0:
                    l += 1
                else:
                    ans.add(tuple([num, nums[l], nums[r]]))
                    l += 1
                    r -= 1
        return list(ans)