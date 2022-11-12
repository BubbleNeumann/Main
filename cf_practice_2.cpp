// 2022-11-09

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    string str;
    cin >> str;

    int count = 0;
    string suff, pref, subst;
    for (int i = 1; i < str.length(); ++i)
    {
        pref = str.substr(0, i);
        suff = str.substr(str.length()-i);
        if (pref == suff) continue;

        count += 2; // count pref and suff
        for (int j  = 1; j < str.length() - i; ++j)
        {
            subst = str.substr(j, i);
            if (subst == pref || subst == suff) ++count;
        }
    }

    cout << count << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
