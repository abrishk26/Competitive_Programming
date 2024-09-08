use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let map: HashMap<char, i32> = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]);

        let roman_number: Vec<char> = s.chars().collect();
        let mut integer: i32 = 0;
        let n = roman_number.len();
        let mut i: usize = 0;

        while i < n {
            if (i < (n - 1)) &&  map.get(&(roman_number[i])).copied().unwrap() < map.get(&(roman_number[i + 1])).copied().unwrap() {
                
                integer += map.get(&(roman_number[i + 1])).copied().unwrap() - map.get(&(roman_number[i])).copied().unwrap();
                i += 1;

            } else {
                    integer += map.get(&(roman_number[i])).copied().unwrap();;
            }

            i += 1;
        }

        return integer
        

    }
}