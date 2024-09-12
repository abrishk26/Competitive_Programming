struct NumArray {
    nums: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(mut nums: Vec<i32>) -> Self {
        
        for i in 1..nums.len() {
            nums[i] += nums[i - 1];
        }

        NumArray { nums }
    }
    
    fn sum_range(&self, left: i32, right: i32) -> i32 {
        
        if left == 0 {
            self.nums[right as usize]
        } else {
            self.nums[right as usize] - self.nums[(left - 1) as usize]
        }

    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(left, right);
 */