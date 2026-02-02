class Solution {
public:
    int reverseBits(int n) {
        unsigned int res = 0;

        for (int i = 0; i < 32; ++i) {
            res <<= 1;
            res |= (n & 1);
            n >>= 1;
        }

        return res;
    }
};

// s <<= 1 is shift left by 1
// a |= b is the same as a = a | b