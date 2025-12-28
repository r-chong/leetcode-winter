class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string res;
        int len = word1.size() + word2.size();
        res.reserve(len);
        int i = 0, j = 0;

        while ((i == j) && !(i + j == len)) {
            if (i < word1.size()) {
                res += word1[i++];
            }
            if (j < word2.size()) {
                res += word2[j++];        
            }
        }

        for (; i < word1.size(); i++) {
            res += word1[i];
        }

        for (; j < word2.size(); j++) {
            res += word2[j];
        }

        return res;
    };
};