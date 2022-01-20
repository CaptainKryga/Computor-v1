import argparse

from algoritm import f_algoritm
from get import f_get_data, f_get_polynomial_degree
from parser import f_parser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('polynomial', type=str, help="polynomial input")
	parser.add_argument("-f", "--free", help="free input mode",
						action="store_true")
	parser.add_argument("-s", "--steps", help="all steps mode",
						action="store_true")
	args = parser.parse_args()
	arr = f_parser(args)
	if arr == "true":
		f_algoritm(args)
	else:
		print("error polynomial: ", str(arr))
