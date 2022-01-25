import argparse

from algoritm import f_algoritm
from parser import f_parser

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('polynomial', type=str, help="polynomial input")
	# parser.add_argument("-f", "--free", help="free input mode",
	# 					action="store_true")
	# parser.add_argument("-s", "--steps", help="all steps mode",
	# 					action="store_true")
	args = parser.parse_args()
	if len(args.polynomial) == 0:
		print("Error parse: empty line ")
	else:
		arr = f_parser(args)
		if arr == "true":
			f_algoritm(args)
		else:
			print("Error parse: symbol ", str(arr))
