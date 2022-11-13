#include <iostream>
#include <string>

using namespace std;
int main()
{
    int n, len;
    string str, newstr;
    cin >> n;
    while (n--)
    {
        cin >> str;
        len = str.length();
        len > 10 ? cout << str[0] << len-2 << str[len-1] << "\n" : cout << str << "\n";
    }
    
    return 0;
}
