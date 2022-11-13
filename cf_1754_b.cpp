// https://codeforces.com/problemset/problem/1754/B
// 2022-11-13

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    int n;
    cin >> n;
       
    for (int i = n; i / 2; --i)
    {
       cout << i / 2 << " ";
       
    }
    
    cout << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
