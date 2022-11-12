// 2022-11-09

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    string str;
    cin >> str;

    int longest_palindrome = 1;
    for (int i = 2; i <= str.length(); ++i) // current palindrome expectation
    {
        for (int j = 0; j <= i / 2; ++j) // iterate over prefix
        {
           if (str[j] != str[i - j -1]) break; 
           if (j == (i - j -1) || (j + 1 == (i-j-1) && i%2 == 0)) longest_palindrome = i;
        }
    }

    cout << longest_palindrome << "\n";
}

int main() 
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
