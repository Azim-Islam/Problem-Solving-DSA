using System;

var _ = int.TryParse(Console.ReadLine(), out int testCases);

foreach (var __ in Enumerable.Range(0, testCases))
{
    var n = int.Parse(Console.ReadLine()!);
    var arr = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
    var ans = Enumerable.Range(1, n - 1).Sum(i => arr[i] < arr[0..i].Max() ? 1 : 0);
    Console.WriteLine(ans);   
}