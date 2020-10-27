#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 

    int n;
    string sUserInput;
    string sEvenOut;
    string sOddOut;
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; i++){
        sUserInput = "";
        sEvenOut = "";
        sOddOut = "";
        
        cin >> sUserInput;
        for (int j = 0; j < sUserInput.size(); j+=2){
            sEvenOut += sUserInput[j];
        }
        for (int j = 1; j < sUserInput.size(); j+=2){
            sOddOut += sUserInput[j];
        }
        cout << sEvenOut << " " << sOddOut << endl;
    }
    return 0;
}
