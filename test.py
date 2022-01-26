import argparse

from sub import sqrt_custom


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('s', type=str, help="s square")
	args = parser.parse_args()

	sqrt_custom(float(args.s))
