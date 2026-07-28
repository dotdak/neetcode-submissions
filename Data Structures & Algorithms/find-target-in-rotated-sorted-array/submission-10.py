class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        smallest_inx = 0
        def bs(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] < target:
                return bs(mid + 1, r)
            elif nums[mid] > target:
                return bs(l, mid - 1)
            else:
                return mid
        if nums[l] > nums[r]:
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            smallest_inx = l
            # for k, num in enumerate(nums):
            #     if num >= nums[smallest_inx]:
            #         smallest_inx = k
            #     else:
            #         break
            if target >= nums[0]:
                return bs(0, smallest_inx - 1)
            else:
                return bs(smallest_inx, len(nums) - 1)
        else:
            return bs(0, len(nums) - 1)

