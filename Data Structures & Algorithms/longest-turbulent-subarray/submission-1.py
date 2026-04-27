class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        max_count = 1
        count = 1
        is_up = None
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] and (is_up is None or is_up == True):
                count += 1
                is_up = False
            elif arr[i] < arr[i+1] and (is_up is None or is_up == False):
                count += 1
                is_up = True
            elif arr[i] != arr[i+1]:
                count = 2
                is_up = (arr[i] < arr[i+1])
            else:
                count = 1
                is_up = None
            max_count = max(max_count, count)
        
        return max_count