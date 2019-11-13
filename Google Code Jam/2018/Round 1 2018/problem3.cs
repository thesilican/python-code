using System;

class Solution
{
    static void Main()
    {
        var numCases = int.Parse(Console.ReadLine());
        for (int cases = 0; cases < numCases; cases++)
        {
            var strs = Console.ReadLine().Split(' ');
            var n = int.Parse(strs[0]);
            var p = int.Parse(strs[1]);

            int total = 0;
            for (int i = 0; i < n; i++)
            {
                var strs_ = Console.ReadLine().Split(' ');
                var w = int.Parse(strs_[0]);
                var h = int.Parse(strs_[1]);

                total += (2 * w) + (2 * h) + (2.0 * Math.Sqrt(Math.Pow(w,2), Math.Pow(h,2)));
            }

            Console.WriteLine($"Case #{cases + 1}: {Math.Min(total, p)}");
        }
    }
}