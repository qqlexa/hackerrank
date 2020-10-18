// https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int reverseNumber(int number){
    string reversedNumber = to_string(number);
    int n = reversedNumber.length();
    // 
    for (int i = 0; i < n / 2; i++){
        char tempSymbol = reversedNumber[i];
        reversedNumber[i] = reversedNumber[n - i - 1];
        reversedNumber[n - i - 1] = tempSymbol;
    }
    return stoi(reversedNumber); 
}

// Complete the beautifulDays function below.
int beautifulDays(int i, int j, int k) {
    int result = 0;

    if (i > j){
        int temp = i;
        i = j;
        j = temp;
    }
    int x = i;
    while (x <= j){
         // x - reverse(x)
        int difference = x - reverseNumber(x);
        // abs(x - reverse(x))
        if (difference < 0){
            difference = -difference;
        }
        if (!(difference % k)){
            result++;
        }
        x++;
    } 


    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ijk_temp;
    getline(cin, ijk_temp);

    vector<string> ijk = split_string(ijk_temp);

    int i = stoi(ijk[0]);

    int j = stoi(ijk[1]);

    int k = stoi(ijk[2]);

    int result = beautifulDays(i, j, k);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
