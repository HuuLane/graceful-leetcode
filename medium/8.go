func myAtoi(str string) int {
	if str == "" {
		return 0
	}
	const intMax = 1<<31 - 1
	const intMin = - 1 << 31
	const boundary = intMax / 10
	i := 0
	for ; i < len(str); i++ {
		if str[i] != ' ' {
			break
		}
	}
	if i == len(str) {
		return 0
	}
	sign := 1
	if str[i] == '-' {
		sign = -1
		i++
	} else if str[i] == '+' {
		i++
	}
	res := 0
	for ; i < len(str); i++ {
		val := int(str[i] - '0')
		if val < 0 || val > 9 {
			break
		}
		if res > boundary || (res == boundary && val > 7) {
			if sign == 1 {
				return intMax
			} else {
				return intMin
			}
		}

		res = res*10 + val
	}
	return sign * res
}
