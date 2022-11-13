#include <iostream>
#include <string>
#include <cassert>

using namespace std;

#define const bool testing = 0;

int solve(int val1, int val2)
{
    return 0;
}

void TestSolve(int val1, int val2, int expected_res)
{
    assert(solve(val1, val2) == expected_res);
}

int main()
{
    int t, val1, val2;
    cin >> t;
    while (t--)
    {
        cin >> val1 >> val2;
        cout << solve(val1, val2) << "\n";
        // TestSolve();
    }
        
    return 0;
}
