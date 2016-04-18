import numpy as np

def get_next(n,k):
	assert k <= n + 1e-5
	if 2*k > n:
		k = n - (2*k - n) + 1
	else:
		k = 2*k
	return k

def trace_loop(n,k0=1):
	k = np.zeros(n)
	k[0] = k0
	for i in range(1,n):
		k[i] = get_next(n,k[i-1])
	return np.unique(k).size == n and get_next(n,k[n-1]) == k0
