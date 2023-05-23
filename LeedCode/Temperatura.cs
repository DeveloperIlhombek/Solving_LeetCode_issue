public class Program
{
    static void Main(string[] args)
    {
        double[] arr = ConvertTemperature(36.50);
        foreach (double d in arr)
            Console.WriteLine(d + " ");
    }
    public static double[] ConvertTemperature(double celsius)
    {
        double[] temperture = new double[2];
        double kelvin = celsius + 273.15;
        temperture[0] = kelvin;
        double farangeyt = celsius * 1.8 + 32;
        temperture[1] = farangeyt;
        return temperture;
    }

}