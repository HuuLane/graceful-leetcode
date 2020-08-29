func reversePairs(nums []int) int {
	n := len(nums)
	tmp := make([]int, n)
	count := 0
	merge := func(low, mid, high int) {
		i, j := low, mid+1
		// copy to tmp at first, then write back the order
		for k := low; k <= high; k++ {
			tmp[k] = nums[k]
		}
		for k := low; k <= high; k++ {
			switch {
			case i > mid:
				nums[k] = tmp[j]
				j++
			case j > high:
				nums[k] = tmp[i]
				i++
			case tmp[i] > tmp[j]:
				nums[k] = nums[j]
				count += mid + 1 - i
				j++
			default:
				nums[k] = tmp[i]
				i++
			}
		}
	}
	var mergesort func(int, int)
	mergesort = func(low, high int) {
		if high <= low {
			return
		}
		mid := (low + high) / 2
		mergesort(low, mid)
		mergesort(mid+1, high)
		merge(low, mid, high)
	}
	mergesort(0, n-1)
	return count
}
