impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        } 

        let mut reverse_number: i32 = 0;
        let mut temp: i32 = x;

        while temp != 0 {
            let digit: i32 = temp % 10;
            reverse_number = (reverse_number * 10) + digit;
            temp = (temp as f64 / 10.) as i32;
        } 

        x == reverse_number
    }
}