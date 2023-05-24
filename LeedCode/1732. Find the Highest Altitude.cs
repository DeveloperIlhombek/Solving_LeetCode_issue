public class Solution
{
    static void Main(string[] args)
    {
        //Input: gain = [-5,1,5,0,-7]
        //Output: 1
        int x = LargestAltitude(new int[] { -5, 1, 5, 0, -7 });
        Console.WriteLine(x);
    }
    public static int LargestAltitude(int[] gain)
    {
        int[] arr = new int[gain.Length];
        int count = 0, k = 0;
        for (int i = 0; i < gain.Length; i++)
        {
            count += gain[i];
            arr[i] = count;
            k = Math.Max(k, arr[i]);
        }
        if (k > 0)
            return k;

        return 0;
    }
}