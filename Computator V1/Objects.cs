using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Computator_V1
{
	class Number
	{
		public double number;
		public bool positive;
		public bool x;
		public int power;
		public Number(double number, bool positive, bool x, int power)
		{
			this.number = number;
			this.positive = positive;
			this.x = x;
			this.power = power;
		}
	}
}
