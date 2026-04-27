class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        fronts = [heights[-1]]
        for i in range(len(heights) - 2, -1, -1):
            for j in range(len(fronts) - 1, -1, -1):
                ans[i] += 1
                if heights[i] <= fronts[j]:
                    break
            
            while fronts and fronts[-1] < heights[i]:
                fronts.pop()
            fronts.append(heights[i])
        # for i in range(len(heights)):
        #     j = i + 1
        #     max_height = 0
        #     for j in range(i + 1, len(heights)):
        #         if heights[j] >= heights[i]:
        #             ans[i] += 1
        #             break
        #         elif j - 1 == i or heights[j] > max_height:
        #             ans[i] += 1
        #         max_height = max(max_height, heights[j])
        return ans