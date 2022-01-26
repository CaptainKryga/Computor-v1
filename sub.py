# получение степени уравнения
def f_get_polynomial_degree(list):
	res = 0
	for l in list:
		if len(l) > 2 and (l[len(l) - 1][0] == 'x' or l[len(l) - 1][0] == 'X'):
			temp = int(l[len(l) - 1][2:])
			res = ternary_operator(temp > res, temp, res)
	return res


# принт уравнения из листа компонентов
def f_print_polynomial(start, src):
	first = True
	equals = False
	res = ""
	for s in src:
		if first or equals:
			x = ternary_operator(s[0] == '+', s[1:], s)

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


# тернарное выражение
def ternary_operator(check, ret1, ret2):
	if check:
		return ret1
	return ret2


# пародия на sqrt
def sqrt_custom(num):
	sub = num / 4
	koof = 0.001
	i = 1
	_max = -999999999
	_min = 999999999
	while True:
		res = sub * sub
		# print(int(sub * 1000) / 1000, "|", int(res * 1000) / 1000, "|", i, "[", int(_min * 100) / 100, "|",
		# 	  int(_max * 100) / 100, "]")
		if res - koof < num < res + koof:
			break

		if res > num:
			_min = ternary_operator(sub < _min, sub, _min)
			sub -= sub / 10
			while sub > _min:
				sub -= sub / 250
		elif res < num:
			_max = ternary_operator(sub > _max, sub, _max)
			sub += sub / 10
			while sub < _max:
				sub += sub / 250
		i += 1
		if i > 10000000:
			# print("erebor")
			break

	return int(sub * 100) / 100
