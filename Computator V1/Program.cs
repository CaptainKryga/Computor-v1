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
				Console.WriteLine("number = " + list[x].number);
			}
			list.Clear();
		}

		public static void Algoritm()
		{

		}

		public static int Parser()
		{
			string str = Console.ReadLine();
			int x = 0;
			if (str == null)
				return 1;

			while (x < str.Length)
			{
				string str2 = str.Substring(x, str.Length - x);
				double num = Library.AtoiD(str2, out int len);
				x += len;
				list.Add(new Number(num, true, false, 1));
			}
			return 0;
		}
	}
}
