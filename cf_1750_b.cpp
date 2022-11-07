// 2022-11-06
// didn't solve during the contest
// CodeTON problem B

#include <iostream>

#define forn(i, n) for (int i = 0; i < int(n); ++i)

using namespace std;

void solve() 
{
    long long n;
    cin >> n;
       
    unsigned long long inp;
    cin >> inp;

    cout << inp << endl;

    int max_g = 1, cur_g = 1, count_x = 0, count_y = 0;
    int prev, cur;

    prev = inp % 10;

    prev == 0 ? count_x++ : count_y++;
    inp /= 10;

    forn(_, n-1)
    {
        cur = inp % 10;
        // cout << inp << endl;
        inp /= 10;
        cur == 0 ? count_x++ : count_y++;
        if (prev == cur) cur_g++;
        // else 
        // {
        //     // if ((count_x + count_y) == n) cur_g++;
        //     cur_g = 1;
        // }
        if (cur_g > max_g) max_g = cur_g;
        if (prev != cur ) cur_g = 1;
        prev = cur;
        cout << max_g << endl;
    }

    // compute ratio

    cout << count_x << " " << count_y << " " << max_g << "\n";
    cout << max(max_g * max_g, count_x * count_y) << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
