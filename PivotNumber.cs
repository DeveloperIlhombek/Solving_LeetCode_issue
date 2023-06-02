public class Solution
{
    static void Main()
    {
        int x = PivotInteger(6);
        Console.WriteLine(x);
    }
    public static int PivotInteger(int n)
    {
        int x = (n * n + n) / 2;
        int y = (int)Math.Sqrt(x);
        return y * y == x ? y : -1;
    }
}