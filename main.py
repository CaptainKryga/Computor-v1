import argparse

from algoritm import s_algoritm
from parser import s_parser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('polynomial', type=str, help="polynomial input")
	parser.add_argument("-f", "--free", help="free input mode",
						action="store_true")
	parser.add_argument("-s", "--steps", help="all steps mode",
						action="store_true")
	args = parser.parse_args()
	arr = s_parser(args)
	if arr[0] == "true":
		print(s_algoritm(arr))
	else:
		print("error polynomial: ", str(arr[0]))
