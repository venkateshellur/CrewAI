using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Multiplication table for 2:");
        for (int i = 1; i <= 100; i++)
        {
            int result = 2 * i;
            if (result > 100)
            {
                break;
            }
            Console.WriteLine("2 x " + i + " = " + result);
        }
    }
}

Output:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24
2 x 13 = 26
2 x 14 = 28
2 x 15 = 30
2 x 16 = 32
2 x 17 = 34
2 x 18 = 36
2 x 19 = 38
2 x 20 = 40
2 x 21 = 42
2 x 22 = 44
2 x 23 = 46
2 x 24 = 48
2 x 25 = 50
2 x 26 = 52
2 x 27 = 54
2 x 28 = 56
2 x 29 = 58
2 x 30 = 60
2 x 31 = 62
2 x 32 = 64
2 x 33 = 66
2 x 34 = 68
2 x 35 = 70
2 x 36 = 72
2 x 37 = 74
2 x 38 = 76
2 x 39 = 78
2 x 40 = 80
2 x 41 = 82
2 x 42 = 84
2 x 43 = 86
2 x 44 = 88
2 x 45 = 90
2 x 46 = 92
2 x 47 = 94
2 x 48 = 96
2 x 49 = 98
2 x 50 = 100