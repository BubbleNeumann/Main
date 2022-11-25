// 2022-11-25
// Codeforces Round # 836 (Div. 2) 
// problem A

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    // long int n; // number of blocks
    // cin >> n;
    string inp;
    cin >> inp;


    string copy = inp + inp;

    int len = inp.length();

    for (int i = 0; i < len; ++i)
    {
        copy[i] = inp[i];
        copy[2*len-i-1] = inp[i];
    }

    cout << copy << '\n';
    
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
