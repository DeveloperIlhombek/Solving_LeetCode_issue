public class Solution
{
    static void Main(string[] args)
    {
        int[] s = new int[] { 4, 5, 6, 7, 0, 2, 1, 3 };
        string x = RestoreString("codeleet", s);
        Console.WriteLine(x);
    }
    public static string RestoreString(string s, int[] indices)
    {
        int n = indices.Length;
        char[] result = new char[n];
        for (int i = 0; i < n; i++)
        {
            result[indices[i]] = s[i];
        }
        return new string(result);
    }
}