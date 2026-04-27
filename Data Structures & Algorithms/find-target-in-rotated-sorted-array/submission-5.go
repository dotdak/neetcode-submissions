func search(nums []int, target int) int {
    if len(nums) == 0 {
        return -1
    }
    l, r := 0, len(nums) - 1

    // find pivot
    for l < r {
        mid := (l + r) / 2
        if nums[mid] > nums[r] {
            l = mid + 1
        } else {
            r = mid
        }
    }

    pivot := l

    search := func(left, right int) int {
        for left <= right {
            mid := (left + right) / 2
            if nums[mid] > target {
                right = mid - 1
            } else if nums[mid] < target {
                left = mid + 1
            } else {
                return mid
            }
        }

        return -1
    }

    if result := search(0, pivot - 1); result != -1 {
        return result
    }

    return search(pivot, len(nums) - 1)
}
