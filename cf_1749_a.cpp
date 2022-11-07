// 2022-11-06

#include <iostream>

#define forn(i, n) for (int i = 0; i < int(n); ++i)

using namespace std;

void solve() 
{
    int n, m;
    cin >> n >> m;
    forn(_, m)
    {
        int x, y;
        cin >> x >> y;
    }
    
    n > m ? cout << "YES\n" : cout << "NO\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
