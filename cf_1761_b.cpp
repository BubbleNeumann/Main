// 2022-11-20
// Pinely Round 1 (Div. 1 + Div. 2)
// problem B

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve() 
{
    int len;
    cin >> len;

    vector<int> a;
    int cur;
    for (int i = 0; i < len; ++i)
    {
        cin >> cur;
        a.push_back(cur);
    }

    unsigned int cur_len = len, counter = 0, ind = 0;
    int stuck_counter =0;
    while (cur_len > 2)
    {
        // cout << stuck_counter << " ";
        cout << "on ind " << ind << "\n";
        // 
        if ( a[(ind%cur_len)] == a[(ind+1)%cur_len] ||a[(ind%cur_len)] == a[(ind-1+(3*(cur_len==3)))%cur_len])
        {
            cout << "delete auto ";
            a.erase(a.begin() + (ind % cur_len));
            --cur_len;
            stuck_counter = 0;
            continue;
        }
        
        // player chooses best pos if possible
        if (a[(ind+1)%cur_len] != a[(ind-1)%cur_len] || stuck_counter == cur_len)
            // || ((ind+1)%cur_len) == ((ind-1)%cur_len) || ((ind+1)%cur_len) == (ind%cur_len))
        {
            a.erase(a.begin() + (ind % cur_len));
            cout << "\nremoved ind " << ind%cur_len << "\n";
            --cur_len;
            ++ind;
            ++counter;
            stuck_counter = 0;
        }
        else
        {
            ++ind;
            ++stuck_counter;
        }
    }

    if (a[0] == a[1]) cur_len = 1;
    cout << counter + cur_len << "\n";
}

int main() 
{
    int t;
    scanf("%d", &t);
    while (t--) solve();
    return 0;
}


