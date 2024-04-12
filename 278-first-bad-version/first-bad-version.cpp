// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long left = 0;
        long right = n;

        while (left <= right) {
            long mid = (left + right) / 2;

            bool isBad = isBadVersion(mid);

            if(isBad) {
                if(isBadVersion(mid - 1)) {
                    right = mid - 1;
                }
                else {
                    return mid;
                }
            }
            else {
                if(isBadVersion(mid + 1))
                    return mid + 1;
                else 
                    left = mid + 1;
            }
        }

        return -1;
    }
};