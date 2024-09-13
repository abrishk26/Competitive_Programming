impl Solution {
    pub fn min_start_value(nums: Vec<i32>) -> i32 {
        let mut sum: i32 = 0;
        let mut min_sum: i32 = 0;

        for i in &nums {
            sum += *i;
            min_sum = min_sum.min(sum);
        }

        return 1 - min_sum.min(0);
        
    }
}