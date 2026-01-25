using System;

var _ = int.TryParse(Console.ReadLine(), out int test_cases);

foreach (var __ in Enumerable.Range(0, test_cases))
{
    var n = int.Parse(Console.ReadLine());
    var ans = 0;
    var arr = Console.ReadLine().Split().Select(int.Parse).ToArray();
    foreach (var i in Enumerable.Range(1, n-1))
    {
        ans += arr[i] > arr[0..i].Max() ? 0 : 1;
    }
    Console.WriteLine(ans);   
}