#include <iostream>
#include <fstream>
#include <string>
#include <cassert>


using namespace std;

const bool testing = true;
const string file_name = "file.txt";

int solve(int val1, int val2)
{
    int n_test;
    // ifstream in_file_stream(file_name);
    return 0;
}

void testSoluition(int val1, int val2, int expected_res)
{
    assert(solve(val1, val2) == expected_res);
}

void test()
{
    int t, val1, val2;
    cin >> t;
    while (t--)
    {
        // cin >> val1 >> val2;
        // cout << solve(val1, val2) << "\n";
        // TestSolve();
    }
}

void solve()
{
    
}


int main()
{
    testing ? test() : solve();
    return 0;
}
