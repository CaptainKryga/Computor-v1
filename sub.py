# получение степени уравнения
def f_get_polynomial_degree(list):
	res = 0
	for l in list:
		if len(l) > 2 and (l[len(l) - 1][0] == 'x' or l[len(l) - 1][0] == 'X'):
			temp = int(l[len(l) - 1][2:])
			res = tolerant(temp > res, temp, res)
	return res


# принт уравнения из листа компонентов
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


# тернарное выражение
def tolerant(check, ret1, ret2):
	if check:
		return ret1
	return ret2
