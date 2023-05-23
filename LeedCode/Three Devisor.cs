public class Solution
{
    static void Main()
    {
        bool result = IsThree(12);
        Console.WriteLine(result);
    }
    public static bool IsThree(int n)
    {
        int[] arr = new int[n];
        int i = 0;
        int count = 0;
        while (i < n)
        {
            arr[i] = i + 1;
            i++;
        }
        for (int j = 0; j < n; j++)
        {
            if (n % arr[j] == 0)
                count++;
        }
        if (count == 2)
        {
            return true;
        }
        return false;
    }
}