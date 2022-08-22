use std::str::FromStr;

// count the number of times a depth measurement increases from the previous measurement
fn aoc_day1(inp: String) -> u64 {

    let next_value = | num: String | u64::from_str(&num).expect("error parsing args");

    let mut answ = 0;
    let mut first_entry = true;
    let mut prev = 0;
    for num in inp.split_whitespace() {

        if first_entry {
            prev = next_value(num.to_string());
            first_entry = false;
            continue;
        }
            
        let cur = next_value(num.to_string());

        answ += (cur > prev) as u64;

        prev = cur;
    }

    answ
}


fn main() {}

#[cfg(test)]
mod tests {
    use crate::aoc_day1;
    #[test]
    fn test_aoc_day1() {
        assert_eq!(aoc_day1(("199 200 208 210 200 207 240 269 260 263").to_string()), 7)
    }
}
