using System;

int t = int.Parse(Console.ReadLine()!);
while (t-- > 0)
{
    var input = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();
    var (n, k, p, m) = (input[0], input[1], input[2], input[3]);
    var arr = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();
    var dict = new OrderedDictionary<int, int>();

    foreach (var (i, val) in arr.Index())
    {
        dict[i + 1] = val;
    }

    var ans = 0;
    var flag = false;

    while (m >= 0)
    {
        flag = false;
        foreach (var (i, (card, cost)) in dict.Index())
        {
            if (i >= k) break;
            if (card == p && m - cost >= 0)
            {
                ans += 1;
                m -= cost;
                dict.Remove(card);
                flag = true;
                dict[card] = cost;
                break;
            }
        }

        if (!flag)
        {
            int[] maxx = [0, int.MaxValue];
            foreach (var (i, (card, cost)) in dict.Index())
            {
                if (i >= k) break;
                if (maxx[1] > cost)
                {
                    maxx = [card, cost];
                }
            }

            if (maxx[1] <= m)
            {
                m -= maxx[1];
                dict.Remove(maxx[0]);
                dict[maxx[0]] = maxx[1];
            }
            else
            {
                goto breakOut;
            }
        }
    }

    breakOut:
    Console.WriteLine(ans);
}