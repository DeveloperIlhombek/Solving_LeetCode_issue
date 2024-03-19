using System.Numerics;

public class Solution
{
    static void Main(string[] args)
    {
        int[] x = new int[] { 9 };
        foreach (int i in PlusOne(x))
        {
            Console.Write(i + "  ");
        }
    }
    public static int[] PlusOne(int[] nums)
    {
        for (int index = nums.Length - 1; index >= 0; index--)
        {
            if (nums[index] < 9)
            {
                nums[index]++;
                return nums;
            }
            nums[index] = 0;
        }
        int[] result = new int[nums.Length + 1];
        result[0] = 1;
        return result;
    }
}