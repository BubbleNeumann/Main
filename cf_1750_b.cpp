// 2022-11-06
// didn't solve during the contest
// CodeTON problem B

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    long long int n;
    cin >> n;
       
    string inp;
    cin >> inp;

    long long int max_g = 1, cur_g = 1, count_x = 0, count_y = 0;
    int prev, cur;
    
    prev = inp.at(0) == '1';
    prev == 0 ? count_x++ : count_y++;

    for (int i = 1; i < n; ++i)
    {
        cur = inp.at(i) == '1';
        cur == 0 ? count_x++ : count_y++;
        cur_g += prev == cur;
        if (cur_g > max_g) max_g = cur_g;
        if (prev != cur ) cur_g = 1;
        prev = cur;
    }

    // compute ratio
    cout << max(max_g * max_g, count_x * count_y) << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
