public class Solution
{
    static void Main(string[] args)
    {
        int x = CountOperations(3, 2);
        Console.WriteLine(x);

    }
    public static int CountOperations(int num1, int num2)
    {
        int count = 0;
        while (num1 != 0 && num2 != 0)
        {
            if (num1 >= num2)
            {
                num1 -= num2;
            }
            else
            {
                num2 -= num1;
            }
            ++count;
        }
        return count;
    }
}