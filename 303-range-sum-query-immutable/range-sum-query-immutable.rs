struct NumArray {
    nums: Vec<i32>,
    prefix_sum: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        let mut prefix_sum = Vec::new();

        prefix_sum.push(nums[0]);

        for i in 1..nums.len() {
            prefix_sum.push(prefix_sum[i - 1] + nums[i]);
        }

        NumArray { nums, prefix_sum }
    }
    
    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let mut return_value = self.prefix_sum[right as usize];
        let mut temp = 0;

        while temp < left {
            return_value -= self.nums[temp as usize];
            temp += 1;
        }

        return_value

    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(left, right);
 */