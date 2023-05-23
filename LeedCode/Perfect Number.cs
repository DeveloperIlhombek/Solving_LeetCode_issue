﻿public class Solution
{
    static void Main(string[] args)
    {
        bool result = CheckPerfectNumber(28);
        Console.WriteLine(result);

    }
    public static bool CheckPerfectNumber(int num)
    {
        if (num <= 1)
            return false;

        int sum = 1;
        for (int i = 2; i * i < num; i++)
        {
            if (num % i == 0)
            {
                sum += i;
                if (num / i != i)
                    sum += num / i;
            }
        }
        return num.Equals(sum);
    }
}