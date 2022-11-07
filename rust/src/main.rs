#![allow(dead_code)]

use std::str::FromStr;

fn next_value(num: String) -> i64 {
    i64::from_str(&num).expect("error parsing args")
}

// --- Day 1: Sonar Sweep ---
// scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, and so on
// figure out how quickly the depth increases:
// count the number of times a depth measurement increases from the previous measurement

fn aoc_day1(inp: String) -> i64 {
    // let next_value = | num: String | u64::from_str(&num).expect("error parsing args");

    let mut ans = 0;
    let mut first_entry = true;
    let mut prev = 0;
    for num in inp.split_whitespace() {
        if first_entry {
            prev = next_value(num.to_string());
            first_entry = false;
            continue;
        }

        let cur = next_value(num.to_string());
        ans += (cur > prev) as i64;
        prev = cur;
    }

    ans
}

// --- Day 2: Dive! ---
// submarine can take a series of commands like forward, down, or up
// forward increases the horizontal position, down increases the depth, up decreases the depth
// your horizontal position and depth both start at 0
// calculate the horizontal position and depth you would have after following the planned course.
// What do you get if you multiply your final horizontal position by your final depth?

fn aoc_day2(inp: String) -> i64 {
    let mut horizontal = 0;
    let mut vertical = 0;
    let mut direction = "".to_string();

    for lexeme in inp.split_whitespace() {
        let lex = lexeme.to_string();

        if direction.len() == 0 {
            direction = lex;
            continue;
        }

        let val = next_value(lex);

        if direction == "forward" {
            horizontal += val as i64;
        } else {
            vertical += if direction == "up" {
                -(val as i64)
            } else {
                val as i64
            }
        }
        direction = "".to_string();
    }

    horizontal * vertical
}

fn aoc_day2_ver2(inp: String) -> i64 {
    let mut horizontal = 0;
    let mut vertical = 0;

    for (direction, val) in inp.split_whitespace() {
        let direct_str = direction.to_string();
        let val_int: u64 = val.parse();

        if direct_str == "forward" {
            horizontal += val_int;
        } else {
            vertical += if direction == "up" {
                -(val_int as i64)
            } else {
                val_int as i64
            }
        }
    }

    (horizontal as i64) * vertical
}
fn fn_caller(f: fn(String) -> i64, arg: String) -> i64 {
    f(arg)
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_aoc_day1() {
        let arg = "199 200 208 210 200 207 240 269 260 263".to_string();
        assert_eq!(fn_caller(aoc_day1, arg), 7)
    }

    #[test]
    fn test_aoc_day2() {
        assert_eq!(
            aoc_day2(("forward 5 down 5 forward 8 up 3 down 8 forward 2").to_string()),
            150
        )
    }

    #[test]
    fn test_aoc_day2_var2() {
        assert_eq!(
            aoc_day2_ver2(("forward 5 down 5 forward 8 up 3 down 8 forward 2").to_string()),
            150
        )
    }
}
