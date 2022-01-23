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

def f_print_polynomial(start, src):
	first = True
	equals = False
	res = ""
	for s in src:
		if first or equals:
			x = tolerant(s[0] == '+', s[1:], s)

			for c in x:
				res += str(c) + ' '
			if first:
				first = False
			elif equals:
				equals = False
		elif s[0] == '=':
			equals = True
			res += s[0] + ' '
		else:
			for c in s:
				res += str(c) + ' '
	print(start + res[:-1])

def tolerant(check, ret1, ret2):
	if check:
		return ret1
	return ret2
