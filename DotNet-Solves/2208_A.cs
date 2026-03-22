using System;

int t = int.Parse(Console.ReadLine()!);
while (t-- > 0)
{
    var input = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();
    var (n, k, p, m) = (input[0], input[1], input[2], input[3]);
    var arr = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();
    var LL = new LinkedList<(int, int)>();
    var ans = 0;
    foreach (var (i, val) in arr.Index())
    {
        LL.AddLast((i + 1, val));
    }

    while (m >= 0)
    {
        var node = LL.First!;
        for (var i = 0; i < k; i++)
        {
            if (node.Value.Item1 == p && node.Value.Item2 <= m)
            {
                ans += 1;
                m -= node.Value.Item2;
                LL.Remove(node);
                LL.AddLast(node);
                break;
            }

            node = node.Next;

            if (i == k - 1)
            {
                var lowestNode = LL.First!;
                var node1 = LL.First!;
                for (var j = 0; j < k; j++)
                {
                    if (node1.Value.Item2 < lowestNode.Value.Item2)
                    {
                        lowestNode = node1;
                    }
                    node1 = node1.Next!;
                }
                LL.Remove(lowestNode);
                LL.AddLast(lowestNode);

                if (lowestNode.Value.Item2 <= m)
                {
                    m -= lowestNode.Value.Item2;
                }
                else
                {
                    goto printAns;
                }
            }
        }
    }
    printAns:
    Console.WriteLine(ans);
}