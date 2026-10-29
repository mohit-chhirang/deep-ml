def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	ans = []
	for i in range(len(a)) :
		if(len(a[i]) != len(b)) :
			ans.append(-1)
			continue
		x = 0
		for j in range(len(b)) :
			x += a[i][j] * b[j]
		ans.append(x)
	return ans
