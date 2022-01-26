from sub import f_get_polynomial_degree, f_print_polynomial, ternary_operator


# разбиение уравнения на компоненты типа "+ 2 * x^3"
from test import sqrt_custom


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


# более детальное разбиение уравнения на подкомпоненты типа ['+', '2', '*', 'x^3']
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


# проверка целостности уравнения
def check_structure_x(list):
	# проверка количества элементов с правой стороны от равно и слевой
	l1 = []
	l2 = []
	equals = False
	for l in list:
		if l[0] == '=':
			if not equals:
				equals = True
				continue
			else:
				return 'missing \'=\''

		if equals:
			l2.append(l)
		else:
			l1.append(l)

	if not equals or len(l1) <= 0 or len(l2) <= 0:
		return 'wrong equation'

	# если х без коофициента
	for l in list:
		for s in l:
			if s[0] == 'x' and len(l) <= 2:
				return 'missing coefficient'
	return 'true'


# стартовая сортировка уравнения относительно '='
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
					resS.append([ternary_operator(i[0] == '+', '-', '+'), i[1]])
				else:
					resS.insert(0, i)
		elif len(i) == 3:
			i.insert(0, ternary_operator(equals, '-', '+'))
			resS.append(i)
		else:
			if equals:
				resS.append([ternary_operator(i[0] == '+', '-', '+'), i[1], i[2], i[3]])
			else:
				resS.append(i)

	return resS + resC + resE


# стартовая сортировка уравнения относительно '='
def sort_abc(res):
	# выборка комнопентов типа "x^n"
	check = []
	for i in res:
		if len(i) == 4:
			flag = True
			for c in check:
				if c == i[len(i) - 1]:
					flag = False
			if flag:
				check.append(i[len(i) - 1])

	check.sort()

	# суммирование компонентов если есть похожие
	res2 = []
	for c in check:
		r = summary_components(res, c)
		if r[0] != 'Null':
			res2.append(r)

	return res2


# суммирование коофициентов
def summary_components(res, str):
	temp = []
	for r in res:
		if str == r[len(r) - 1]:
			temp.append(r)

	nums = []
	for t in temp:
		nums.append(float(t[1]) * ternary_operator(t[0] == '+', 1, -1))

	num = ternary_operator(sum(nums) == (int(sum(nums))), int(sum(nums)), sum(nums))
	if num == 0:
		return ["Null"]

	return [ternary_operator(num >= 0, '+', '-'), ternary_operator(num >= 0, num, num * -1), '*', str]


# суммирование всех чисел без и с x^0
def sort_nums(res):
	nums = []
	for i in res:
		if len(i) == 2:
			nums.append(float(i[1]) * ternary_operator(i[0] == '+', 1, -1))

	num = ternary_operator(sum(nums) == (int(sum(nums))), int(sum(nums)), sum(nums))
	if num == 0:
		return []
	return [ternary_operator(num >= 0, '+', '-'), ternary_operator(num >= 0, num, num * -1)]


# объединение буквенных компонентов и чисел
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
		list.insert(0, [s2[0], s2[1], '*', 'x^0'])
	return list


# разбиение компонентов уравнения для сравнения между '='
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


# доп проверки и строки в уравнение для дальнейших расчётов
def algoritm_parser(args):
	# создание компонентов "- 7 * 3x"
	pre_list = parser_v2(args)

	# создания листа подкомпонентов "[-, 7, *, 3x]"
	list = parser_v3(pre_list)

	# добавление x^0 всем значениям без него
	list2 = []
	for c in list:
		if c[0] != '=' and len(c) <= 2:
			c2 = []
			c2.append(c[0])
			if len(c) > 1:
				c2.append(c[1])
			c2.append('*')
			c2.append('x^0')
			list2.append(c2)
		else:
			list2.append(c)
	return list2


# сортировки и пересборки
def algoritm_sort(list):
	# сортировка [x2, x1, x0, =, 100]
	res = start_sort(list)

	# сортировка численных и буквенных элементов
	s1 = sort_abc(res)
	s2 = sort_nums(res)

	# объединение
	res2 = []
	if len(s2) < 2:
		res2 = s1
	else:
		res2 = sum_abc_and_nums(s1, s2)
	if len(res2) == 0:
		res2.append(['+', '0'])
	res2 += ['='], ['+', '0']
	return res2


# проверка сколько разных степеней в уравнении
def check_x(parser):
	res = 0
	for n in parser:
		if len(n) == 4:
			res += 1
	return res


# решение без x^
def solution_x0(parser):
	f = 0
	for n in parser:
		if n[0] == '=':
			break
		f += float(n[1])
	if f != 0:
		return ["incorrect"]
	return ["incorrect"]


# решение с одним x^
def solution_x1(parser):
	c = 0
	b = 0
	a = 0
	flag_c = False
	flag_b = False
	for p in parser:
		if len(p) > 2 and p[len(p) - 1][2] == '0':
			c = get_num_solution(p)
			flag_c = True
		if len(p) > 2 and p[len(p) - 1][2] == '1':
			b = get_num_solution(p)
			flag_b = True
		if len(p) > 2 and p[len(p) - 1][2] == '2':
			a = get_num_solution(p)

	if b != 0:
		return ['The solution is:', '0']
	elif a != 0:
		return get_discriminant(a, b, c)

	return ["incorrect"]


# поиск коофициента компонента
def get_num_solution(p):
	num = 0
	if len(p) == 3:
		num = float(p[0])
	else:
		num = ternary_operator(p[0] == '+', float(p[1]), float(p[1]) * -1)
	return num


# решение с двумя x^
# ax + b = 0
# ax = - b
# x = - b / a
def solution_x2(parser):
	c = 0
	b = 0
	a = 0
	flag_c = False
	flag_b = False
	for p in parser:
		if len(p) > 2 and p[len(p) - 1][2] == '0':
			c = get_num_solution(p)
			flag_c = True
		if len(p) > 2 and p[len(p) - 1][2] == '1':
			b = get_num_solution(p)
			flag_b = True
		if len(p) > 2 and p[len(p) - 1][2] == '2':
			a = get_num_solution(p)

	if flag_c and flag_b:
		x = int(c / b * 100) / 100
		return ['The solution is:', x]

	return get_discriminant(a, b, c)


# вычисление по дискриминанту
def get_discriminant(a, b, c):
	D = b * b - 4 * a * c

	resString = "Discriminant "

	if D < 0:
		sqrt = sqrt_custom(D * -1)

		x1 = -b / (2 * a)
		i1 = -sqrt / (2 * a)
		x2 = -b / (2 * a)
		i2 = sqrt / (2 * a)

		i1 = int(i1 * 100) / 100
		i2 = int(i2 * 100) / 100

		res1 = str(x1) + ' ' + ternary_operator(i1 >= 0, '+', '-') + ' ' + \
			ternary_operator(i1 >= 0, str(i1), str(i1 * -1)) + ' * i'
		res2 = str(x2) + ' ' + ternary_operator(i2 >= 0, '+', '-') + ' ' + \
			ternary_operator(i2 >= 0, str(i2), str(i2 * -1)) + ' * i'
		resString += "< 0, there are 2 solutions(a + b * i): "
		return [resString, res1, res2]
	elif D == 0:
		x = -b / (2 * a)
		resString += "== 0, there are 1 solution: "
		return [resString, x]
	else:
		sqrt = sqrt_custom(D)

		x1 = (-b - sqrt) / (2 * a)
		x2 = (-b + sqrt) / (2 * a)

		x1 = int(x1 * 100) / 100
		x2 = int(x2 * 100) / 100
		resString += "> 0, there are 2 solution: "
		return [resString, x1, x2]


# решение с тремя x^
def solution_x3(parser):
	c = 0
	b = 0
	a = 0
	for p in parser:
		if len(p) > 2 and p[len(p) - 1][2] == '0':
			c = get_num_solution(p)
		if len(p) > 2 and p[len(p) - 1][2] == '1':
			b = get_num_solution(p)
		if len(p) > 2 and p[len(p) - 1][2] == '2':
			a = get_num_solution(p)

	return get_discriminant(a, b, c)


# основная функция алгоритма
def f_algoritm(args):
	list = algoritm_parser(args)
	check = check_structure_x(list)
	if check != 'true':
		print("Error parse: " + check)
		return

	parser = []
	# проверка на совпаддение двух сторон уравнения
	if not check_all_sol(list):
		parser = algoritm_sort(list)
		f_print_polynomial("Reduced form: ", parser)
	else:
		f_print_polynomial("Reduced form: ", list)
		print("Polynomial degree: " + str(f_get_polynomial_degree(list)))
		print("ANY real number is a solution")
		return

	# получаем степень уравнения
	degree = f_get_polynomial_degree(parser)
	print("Polynomial degree: " + str(degree))
	if degree > 2:
		print("The polynomial degree is strictly greater than 2, I CAN'T solve.")
		return

	# решение или фиаско уравнения
	check = check_x(parser)
	sol = []
	if check == 0:
		sol = solution_x0(parser)
	elif check == 1:
		sol = solution_x1(parser)
	elif check == 2:
		sol = solution_x2(parser)
	elif check == 3:
		sol = solution_x3(parser)

	# финальный вывод
	if sol[0] == 'incorrect':
		print("The equation has no solution because it was built INCORRECTLY")
	elif sol[0] == 'no x':
		print("The equation has no UNKNOWN value")
	else:
		for s in sol:
			print(s)
