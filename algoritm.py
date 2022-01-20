from get import f_get_polynomial_degree
from parser import is_digit2


def parser_v2(args):
	sr = ""
	list = []
	for s in args.polynomial:
		if s == '-' or s == '+' or s == '=':
			list.append(sr)
			sr = ""

		if s == '=':
			list.append(s)
		else:
			sr += s

	list.append(sr)

	return list


def parser_v3(pre_list):
	list = []
	for l in pre_list:
		temp = str.split(l, ' ')
		i = temp.count('')
		while i > 0:
			i -= 1
			temp.remove('')
		list.append(temp)
	return list


def start_sort(list):
	resS = []
	resE = []
	resC = []
	equals = False
	for i in list:
		if len(i) == 1:
			resC.append(i)
			equals = True
		elif 2 >= len(i) > 1:
			if equals:
				resS.insert(0, i)
			else:
				if equals:
					resS.append(i)
				else:
					resE.append(i)
		else:
			if equals:
				resE.append(i)
			else:
				resS.append(i)

	return resS + resC + resE


def f_algoritm(args):
	check = "-+*"
	arr = str.split(args.polynomial, ' ')

	pre_list = parser_v2(args)
	list = parser_v3(pre_list)
	res = start_sort(list)

	print(res)

	equals = False
	for c in arr:

		if c == '=':
			equals = True
		elif is_digit2(c):
			float(c)

	print("Polynomial degree: " + str(f_get_polynomial_degree(args)))
