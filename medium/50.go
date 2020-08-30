func myPow(x float64, n int) float64 {
	isFraction := false
	if n < 0 {
		isFraction = true
		n = -n
	}
	var pow func(float64, int) float64
	pow = func(x float64, n int) float64 {
		if n == 0 {
			return 1
		}
		if n == 1 {
			return x
		}
		r := pow(x, n/2)
		if n%2 == 0 {
			return r * r
		}
		return r * r * x
	}
	r := pow(x, n)
	if isFraction {
		return 1 / r
	}
	return r
}
