// 2022-11-12
// problem C

#include <iostream>
#include <map>
#include <string>
// #include <vector>

using namespace std;

void solve() 
{
    int n;
    scanf("%d", &n);
    int cur_sum = 0, cur_elem;
    int cur;
    map<int, int> unpaired;
    for (int i = 0; i < n; ++i)
    {
        if (unpaired.find(-cur) == unpaired.end()) {
            cin >> cur;
            unpaired[cur] = i;
          // not found
        } else {
          // found
        }

    }
}

int main() 
{
    int t;
    scanf("%d", &t);
    while (t--) solve();
    return 0;
}
