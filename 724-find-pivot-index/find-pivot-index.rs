impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        
        let total_sum: i32 = nums.iter().sum();
        let mut left_sum = 0;

        for i in 0..nums.len() {

            let right_sum = total_sum - left_sum - nums[i];

            if right_sum == left_sum {
                return i as i32;
            } else {
                left_sum += nums[i];
            }
        }

        return -1; 
    }
}