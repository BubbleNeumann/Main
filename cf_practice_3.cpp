#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve()
{
   int counter = 0, inp_len, templ_len;
   string inp, templ;

   cin >> inp >> templ;

   inp_len = inp.length();
   templ_len = templ.length();

   int i;

   vector<int> indeces;

   templ_len > inp_len ? i = inp_len : i = 0;

   for (; i < inp_len - templ_len + 1; ++i)
   {
       // internal_counter = 0;
       for (int j = 0, internal_counter = 0; j < templ_len; ++j)
       {
           internal_counter += inp[i + j] == templ[j] || templ[j] == '?';
           if (internal_counter == templ_len)
           {
               ++counter;
               indeces.push_back(i);
           }
       }
   }
   
  cout << counter << "\n";
  for (auto i : indeces) cout << i << " ";
  cout << "\n";
}

int main()
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
