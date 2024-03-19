public class Solution
{
    static void Main(string[] args)
    {
        string x = DefangIPaddr("1.1.1.1");
        Console.WriteLine(x);
    }
    public static string DefangIPaddr(string address)
    {
        string[] strings = address.Split('.');
        int c = strings.Length;
        string result = "";

        for (int i = 0; i < strings.Length - 1; i++)
        {
            result += strings[i] + "[.]";
        }
        result += strings[c - 1];

        return result;
    }
}