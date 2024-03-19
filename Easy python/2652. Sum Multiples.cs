public class Solution
{
    public int SumOfMultiples(int n)
    {
        int[] arr = new int[n + 1];
        int count = 0;
        for (int i = 1; i <= n; i++)
        {
            arr[i] = i;
            if (arr[i] % 3 == 0 || arr[i] % 5 == 0 || arr[i] % 7 == 0)
            {
                count += arr[i];
            }
        }
        return count;
    }
}