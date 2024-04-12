/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long left = 0;
        long right = n;

        while( left <= right) {
            long mid = (left + right) / 2;
            long output = guess(mid);

            if (output == -1)
                right = mid - 1;
            else if(output == 1)
                    left = mid + 1;
                else 
                    return mid;
    }
    return -1;
    }
};