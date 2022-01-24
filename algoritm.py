from sub import f_get_polynomial_degree, f_print_polynomial, tolerant
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
		if len(temp) > 0:
			list.append(temp)
	return list


def start_sort(list):
	resS = []
	resE = []
	resC = []
	equals = False
	for i in list:
		if len(i) == 1:
			if i[0] == '=':
				resC.append(i)
				equals = True
			else:
				i.insert(0, '+')
				resE.insert(0, i)
		elif len(i) == 2:
			if i[1] != '0':
				resS.insert(0, i)
		elif len(i) == 3:
			i.insert(0, '+')
			resS.append(i)
		else:
			resS.append(i)

	return resS + resC + resE


def sort_abc(res):
	# find all different values
	check = []
	for i in res:
		if len(i) == 4:
			flag = True
			for c in check:
				if c == i[len(i) - 1]:
					flag = False
			if flag:
				check.append(i[len(i) - 1])

	# destroy duplicate's
	check.sort()
	# check.reverse()

	# sum values on check
	res2 = []
	for c in check:
		res2.append(algos(res, c))
	return res2


def algos(res, str):
	temp = []
	for r in res:
		if str == r[len(r) - 1]:
			temp.append(r)

	nums = []
	for t in temp:
		nums.append(float(t[1]) * tolerant(t[0] == '+', 1, -1))

	num = tolerant(sum(nums) == (int(sum(nums))), int(sum(nums)), sum(nums))
	return [tolerant(num >= 0, '+', '-'), tolerant(num >= 0, num, num * -1), '*', str]


def sort_nums(res):
	# find all different values
	nums = []
	for i in res:
		if len(i) == 2:
			nums.append(float(i[1]) * tolerant(i[0] == '+', 1, -1))

	num = tolerant(sum(nums) == (int(sum(nums))), int(sum(nums)), sum(nums))
	return [tolerant(num >= 0, '+', '-'), tolerant(num >= 0, num, num * -1)]


def algoritm_parser(args):
	# create component's list "- 7 * 3x"
	pre_list = parser_v2(args)
	# create sub component's list "[-, 7, *, 3x]"
	list = parser_v3(pre_list)
	# first sort elements [x2, x1, x0, =, 100]
	res = start_sort(list)
	# sum sort elements [x2, x1, x0, =, 100]
	res2 = sort_abc(res)

	# res2

	res2 += sort_nums(res), ['='], ['+', '0']
	return res2


# поверка можно ли решить уравнение
def algoritm_check_discriminant(parser):
	i = 0


def f_algoritm(args):
	parser = algoritm_parser(args)
	f_print_polynomial("Reduced form: ", parser)

	degree = f_get_polynomial_degree(args)
	print("Polynomial degree: " + str(degree))
	if degree > 2:
		print("The polynomial degree is strictly greater than 2, I can't solve.")
		return

	algoritm_check_discriminant(parser)

