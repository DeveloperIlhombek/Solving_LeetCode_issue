
class Program
{
    static void Main(string[] args)
    {
        int[] arr = new int[] { 1, 2, 3, 1, 2, 3 };
        int k = 2;
        Console.WriteLine(ContainsNearbyDuplicate(arr, k));
    }
    public static bool ContainsNearbyDuplicate(int[] nums, int k)
    {
        int n = nums.Length - 1;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (nums[i] == nums[j] && Math.Abs(j - i) <= k)
                {
                    return false;
                }
            }
        }
        return true;
    }
}


