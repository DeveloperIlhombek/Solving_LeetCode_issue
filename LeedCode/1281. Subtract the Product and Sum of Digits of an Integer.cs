public class Solution
{
    static void Main(string[] args)
    {
        int d = SubtractProductAndSum(4421);
        Console.WriteLine(d);
    }
    public static int SubtractProductAndSum(int n)
    {
        int i = 0, count = 0, multi = 1;
        int strs = n.ToString().Length;
        int[] nums = new int[strs];
        while (i < strs)
        {
            nums[i] = n % 10;
            n = n / 10;
            count += nums[i];
            multi *= nums[i];
            i++;
        }
        return multi - count;
    }
}