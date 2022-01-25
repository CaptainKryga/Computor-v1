import argparse

from sub import ternary_operator


def mabs(x):
	return ternary_operator(x < 0, -x, x)

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
		if i > 100000:
			break

	return sub


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('s', type=str, help="s square")
	args = parser.parse_args()

	sqrt_custom(float(args.s))





	# rootDegree = 2
	#
	# eps = 0.01  # допустимая погрешность double
	# root = num / rootDegree  # начальное приближение корня double
	# rn = num  # значение корня последовательным делением
	# countiter = 0  # число итераций
	#
	# while mabs(root - rn) >= eps:
	# 	rn = num
	# 	i = 0
	# 	while i < rootDegree:
	# 		rn = rn / root
	# 		i += 1
	# 	root = 0.5 * (rn + root)
	# 	countiter += 1
	#
	# 	print(countiter, "|", root)
