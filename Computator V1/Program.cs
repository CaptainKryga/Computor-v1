using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Computator_V1;

namespace Computator_V1
{
	class Program
	{
		public static List<Number> list = new List<Number>();
		public static double result;
		static void Main(string[] args)
		{
			while (true)
			{
				Parser();

				Algoritm();
				Print();
			}
		}

		public static void Print()
		{
			for (int x = 0; x < list.Count; x++)
			{
				Console.WriteLine("number = " + (list[x].positive ? "+" : "-") + + list[x].number);
			}
			Console.WriteLine("result: " + result);
			list.Clear();
		}

		public static void Algoritm()
		{
			for (int x = 0; x < list.Count; x++)
				result += list[x].number * (list[x].positive ? 1 : -1);
		}

		public static int Parser()
		{
			string str = Console.ReadLine();
			int x = 0;
			if (str == null)
				return 1;
			while (x < str.Length)
			{
				bool positive = true;
				bool xo = false;
				string str2 = str.Substring(x, str.Length - x);
				if (Library.GetSign(str2, out int len, out char ch) == 1)
				{
					if (ch == '-')
						positive = false;
					else
						positive = true;
					x += len;
				}
				str2 = str.Substring(x, str.Length - x);
				double num = Library.AtoiD(str2, out len);
				x += len;
				list.Add(new Number(num, positive, xo, 1));
			}
			return 0;
		}
	}
}
