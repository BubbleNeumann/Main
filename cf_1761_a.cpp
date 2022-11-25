// 2022-11-20
// Pinely Round 1 (Div. 1 + Div. 2)
// problem A

#include <iostream>
#include <string>

using namespace std;

void solve() 
{
    int a, b , n;
    cin >> n >> a >> b;
    ((n - a - b > 1) || (n == 1 && (a+b) == 2) || ( a == n && b == n)) 
        ? cout << "yes\n" : cout << "no\n";
}

int main() 
{
    int t;
    scanf("%d", &t);
    while (t--) solve();
    return 0;
}

