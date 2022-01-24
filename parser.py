# check num or not num
def is_digit2(num):
	check = "0123456789"
	tchk = True
	for c in num:
		flag = False
		for ch in check:
			if c == ch:
				flag = True
		if c == '.' and tchk:
			tchk = False
			flag = True

		if not flag:
			return False
	return True

# pre check num, check x^
def is_digit(s):
	if s[0] == 'x' or s[0] == 'X':
		if len(s) > 2 and s[1] == '^':
			if is_digit2(str.split(s, '^')[1]):
				return True
	elif is_digit2(s):
		return True
	return False


# check symbols
def check_chars(arr):
	check_list = "0123456789+-*=^ Xx."
	equals = False

	for c in arr:
		flag = False
		if c == '=':
			if not equals:
				equals = True
			else:
				return c
		for c2 in check_list:
			if c == c2:
				flag = True

		if not flag:
			return c

	return "true"


# check iterations
def check_iterations(arr):
	iter = 0
	is_num = False
	if arr[0] == '-':
		is_num = True
	for word in arr:
		if is_num:
			if word != '+' and word != '-' and word != '*' and word != '/' and word != '=':
				return word
			is_num = False
		else:
			if not is_digit(word):
				return word
			is_num = True
		iter += 1

	return "true"


def f_parser(args):
	check = check_chars(args.polynomial)
	if check != "true":
		return check

	check = check_iterations(str.split(args.polynomial))
	if check != "true":
		return check

	return "true"
