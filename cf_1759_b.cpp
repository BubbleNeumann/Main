// 2022-11-18
// Div.3 problem B
// didn't solve during the contest
// possibly wrong indeces

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void solve() 
{
    int m, s; // m = num, s = summ
    cin >> m >> s;

    int b[50];
    int b_max = -1;
    int b_summ = 0;
    // read array
    for (int i = 0; i < m; ++i)
    {
        cin >> b[i];
        if (b[i] > b_max) b_max = b[i];
        b_summ += b[i];
    }

    sort(b, b + m);

    // for (int i = 1, j = b[0], l = 0; j <= b_max; i = b[l++],j = b[l])
    // {
    //     for (int k = b[l-1] + 1; k < j; s -= k++);
    //     // if (s < 0 && i != b_max -1 ) ans = false;
    // }
    // for (int i = 1, j = b[0]; j <= b_max; j = b[++i])
    // {
    //     for (int k = b[i-1] + 1; k < j; s -= k++);
    // }

    for (int i = 0, start = 1, end = b[i]; i < m; start = end + 1, end = b[++i])
    {
        for (int num = start; num < end; s -= num++);
    }

    // cout << "\n" << s << " ";

    // int summ = 0;
    // for (int i = 0; i < b_max; summ += ++i);

    while (s > 0) s -= ++b_max;        

    !s ? cout << "yes\n" : cout << "no\n";
}

int main() 
{
    int t;
    scanf("%d", &t);
    while (t--) solve();
    return 0;
}

