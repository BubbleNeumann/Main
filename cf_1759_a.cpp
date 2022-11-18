// 2022-11-18
// Div.3 problem A

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    int str_len;

    string str;
    cin >> str;

    str_len = str.length();
    
    auto prev_ch = str[0];
    if (prev_ch != 'Y' && prev_ch != 'e' && prev_ch != 's') 
    {
        cout << "no\n";
        return;
    }
    
    bool ans = true;
    for (int i = 1; i < str_len; ++i)
    {
        auto cur_ch = str[i];

        switch (cur_ch)
        {
            case 'Y': if (prev_ch != 's') ans = false; break;
            case 'e': if (prev_ch != 'Y') ans = false; break;
            case 's': if (prev_ch != 'e') ans = false; break;
            default: ans = false;
        }

        if (!ans) break;
        prev_ch = cur_ch;
    }
    
    ans ? cout << "yes\n" : cout << "no\n";
}

int main() 
{
    int t;
    scanf("%d", &t);
    while (t--) solve();
    return 0;
}
