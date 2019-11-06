using System;

namespace Computator_V1
{
	public static class Library
	{
		public static double AtoiD(string str, out int len)
		{
			double result = 0;
			int x = 0;
			int xx = 0;
			while (x < str.Length && str[x] == ' ' || str[x] == '\t')
				x++;
			int znak = str[x] == '-' ? -1 : 1;
			x += str[x] == '-' ? 1 : 0;
			while (x < str.Length && str[x] == ' ')
				x++;
			while (x < str.Length && str[x] != '.' && str[x] >= '0' && str[x] <= '9')
				result = result * 10 + (str[x++] - '0');
			if (x < str.Length)
				x += ((str[x] == '.') ? 1 : 0);
			while (x + xx < str.Length && (str[x + xx] >= '0' && str[x + xx] <= '9'))
				result = result * 10 + (str[x + xx++] - '0');
			len = x + xx;
			while (xx-- > 0)
				result /= 10;
			return result;
		}

		public static int GetSign(string str, out int len, out char ch)
		{
			int x = 0;

			ch = ' ';
			x++;
			if (str[x] == '-' || str[x] == '+' || str[x] == '/' || str[x] == '*' || str[x] == '(' || str[x] == ')')
			{
				len = 2;
				ch = str[x];
				return 1;
			}
			len = 0;
			return 0;
		}
	}
}
