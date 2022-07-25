// July 24th, 2022
// https://codeforces.com/problemset/problem/1706/A

#include <iostream>
#include <vector>

int main()
{
    int t, indlen, strlen, cur_ind;
    std::vector<char> res;
    std::cin >> t;

    for (t; t; t--)
    {
        std::cin >> indlen >> strlen;
        char* str = new char[strlen];
        for (int i = 0; i < strlen; str[i] = 'B', i++);

        for (int i=indlen; i; i--)
        {
            std::cin >> cur_ind;

            cur_ind =  std::min(cur_ind, strlen + 1 - cur_ind);

            if (str[cur_ind-1] == 'A')
            {
                str[strlen + 1 - cur_ind-1] = 'A';
            }
            else
            {
                str[cur_ind-1] = 'A';
            }
        }
        
        for (int i = 0; i < strlen; res.push_back(str[i]), i++);
        res.push_back('\n');
        delete [] str;      
    }   

    for (char i : res)
    {
        std::cout << i;
    }

    return 0;
}