using System;

namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            int var1 = 3;
            String var2 = "een tekst";
            Console.WriteLine(var2);
            var2 = Console.ReadLine();
            Console.WriteLine(var2);
            Console.WriteLine( var2 + var2 );
            int var3 = Int32.Parse(var2);
            Console.WriteLine(var3 + var3 );
            bereken();
            bereken();
            bereken();
            bereken(45);
            bereken(6);
            String uitkomst = bereken(12);
            Console.WriteLine(uitkomst);
        }
        static void bereken() {
            Console.WriteLine("start met de functie");
            int vartemp = 55;
            Console.WriteLine(vartemp);
            Console.WriteLine("ik ga dit vermenigvuldigen");
            Console.WriteLine(vartemp * vartemp);
        }
        static String bereken(int x)
        {
            Console.WriteLine("start met de functie");
            int vartemp = x;
            Console.WriteLine(vartemp);
            Console.WriteLine("ik ga dit vermenigvuldigen");
            Console.WriteLine(vartemp * vartemp);
            return "maandag";
        }
    }
}
