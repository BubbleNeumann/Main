// 2022-11-12
// Codeforces Round # 833 (Div. 2) 
// problem A

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    long int n; // number of blocks
    cin >> n;
    cout << n / 2 + n % 2 << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
