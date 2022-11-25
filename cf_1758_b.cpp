// 2022-11-25
// Codeforces Round # 836 (Div. 2) 
// problem B

#include <iostream>
#include <string>
#include <math.h>

using namespace std;

void solve() 
{
    int n; // len
    cin >> n;


    // first num random ?

    // n % 2 ? n = 1 : n = 0;

    // if (!n % 2) 
    // {
    //     while (n--) cout << 69 << ' ';
    // }
    // else 
    // {
    //     while (n-- != 1) cout << 69 << ' ';
    //     cout << 0;
    // }

    // if (n == 1) cout << 2 << " " << 1;
    // if (n == 0) cout << 1;


    unsigned long long int res = 0;
    unsigned long long int two_pow = 0;
    

    for (int i = 0; i < n; ++i)
    {
        two_pow = pow(2, i);
        // cout << ((two_pow ^ n) & (two_pow*2-1)) << ' ';
        cout << (two_pow ^ n) % two_pow*2 << ' ';
        // res += ((two_pow ^ n) & (two_pow*2-1));
        res += (two_pow ^ n) % two_pow*2;
    }

    // int printed = 0;
    // int power = 0;
    // while (printed != n)
    // {
    //     two_pow = pow(2, power);
    //     two_pow =  ((two_pow ^ n) & (two_pow*2-1));
    //     if (two_pow)
    //     {
    //         cout << two_pow << ' ';
    //         res += two_pow;
    //         ++power;
    //         ++printed;
    //     }
    // }
    
    // cout << (res ^ n) ;
    cout << '\n';

    
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}

