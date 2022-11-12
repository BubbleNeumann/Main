// 2022-11-12
// Div.2 problem B
// exeeded time limit during the contest

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve() 
{
    int n; // str len
    cin >> n;
       
    string str, substr;
    cin >> str;

    int distinct = n, count; // number of "distinct" substrings
                      // 
    vector<int> nums;
    for (int i = 2; i <= n; ++i) // len of substr
    {
        for (int j = 0; j < n - i + 1; ++j) // starting index of substr
        {
            bool is_distinct = true;
            nums = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            substr = str.substr(j, i);
            count = 0; // number of distinct symbols in substring

            for (auto k : substr) count += ++nums[k - '0'] == 1;
            
            for (auto k : nums)
            {
                if (k > count)
                {
                    is_distinct = false; 
                    break;
                }
            }
            
            // cout << "sub = " << substr << ", " << is_distinct << " count = " << count << "\n";
            distinct += (count == i) || is_distinct ;
        }
    }
                      
    cout << distinct << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
