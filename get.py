def f_get_data(args):
	return str.split(args.polynomial, ' ')


def f_get_polynomial_degree(args):
	res = 0
	arr = str.split(args.polynomial, ' ')
	for s in arr:
		if len(str.split(s, '^')) > 1:
			temp = int(str.split(s, '^')[1])
			if res < temp:
				res = temp
	return res
