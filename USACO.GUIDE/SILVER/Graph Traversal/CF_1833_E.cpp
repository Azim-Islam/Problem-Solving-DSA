#include <bits/stdc++.h>

using namespace std;

typedef int ll;

int main()
{
    ll t;
    scanf("%d", &t);
    while (t--)
    {
        ll n;
        scanf("%d", &n);
        vector<ll> arr(n);
        vector<vector<ll>> components;
        vector<set<ll>> adj(n);
        // vector<ll> visited(n);
        for (ll i = 0; i < n; i++)
        {
            scanf("%d", &arr[i]);
            arr[i] -= 1;
        }
        for (ll i = 0; i < n; i++)
        {
            adj[i].insert(arr[i]);
            adj[arr[i]].insert(i);
        }

        vector<int> vis(n);
        for (ll i = 0; i < n; i++)
        {
            if (!vis[i])
            {
                vector<ll> ss = {i};
                vis[i] = 1;
                components.push_back({i});
                while (ss.size())
                {
                    ll v = ss.back();
                    ss.pop_back();
                    for (auto nn : adj[v])
                    {
                        if (!vis[nn])
                        {
                            ss.push_back(nn);
                            vis[nn] = 1;
                            components.back().push_back(nn);
                        }
                    }
                }
            }
        }
        ll ans_min = 0, ans_max = 0, extras = 0;
        for (auto cmp : components)
        {
            if (cmp.size())
            {
                ans_max += 1;
                ll tt = 0;
                for (auto v : cmp)
                {
                    if (adj[v].size() < 2)
                    {
                        tt += 1;
                    }
                }
                if (extras > 0 && tt > 0)
                {
                    ans_min += 1;
                    extras -= 1;
                    tt -= 1;
                    extras += tt;
                }
                else
                {
                    extras += tt;
                }
            }
        }
        printf("%d %d\n", ans_max - ans_min, ans_max);
        // print_comp(components);
    }
    return 0;
}