// 2022-11-06
// CodeTON problem C

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    long long int n;
    cin >> n;
       
    string a, b;
    cin >> a;
    cin >> b;

    // todo : replace with forn ??

    long long int count_a_left_gr = 1, count_a_right = 1, count_b_left_gr = 1, count_b_right_gr = 1 ;


    // or count number of state changes
    // 
    for (int i = 0; i < n / 2; ++i)
    {
        
        // if ((a.at(i) == b.at(i)) == eq)
        // if (a.)
        
        // cur = inp.at(i) == '1';
        // cur == 0 ? count_x++ : count_y++;
        // cur_g += prev == cur;
        // if (cur_g > max_g) max_g = cur_g;
        // if (prev != cur ) cur_g = 1;
        // prev = cur;
    }

    // compute ratio
    // cout << max(max_g * max_g, count_x * count_y) << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
