func search(nums []int, target int) int {
    if len(nums) == 0 {
        return -1
    }
    l, r := 0, len(nums) - 1

    if nums[0] < nums[len(nums) - 1] {
        // not rotated, perform binary search
        fmt.Println("not rotated, perform binary search")
        for l <= r {
            mid := (l + r) / 2
            if nums[mid] < target {
                l = mid + 1
            } else if nums[mid] > target {
                r = mid - 1
            } else {
                return mid
            }
        }

        return -1
    }
    if target == nums[0] {
        return 0
    }

    if target > nums [0] {
        // in first segment
        fmt.Println("in first segment")
        for l <= r {
            mid := (l + r) / 2
            if nums[mid] < target {
                if nums[mid] >= nums[0] {
                    l = mid + 1
                } else {
                    r = mid - 1
                }
            } else if nums[mid] > target {
                r = mid - 1
            } else {
                return mid
            }
        }

        return -1
    }

    // in second segment
    fmt.Println("in second segment")
    for l <= r {
        mid := (l + r) / 2
        if nums[mid] < target {
            l = mid + 1
        } else if nums[mid] > target {
            if nums[mid] < nums[0] {
                r = mid - 1
            } else {
                l = mid + 1
            }
        } else {
            return mid
        }
    }

    return -1
}
