func search(nums []int, target int) bool {
    pivot := 0
    if nums[0] >= nums[len(nums) - 1] {
        l, r := 0, len(nums)-1
        for l <= r {
            mid := (l + r) / 2
            if nums[mid] == target {
                return true
            }
            
            if nums[mid] == nums[l] && nums[mid] == nums[r] {
                l++
                r--
            } else if nums[mid] >= nums[0] {
                l = mid + 1
            } else {
                r = mid - 1
            }
            fmt.Println(mid, l, r)
        }

        pivot = l
    }

    binarySearch := func(l, r int) bool {
        for l <= r {
            mid := (l +r) / 2
            if nums[mid] > target {
                r = mid - 1
            } else if nums[mid] < target {
                l = mid + 1
            } else {
                return true
            }
        }

        return false
    }
    fmt.Println(pivot)

    return binarySearch(0, pivot - 1) || binarySearch(pivot, len(nums) - 1)
}