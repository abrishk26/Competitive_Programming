impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections;

        let mut hash_table: collections::HashMap<i32, i32> = collections::HashMap::new();
        let mut result: Vec<i32> = Vec::new();

        for i in 0..nums.len() {
            if hash_table.contains_key(&(nums[i])) {
                result.push(i as i32);
                result.push(hash_table.get(&(nums[i])).copied().unwrap());
                break;
            } else {
                hash_table.insert(target - nums[i], i as i32);
            }
        }

        return result
    }
}