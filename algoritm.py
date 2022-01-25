import collections

from sub import f_get_polynomial_degree, f_print_polynomial, tolerant
from parser import is_digit2


def parser_v2(args):
	sr = ""
	list = []
	polynomial = args.polynomial.lower()
	for s in polynomial:
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


def check_structure_x(list):
	for l in list:
		for s in l:
			if s[0] == 'x' and len(l) <= 2:
				return False
	return True


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
				if equals:
					resS.append([tolerant(i[0] == '+', '-', '+'), i[1]])
				else:
					resS.insert(0, i)
		elif len(i) == 3:
			i.insert(0, tolerant(equals, '-', '+'))
			resS.append(i)
		else:
			if equals:
				resS.append([tolerant(i[0] == '+', '-', '+'), i[1], i[2], i[3]])
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
		r = algos(res, c)
		if r[0] != 'Null':
			res2.append(r)

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
	if num == 0:
		return ["Null"]

	return [tolerant(num >= 0, '+', '-'), tolerant(num >= 0, num, num * -1), '*', str]


def sort_nums(res):
	# find all different values
	nums = []
	for i in res:
		if len(i) == 2:
			nums.append(float(i[1]) * tolerant(i[0] == '+', 1, -1))

	num = tolerant(sum(nums) == (int(sum(nums))), int(sum(nums)), sum(nums))
	if num == 0:
		return []
	return [tolerant(num >= 0, '+', '-'), tolerant(num >= 0, num, num * -1)]


def sum_abc_and_nums(s1, s2):
	list = []
	is_x = False
	for s in s1:
		if s[len(s) - 1] == 'x^0':
			is_x = True
			f = s2[1]
			f += s[1]
			list.append([s[0], f, s[2], s[3]])
		else:
			list.append(s)
	if not is_x:
		list.append([s2[0], s2[1], '*', 'x^0'])
	return list


def check_all_sol(list):
	equals = False
	l1 = []
	l2 = []
	for s in list:
		if s[0] == '=':
			equals = True
		elif equals:
			l2.append(s)
		elif not equals:
			l1.append(s)

	if len(l1) == len(l2):
		i = len(l1) - 1
		while i >= 0:
			if l1[i] != l2[i]:
				return False
			i -= 1
		return True
	return False

def algoritm_parser(args):
	# create component's list "- 7 * 3x"
	pre_list = parser_v2(args)

	# create sub component's list "[-, 7, *, 3x]"
	list = parser_v3(pre_list)
	return list


def algoritm_sort(list):
	# first sort elements [x2, x1, x0, =, 100]
	res = start_sort(list)

	# sum sort elements [x2, x1, x0, =, 100]
	s1 = sort_abc(res)
	s2 = sort_nums(res)

	res2 = []
	if len(s2) < 2:
		res2 = s1
	else:
		res2 = sum_abc_and_nums(s1, s2)
	res2 += ['='], ['+', '0']
	return res2


def get_num_in_x(parser, x):
	for n in parser:
		if n[len(n) - 1] == x:
			return n[1]
		else:
			return False


# поверка можно ли решить уравнение
def algoritm_check_discriminant(parser):
	a = get_num_in_x(parser, 'x^0')


def check_x(parser):
	res = 0
	for n in parser:
		if len(n) == 4:
			res += 1
	return res


def solution_x0(parser):
	f = 0
	for n in parser:
		if n[0] == '=':
			break
		f += float(n[1])
	if f != 0:
		return ["false"]
	return ["no x"]


def solution_x1(parser):
	return ["all"]


def solution_x2(parser):
	x = 2
	return ['c']


def f_algoritm(args):
	list = algoritm_parser(args)
	if not check_structure_x(list):
		print("Error parse: X has no coefficient")
		return

	parser = []
	if not check_all_sol(list):
		parser = algoritm_sort(list)
		f_print_polynomial("Reduced form: ", parser)
	else:
		f_print_polynomial("Reduced form: ", list)
		print("Polynomial degree: " + str(f_get_polynomial_degree(args)))
		print("ANY real number is a solution")
		return

	degree = f_get_polynomial_degree(parser)
	print("Polynomial degree: " + str(degree))
	if degree > 2:
		print("The polynomial degree is strictly greater than 2, I CAN'T solve.")
		return

	check = check_x(parser)
	sol = []
	if check == 0:
		sol = solution_x0(parser)
	elif check == 1:
		sol = solution_x1(parser)
	elif check == 2:
		sol = solution_x2(parser)

	if sol[0] == 'false':
		print("The equation has no solution because it was built INCORRECTLY")
	elif sol[0] == 'no x':
		print("The equation has no UNKNOWN value")
	elif sol[0] == 'all':
		print()

	algoritm_check_discriminant(parser)

