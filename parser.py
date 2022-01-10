def is_digit(s):
	return s.isdigit()


def s_parser(args):
	arr = str.split(args.polynomial)
	print(arr)
	for s in arr:
		if not s.isdigit():
			if s != '+' and s != '-' and s != "*" and s != "/" and s != "=":
				if len(s) < 3 or s[0] != 'X' or s[1] != '^' or not is_digit(str.split(s, '^')[1]):
					return [s]

	print("parser\n")
	array = args.polynomial
	return ["true"] + array