// 2022-11-19
// Div.3 problem C

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    int l, r, x, a, b, ans = -1;
    cin >> l >> r >> x >> a >> b;
    
    if (b < l || b > r) { cout << -1; return; }
    if (a == b) { cout << 0; return; }
    if (abs(a - b) >= x) { cout << 1; return; }
    
    



}

int main() 
{
    int t;
    scanf("%d", &t);
    while (t--) solve();
    return 0;
}


