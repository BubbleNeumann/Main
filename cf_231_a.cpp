#include <iostream>
#include <string>

using namespace std;

int main() 
{
    int n, answ = 0;
    int one, two, three;
    cin >> n;
    while (n--)
    {
        cin >> one >> two >> three;
        answ += (one && two) || (two && three) || (one && three);
    }

    cout << answ << "\n";
    return 0;
}
