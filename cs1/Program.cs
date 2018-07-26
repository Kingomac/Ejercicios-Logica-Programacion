using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*
SILENCIO. Si Ángela habla más bajo que Rosa y Celia habla más alto que Rosa,
¿habla Ángela más alto o más bajo que Celia?
C
R
A
 */
namespace cs1
{
    class Program
    {
        public static int C, R, A;
        static void Main(string[] args)
        {
            while (!Comprobar())
            {
                var numb = new Random();
                C = numb.Next(0, 3);
                R = numb.Next(0, 3);
                A = numb.Next(0, 3);
                Console.WriteLine("-------------------");
                Console.WriteLine($"Ángela: {A}");
                Console.WriteLine($"Rosa: {R}");
                Console.WriteLine($"Celia: {C}");
            }
            Console.WriteLine("*************");
            Console.Write("Ángela habla más bajo que Celia");
            Console.ReadKey();
        }
        public static bool Comprobar()
        {
            if (A < R && C > R) return true;
            else return false;
        }
    }
}
