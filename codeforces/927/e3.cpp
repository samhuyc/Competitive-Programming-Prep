#include <iostream>
#include <vector>
#include <string>
#include <algorithm> 

using namespace std;

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        string input;
        cin >> input;

        input.erase(0, min(input.find_first_not_of('0'), input.size()-1));
        reverse(input.begin(), input.end());

        vector<int> valint;
        vector<int> ans;

        for(char c : input) {
            valint.push_back(c - '0');
        }
        ans = valint;

        for(int i = 0; i < valint.size(); ++i) {
            int carry = 0;
            for(int j = 0; j < i; ++j) {
                ans[j] += valint[i] + carry;
                carry = 0;
                int currdigit = j;
                if(ans[currdigit] >= 10) {
                    ans[currdigit] -= 10;
                    carry = 1;
                    currdigit++;
                    if(currdigit >= ans.size()) {
                        ans.push_back(0);
                    }
                    while(carry != 0) {
                        ans[currdigit] += carry;
                        carry = 0;
                        if(ans[currdigit] >= 10) {
                            ans[currdigit] -= 10;
                            carry = 1;
                        }
                        currdigit++;
                        if(currdigit >= ans.size()) {
                            ans.push_back(0);
                        }
                    }
                }
            }
        }

        string result = "";
        for(int num : ans) {
            result += to_string(num);
        }
        reverse(result.begin(), result.end());


        result.erase(0, min(result.find_first_not_of('0'), result.size()-1));
        cout << (result.empty() ? "0" : result) << endl;
    }

    return 0;
}
