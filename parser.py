def get_num(num):
	return float(num)

def is_digit2(num):
	check = "0123456789"
	tchk = True
	# if num[0] == '-':
	# 	num = num[1:]
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


def is_digit(s):
	if s[0] == 'x' or s[0] == 'X':
		if len(s) > 2 and s[1] == '^':
			if is_digit2(str.split(s, '^')[1]) and \
				get_num(str.split(s, '^')[1]) == 0 or \
				get_num(str.split(s, '^')[1]) == 1 or \
				get_num(str.split(s, '^')[1]) == 2:
				return True
	elif is_digit2(s):
		return True
	return False


# check symbols
def check_chars(arr):
	check_list = "0123456789+-*/=^ Xx."

	for c in arr:
		flag = False
		for c2 in check_list:
			if c == c2:
				flag = True

		if not flag:
			return c

	return "true"


# check iterations
def check_iterations(arr):
	iter = 0
	print(arr)
	for word in arr:
		if iter == 0 or iter % 2 == 0:
			if not is_digit(word):
				return word
		elif word != '+' and word != '-' and word != '*' and word != '/' and word != '=':
			return word
		iter += 1

	return "true"


# check variables
def check_variables():
	print("")


def f_parser(args):
	check = check_chars(args.polynomial)
	if check != "true":
		return check

	check = check_iterations(str.split(args.polynomial))
	if check != "true":
		return check

	print("parser\n")
	return "true"
