use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
        let mut hash_table: HashMap<i32, i32> = HashMap::new();
    
        for i in 0..nums.len() {
            if hash_table.contains_key(&(nums[i])) {
               return vec![i as i32, hash_table.get(&(nums[i])).copied().unwrap()];
            } else {
                hash_table.insert(target - nums[i], i as i32);
            }
        }

        unreachable!()
    }
}