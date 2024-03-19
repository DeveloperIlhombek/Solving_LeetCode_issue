public class Solution
{
    static void Main(string[] args)
    {
        int x = ArrangeCoins(2147483647);
        Console.WriteLine(x);

    }
    public static int ArrangeCoins(int n)
    {
        int level = 0, coin = 1;
        while (n >= coin)
        {
            n -= coin;
            coin++;
            level++;
        }
        return level;
    }
}