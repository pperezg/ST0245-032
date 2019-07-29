def gcd_euclid(p, q):
	r = p % q
	if r == 0:
		return q
	else:
		return gcd_euclid(q, r)

print(gcd_euclid(60, 48))
