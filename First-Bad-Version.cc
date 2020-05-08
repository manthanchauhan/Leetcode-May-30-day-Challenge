// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        
//      long long is neccessary for large test cases to pass
        long long int beg = 0;
        long long int end = n;
        
        while (true) {
            long long int mid = (beg + end)/2;
            
            if (isBadVersion(mid)) {
                if (mid + 1 == end) {
                    if (end - beg == 1) return beg;
                    else return (isBadVersion(beg))?(beg):(mid);
                }
                else end = mid+1;
            }
            else beg = mid+1;
        }
    }
};
