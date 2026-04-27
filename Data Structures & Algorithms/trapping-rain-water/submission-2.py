class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0] + height + [0]
        bars = []
        ans = 0
        for i, h in enumerate(height):
            # if not bars:
            #     bars.append((i, h))
            # if h < bars[-1]:
            #     bars.append((i, h))
            # else:
            while bars and bars[-1][1] < h:
                last_index, last_height = bars.pop()
                if not bars:
                    break
                distance = i - bars[-1][0] - 1
                bounded_height = min(h, bars[-1][1]) - last_height
                ans += distance * bounded_height
                # print(i, h, bars, ans)
            bars.append((i, h))

        return ans
